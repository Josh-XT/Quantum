import os
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer, IBMQ
from qiskit.tools.visualization import plot_histogram
from dotenv import load_dotenv
# Load the API key from the .env file
load_dotenv()
IBM_TOKEN = os.getenv('IBM_TOKEN')
IBMQ.delete_account()
IBMQ.save_account(IBM_TOKEN)
IBMQ.load_account()

# Define functions to simplify interactions with quantum computers
def get_quantum_computer(qubits=2, simulation=False, verbose=False):
    # Finds a quantum computer at IBM with the lowest queue as long as it has enough qubits for the circuit
    if simulation == False: # Execute the circuit on a quantum computer at IBM
        lowest = float('inf')
        provider = IBMQ.get_provider(hub='ibm-q')
        for backend in provider.backends():
            try:
                if "simulator" not in backend.name():
                    queue = backend.status().pending_jobs
                    qubit_count = len(backend.properties().qubits)
                    if qubit_count >= qubits:
                        if queue < lowest:
                            lowest = queue
                            quantum_comp = provider.get_backend(backend.name())
                        if verbose == True:
                            print(f"Quantum Computer {backend.name()} has {queue} queued jobs and {qubit_count} qubits")
                    else:
                        if verbose == True:
                            print(f"Quantum Computer {backend.name()} has {qubit_count} qubits, but we need {qubits} qubits")
            except:
                print(f"Quantum Computer {backend.name()} is not operational")
        if quantum_comp is None:
            print(f"No Quantum Computers available with {qubits} qubits, using simulator")
    if simulation == True or quantum_comp is None: # Execute the circuit on the simulator
        quantum_comp = Aer.get_backend('qasm_simulator')
    if verbose == True:
        print(f"Using Quantum Computer: {quantum_comp.name()} with {quantum_comp.status().pending_jobs} queued jobs")
    return quantum_comp

def prepare_quantum_circuit(qubits=2, classical_bits=2, simulation=False, verbose=False):
    # Create registers for the circuit
    quantum_register = QuantumRegister(qubits)
    classical_register = ClassicalRegister(classical_bits)
    # Create a Quantum Circuit
    quantum_circuit = QuantumCircuit(quantum_register, classical_register)
    # Get a quantum computer with at least the number of selected qubits for the circuit and the lowest queue, or the simulator
    quantum_computer = get_quantum_computer(qubits=qubits, simulation=simulation, verbose=verbose)
    return quantum_circuit, quantum_register, classical_register, quantum_computer

def execute_quantum_circuit(quantum_circuit, quantum_comp, shots=500, verbose=False):
    queue_position = quantum_comp.status().pending_jobs + 1
    if verbose == True:
        print(f"Your job is number {queue_position} in the queue on {quantum_comp.name()}.  Please wait...")
    result = execute(quantum_circuit, backend=quantum_comp, shots=shots).result()
    plot_histogram(result.get_counts(quantum_circuit))
    if verbose == True:
        print(f"{result.status} in {result.time_taken} seconds on {quantum_comp.name()}")
    most_common = result.get_counts(quantum_circuit).most_frequent()
    if verbose == True:
        probability = 100 * float(result.get_counts(quantum_circuit)[most_common])/float(shots)
        print(f"The most common result was {most_common} with {probability}% probability")
    return most_common

def bell_state_circuit(quantum_circuit, quantum_register, classical_register):
    # Build a Bell State circuit
    # https://en.wikipedia.org/wiki/Bell_state
    quantum_circuit.h(quantum_register[0])
    quantum_circuit.cx(quantum_register[0], quantum_register[1])
    quantum_circuit.measure(quantum_register, classical_register)
    quantum_circuit.draw()
    return quantum_circuit

# Set up the circuit
quantum_circuit, quantum_register, classical_register, quantum_computer = prepare_quantum_circuit(qubits=2, classical_bits=2, simulation=False, verbose=True)
# Build a Bell State circuit
quantum_circuit = bell_state_circuit(quantum_circuit, quantum_register, classical_register)

# Execute the circuit
result = execute_quantum_circuit(quantum_circuit, quantum_computer, shots=500, verbose=True)
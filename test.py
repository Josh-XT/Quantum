from qiskit import *
from dotenv import load_dotenv
import os
from qiskit.tools.visualization import plot_histogram
# Load the API key from the .env file
load_dotenv()
IBM_TOKEN = os.getenv('IBM_TOKEN')
IBMQ.save_account(IBM_TOKEN)

IBMQ.load_account()
provider = IBMQ.get_provider(hub='ibm-q')

# Create a Quantum Register with 2 qubits.
qr = QuantumRegister(2)
# Create a Classical Register with 2 bits.
cr = ClassicalRegister(2)
# Create a Quantum Circuit
circuit = QuantumCircuit(qr, cr)

circuit.h(qr[0])

circuit.cx(qr[0], qr[1])

circuit.measure(qr, cr)

circuit.draw()

# Execute the circuit on a simulator backend
simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend = simulator, shots=1024).result()
plot_histogram(result.get_counts(circuit))
circuit.draw()
# Execute the circuit on a real device backend
backend = provider.get_backend('ibmq_16_melbourne')
job = execute(circuit, backend, shots=1024)
result = job.result()
counts = result.get_counts(circuit)
print(counts)

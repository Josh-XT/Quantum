# Quantum Computing

After reading Stephen Hawking's book **``The Theory of Everything``**, my interest in Quantum Mechanics and the accompanying concepts took the top seat in what I ~~wanted~~ needed to know more about.  Many books later, I started looking in to Quantum Computing to see how these concepts could be used in software development and was very happy to learn that I could use ``Python`` to work with Quantum Computers.  In my search online, I found that ``IBM`` allows people to test their code on their actual Quantum Computers for free!  The down side is that the capabilities are limited due to current hardware, but it is still great for getting started.

Enter ``Qiskit``, a ``Python`` package from ``IBM`` to interface with their Quantum Computers or to simulate one. I wrote some functions that I found would be useful and then some that I found fun to play with.  I also participated a workshop for ``Amazon Braket`` and learned how I could execute my ``Qiskit`` code on ``Amazon Braket`` devices.

To share part of my learning journey, I am leaving all that I learn open for others to learn from or use in this repository. 

# Quantum Alethiometer (Joke function)

An example of one of the fun things: I made a Quantum Alethiometer (for fans of The Golden Compass / His Dark Materials) that you can make a statement to and it will evaluate rather the statement is true or false using the Deutsch Jozsa algorithm on a quantum computer.  The concept behind the alethiometer is that you can ask it anything (if you know how) and it will give you the answer if you know how to decode it.  My alethiometer function does both of those things to allow you to make your statement in plain English.

The Alethiometer says that the statement "I should eat less chocolate" is False.  I accept this answer.

Unfortunately due to the limited access available to quantum computers currently, I only have 7 qubits to work with and a single letter requires 8 for the binary conversion, so it is all just on a quantum computer simulation running on my computer currently.  The answers it gives aren't coming from the universe (or angels) currently, they're just coming from a computer.

# Tests for learning Quantum Computer Programming with Python and Qiskit

## Create or log in to IBM account
Go to https://quantum-computing.ibm.com/ log in with GitHub account, click the user icon in the top right, then ``Account Settings``, then copy the API token.

## Add API token to environment variable file
Create a ``.env`` file in this folder with the following content:

```
IBM_TOKEN=PASTE_YOUR_IBM_TOKEN_HERE
```

## Install dependencies

Run the following in the terminal:

```
pip install --upgrade -r requirements.txt
```

Install the ``Jupyter`` extension for VSCode

## Try it out

For Qiskit, Open ``qk.ipynb`` in VSCode from the ``qiskit-tests`` folder, run each step from top to bottom to see outputs.

It can also be viewed in the browser by [clicking here.](https://github.com/Josh-XT/Quantum/blob/main/qk.ipynb)
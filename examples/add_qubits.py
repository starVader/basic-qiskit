from matplotlib import pyplot as plt
from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram
from qiskit_aer import Aer

if __name__ == '__main__':
    # Create a quantum circuit with 2 qubits
    qc = QuantumCircuit(2)

    # Prepare the first qubit in |0> (default state)
    qc.h(0)  # Apply Hadamard gate to the first qubit

    # Apply a CNOT gate (control = qubit 0, target = qubit 1) create entanglement
    qc.cx(0, 1)
    # Visualize the circuit
    print(qc)

    # Simulate the statevector
    simulator = Aer.get_backend('statevector_simulator')
    result = simulator.run(qc, backend=simulator).result()
    statevector = result.get_statevector()
    print("Statevector:\n", statevector)

    qc.measure_all()  # Add measurement for classical results
    simulator = Aer.get_backend('qasm_simulator')
    result = simulator.run(qc, backend=simulator, shots=1024).result()
    counts = result.get_counts()

    # Plot the histogram of results
    print("\nMeasurement Results:")
    print(counts)
    plot_histogram(counts)
    plt.show()
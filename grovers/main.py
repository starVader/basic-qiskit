import math

from qiskit import QuantumCircuit, generate_preset_pass_manager
from qiskit.circuit.library import GroverOperator
from qiskit.visualization import plot_distribution
from qiskit_ibm_runtime import SamplerV2 as Sampler
from qiskit_ibm_runtime.fake_provider import FakeManilaV2


# from auth.authenticate import authenticate
from grovers.oracles import grover_oracle

if __name__ == '__main__':
    marked_states = ["011", "100"]

    oracle = grover_oracle(marked_states)
    grover_op = GroverOperator(oracle)

    qc = QuantumCircuit(grover_op.num_qubits)
    # Create even superposition of all basis states
    qc.h(range(grover_op.num_qubits))
    # Apply Grover operator the optimal number of times
    optimal_num_iterations = math.floor(
        math.pi / (4 * math.asin(math.sqrt(len(marked_states) / 2 ** grover_op.num_qubits)))
    )

    qc.compose(grover_op.power(optimal_num_iterations), inplace=True)
    # Measure all qubits
    qc.measure_all()
    # Optimize problem for quantum execution
    pm = generate_preset_pass_manager(optimization_level=3)
    circuit_isa = pm.run(qc)
    circuit_isa.draw(output="mpl", idle_wires=False, style="iqp")

    # auth = authenticate()
    # run on IBM server
    # backend = auth.least_busy(operational=True, simulator=False)
    # sampler = Sampler(backend)

    options = {"simulator": {"seed_simulator": 42}}
    fake_manila = FakeManilaV2()
    pm = generate_preset_pass_manager(backend=fake_manila, optimization_level=1)
    isa_qc = pm.run(qc)
    sampler = Sampler(mode=fake_manila, options=options)
    sampler.options.default_shots = 10_000
    result = sampler.run([circuit_isa]).result()
    dist = result[0].data.meas.get_counts()
    plot_distribution(dist)

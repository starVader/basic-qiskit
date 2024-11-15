from qiskit import QuantumCircuit
from qiskit_ibm_runtime import SamplerV2 as Sampler


def verify_set_up(auth):
    """
        verifies the connection with IBM quantum server and job execution
    :param auth: Auth object based on API key
    """
    # Create empty circuit
    example_circuit = QuantumCircuit(2)
    example_circuit.measure_all()

    # You'll need to specify the credentials when initializing QiskitRuntimeService, if they were not previously saved.
    backend = auth.least_busy(operational=True, simulator=False)

    sampler = Sampler(backend)
    job = sampler.run([example_circuit])
    print(f"job id: {job.job_id()}")
    result = job.result()
    print(result)

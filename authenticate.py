import os

from qiskit_ibm_runtime import QiskitRuntimeService

def authenticate():
    # Save an IBM Quantum account and set it as your default account.
    QiskitRuntimeService.save_account(
        channel="ibm_quantum",
        token=os.getenv("API_KEY"),
        set_as_default=True,
        # Use `overwrite=True` if you're updating your token.
        overwrite=True,
    )
    return QiskitRuntimeService()

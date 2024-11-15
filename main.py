from auth.authenticate import authenticate
from hello_world.sample import hello_qubit
from verification.verify_setup import verify_set_up


if __name__ == '__main__':
    print("Initializing")
    hello_qubit()
    auth = authenticate()
    verify_set_up(auth)


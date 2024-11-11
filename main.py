# This is a sample Python script.
from authenticate import authenticate
from hello_world import hello_world
from verify_setup import verify_set_up

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Initializing")
    hello_world()
    auth = authenticate()
    # verify_set_up(auth)

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/

from modules import system

def dispatch(command, action, args):
    if command == "system":
        system.handle(action, args)

    else:
        print("Unknown command")
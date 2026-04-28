def parse_input(user_input):
    parts = user_input.split()

    command = parts[0] if len(parts) > 0 else None
    action = parts[1] if len(parts) > 1 else None
    args = parts[2:] if len(parts) > 2 else []

    return command, action, args
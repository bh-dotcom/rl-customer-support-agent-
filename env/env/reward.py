def calculate_reward(action, state):
    if action == "CLOSE" and state["resolved"]:
        return 10
    elif action == "ESCALATE" and state["complex"]:
        return 5
    elif action == "RESPOND":
        return 2
    elif action == "REQUEST_INFO":
        return 1
    return -3

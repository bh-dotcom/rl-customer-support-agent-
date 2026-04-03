class BaselineAgent:
    def act(self, state):
        if state["complex"]:
            return "ESCALATE"
        elif state["resolved"]:
            return "CLOSE"
        elif state["sentiment"] == "angry":
            return "RESPOND"
        return "REQUEST_INFO"

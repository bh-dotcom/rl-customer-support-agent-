def evaluate(history):
    success = sum(1 for h in history if h["action"] == "CLOSE" and h["state"]["resolved"])
    total = len(history)

    return {
        "success_rate": success / total if total else 0,
        "total_steps": total
    }

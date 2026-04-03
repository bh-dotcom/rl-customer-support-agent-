from env.support_env import SupportEnv
from agents.baseline_agent import BaselineAgent
from evaluator.grader import evaluate

env = SupportEnv("data/sample_tickets.json")
agent = BaselineAgent()

state = env.reset()
done = False

history = []
step = 1

while not done:
    action = agent.act(state)
    next_state, reward, done, _ = env.step(action)

    print(f"Step {step} → Action: {action} → Reward: {reward}")

    history.append({
        "state": state,
        "action": action,
        "reward": reward
    })

    state = next_state
    step += 1

print("\nEvaluation:", evaluate(history))

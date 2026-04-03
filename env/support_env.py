import json
from env.reward import calculate_reward

class SupportEnv:
    def __init__(self, data_path):
        with open(data_path) as f:
            self.tickets = json.load(f)
        self.index = 0
        self.max_steps = len(self.tickets)

    def reset(self):
        self.index = 0
        return self._get_state()

    def step(self, action):
        state = self._get_state()
        reward = calculate_reward(action, state)

        self.index += 1
        done = self.index >= self.max_steps

        next_state = self._get_state() if not done else None

        return next_state, reward, done, {}

    def _get_state(self):
        return self.tickets[self.index]

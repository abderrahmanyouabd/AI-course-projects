import numpy
import random


class QLearningAgent:
    def __init__(self, n_states, n_actions, learning_rate):
        self.n_states = n_states
        self.n_actions = n_actions
        self.learning_rate = learning_rate
        self.q_table = numpy.zeros((n_states, n_actions))

    def act(self, state, epsilon):
        random_int = random.uniform(0, 1)

        if epsilon > random_int:
            action = numpy.argmax(self.q_table[state])
        else:
            action = random.randint(0, self.n_actions - 1)

        return action

    def learn(self, state, new_state, gamma, reward, action):
        old_value = self.q_table[state][action]
        new_value = reward + gamma * max(self.q_table[new_state])

        self.q_table[state][action] = old_value + self.learning_rate * (new_value - old_value)


def main():
    n_states = 5  # Define the number of states
    n_actions = 2  # Define the number of actions
    learning_rate = 0.1  # Define the learning rate
    gamma = 0.9  # Define the discount factor
    epsilon = 0.2  # Define the exploration rate
    n_episodes = 100  # Define the number of episodes
    max_steps = 10  # Define the maximum steps per episode

    agent = QLearningAgent(n_states, n_actions, learning_rate)

    for episode in range(n_episodes):
        state = random.randint(0, n_states - 1)  # Start with a random state
        for step in range(max_steps):
            action = agent.act(state, epsilon)
            # Simulate environment response
            new_state = (state + 1) % n_states  # Transition to the next state (for testing purposes)
            reward = 1 if new_state == 0 else 0  # Reward of 1 if reaching state 0, else 0
            agent.learn(state, new_state, gamma, reward, action)
            state = new_state  # Move to the new state
            if state == 0:
                break  # Episode ends if the agent reaches state 0

    # Print the Q-table after training
    print("Q-table after training:")
    print(agent.q_table)


if __name__ == "__main__":
    main()

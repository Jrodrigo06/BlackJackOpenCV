from stable_baselines3 import DQN

model = DQN.load("dqn_blackjack")

print(model.policy)  # Print the policy of the loaded model
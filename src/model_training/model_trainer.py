import gymnasium as gym
import numpy as np
from stable_baselines3 import DQN
from stable_baselines3.common.vec_env import DummyVecEnv
from src.model_training.blackjack_env import BlackjackEnv
from src.logger import logging

# Wrap the environment in a vector environment
env = DummyVecEnv([lambda: BlackjackEnv()])

# Initialize the DQN model
model = DQN("MlpPolicy", env, verbose=1, learning_rate=0.001, 
            batch_size=32, buffer_size=50000, exploration_fraction=0.1)
logging.info("DQN model initialized")

# Train the model
model.learn(total_timesteps=100000)

# Save the trained model
model.save("dqn_blackjack")
logging.info("Model saved as 'dqn_blackjack'")

env.close()
logging.info("Environment closed")

print("Training complete! Model saved as 'dqn_blackjack'.")
import gymnasium as gym
import numpy as np
from stable_baselines3 import DQN, PPO, A2C

env = gym.make("Black Jack-v1")

env.reset()

print("sample action: ", env.action_space.sample())

print("sample observation: ", env.observation_space.sample())
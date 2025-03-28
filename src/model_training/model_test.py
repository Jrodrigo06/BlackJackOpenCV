import gymnasium as gym
import numpy as np
from stable_baselines3 import DQN
from stable_baselines3.common.vec_env import DummyVecEnv
from src.model_training.blackjack_env import BlackjackEnv
from src.logger import logging

def evaluate_model(model_path, num_episodes=1000):
    # Wrap the environment in a vector environment
    # to ensure the baseline models use it as their algorithm expects
    # vectorized environments
    env = DummyVecEnv([lambda: BlackjackEnv()])
    
    # Load the trained model
    model = DQN.load(model_path, env=env)
    
    # Evaluation metrics
    total_rewards = []
    wins = 0
    draws = 0
    losses = 0
    
    # Run evaluation episodes

    logging.info("Starting testing of the model") 
    for _ in range(num_episodes):
        
        # Start a new episode
        obs = env.reset()
        #Makes sure the game runs
        done = False
        # Initialize episode reward
        episode_reward = 0
        
        while not done:
            # Predict action using the model, and with deterministic=True 
            # It doesnt use randomness in the action selection
            action, _ = model.predict(obs, deterministic=True)
            # Collects info on the observation and reward
            # Interestingly enough it seems since info was empty the
            # function was not returning it, so we had to remove the param
            obs, reward, done, _ = env.step(action)
            episode_reward += reward[0]
        
        ## Appends the episodes reward to the list
        total_rewards.append(episode_reward)
        
        # Classify the episode outcome
        if episode_reward == 0:
            draws += 1
        elif episode_reward > 0:
            wins += 1
        elif episode_reward < 0:
            losses += 1
    
    # Calculate metrics
    metrics = {
        'average_reward': np.mean(total_rewards),
        'reward_std': np.std(total_rewards),
        'win_rate': wins / num_episodes,
        'loss_rate': losses / num_episodes,
        'draw_rate': draws / num_episodes
    }
    
    print("Model Evaluation Metrics:")
    for key, value in metrics.items():
        print(f"{key}: {value:.4f}")
    
    env.close()
    return metrics

# Evaluate the saved model
evaluate_model("dqn_blackjack.zip")#
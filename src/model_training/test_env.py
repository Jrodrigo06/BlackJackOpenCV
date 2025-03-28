import gymnasium as gym
from src.model_training.blackjack_env import BlackjackEnv
import numpy as np

def main():
    # Create the environment instance
    env = BlackjackEnv()

    # Reset the environment to get the initial state
    observation = env.reset()
    print("Initial Observation:", observation)
    env.render()

    done = False

    # Game loop: continue until the game is finished
    while not done:
        try:
            # Get the action from the user: 0 = stick, 1 = hit
            action = input("Enter action (0 for stick, 1 for hit): ")
            # Validate the input
            if action not in ["0", "1"]:
                print("Invalid input. Please enter 0 or 1.")
                continue
            action = int(action)
            
            # Take a step in the environment using the chosen action
            observation, reward, done, info = env.step(action)
            print("Observation:", observation)
            print("Reward:", reward)
            print("Done:", done)
            env.render()
            print("-" * 40)
        except Exception as e:
            print("An error occurred:", e)
    
    env.close()

if __name__ == "__main__":
    main()

# OpenCV Implementation coming soon!

# Blackjack Reinforcement Learning Agent

This project is a reinforcement learning-based agent that learns to play Blackjack. The goal of the agent is to maximize its rewards through playing the game, by deciding whether to "hit" (draw a card) or "stick" (stop drawing cards) based on its current hand value and the dealer’s visible card's value.

## Overview

In this project, I used a Deep Q-Network (DQN), a reinforcement learning algorithm, to train an AI agent to play Blackjack. The agent receives feedback based on the outcome of the game, I found winning = 1, losing = -1, and Tie/Push = 0 worked the best, although more testing could be used to determine this.

### Technologies Used:
- **Python**: Programming language used
- **Stable-Baselines3**: Library for reinforcement learning algorithms, where I used DQN
- **Gymnasium**: Framework for creating the Blackjack environment
- **NumPy**: For numerical operations like calculating rewards and creating arrays for return for the Gymnasium methods like step()


## How It Works

1. **Environment**: 
   - The environment is built using the `gymnasium` library, which simulates the Blackjack game.
   - The agent interacts with this environment by taking actions, either hitting or sticking based on its current hand and the visible card of the dealer.
   - Works with Baseline3

2. **Reinforcement Learning**:
   - The agent uses a **Q-learning** approach where it learns a function (called Q-function) that predicts the expected future rewards of taking certain actions in certain states, by initially taking random actions and figuring out on its own what rewards the best

   - It uses the **Deep Q-Network (DQN)** algorithm, which approximates this Q-function using a neural network. The agent adjusts the weights of the neural network based on the reward it receives after each action, through brack propogation. So, a DQN differs from traditional Q-Learning as it uses Neural Networks and to start it creates two neural networks that are randomly intialized, and one is constantly updating during the training and the other one is updated much less frequeuntly to help stablilize the finel model, the target network learns from a random sample of a wide range of expierences not just the most recent ones.

3. **Training Process**:
   - The agent plays many games, and after each game, it gets feedback:
     - **Positive reward** of 1 for winning
     - **Negative reward** of -1 for losing
     - **Zero reward** for a tie (draw)
   - Through many episodes, the agent learns which actions are more likely to lead to better rewards. I trained it on a 100000 steps

4. **Evaluation**:
   - After training, the model is evaluated by running it through many test episodes and calculating the performance metrics, such as the average reward, win rate, and loss rate.
   - **Metrics**:
     - **Average Reward**: -0.0030
     - **Win Rate**: 45.10%
     - **Loss Rate**: 45.40%
     - **Draw Rate**: 9.5%
    
    - So far this shows that the Model played slightly better than the true statistics of black jack


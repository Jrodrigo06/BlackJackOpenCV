#import "@preview/fletcher:0.5.5"

#import "@preview/charged-ieee:0.1.3": ieee


#show: ieee.with(
  title: [Deep Q-Learning in Blackjack: Theory and Implementation],
  abstract: [
    This paper explores the math behind my implementation of a Deep Q-Learning agent for my implementation of Blackjack. It examines the theoretical basis of Q-learning, the mathematical formulation of the Q-learning algorithm, and the neural networks used to approximate Q-values. Additionally, it details the implementation process, training methodology, and performance evaluation against a simple dealer. This paper is a personal deep dive to enhance my understanding of the math for reinforcement learning and Deep Q-Networks (DQN) Not for publication.
  ],
  authors: (
    (
      name: "Jerome Rodrigo",
      organization: [Student at Northeastern University],
      location: [Boston, MA],
      email: "rodrigo.j@northeastern.edu"
    ),
)
)

= Introduction
This project originally started as I believed that BlackJack would be a simple game to implement Reinforcement Learning, as there are not many states and actions to worry about. So I first started this project by implementing my own blackjack game and setting it up where I was the player, with a simple dealer bot as the dealer. The dealer's logic was pretty simple: either keep hitting till you beat the player or till it reaches 17 or greater.

I then started to implement Reinforcement Learning using Open AI's Gymnasium, and Baseline3. I chose to use Deep Q-Networks as the action space is discrete, as the player can only hit or stay. 

= Reinforcement Learning

== What is Q-Learning?
To start Q-Learning is a value based algorithim which means it uses a value function to determine the reward and from there it figures out the optimal policy, which is the best action to take given the state. Q-learning uses state-action value functions where both the state current setup of the game (i.e the dealer has 11 and the player has 10) and the action (hit or stay) are used to determine a number) which is the Q-value, quantifying _How good it is to be in the state s and take an action a given this state?_ The goal of Q learning is to get the best Q-function to maximize the reward, finding the optimal policy. Typically the agent/AI will start with an abritrary Q-function, and an exploration policy, where it'll randomly explore the enviroment. The Q-function is updated using the Bellman equation. \ \
=== Bellman Equation for Q-Learning
$
  V(S#sub[1]) = max_a [sum_s' P(s'|s, = S#sub[1] , a) V(s')]
$

While this function looks complicated, it is quite simple. The left side is the value function and it's a recursive function where it finds the maximum future value over all possible actions. The summation of probablities is there due to stochasticity of the environment. This is due to the fact that the next state is not guarnteed with the action taken, for example in blackjack the next state isn't guranteed with a hit (i.e. you have 10 the next card is not guranteed to be an ace), as the next card pulled is random. The summation accounts for all possible future states, weighted by their probabilities, in order to evaluate the expected value of taking each action.

== Deep Q-Networks (DQN)
So I opted for Deep-Q-Networks due to the stochastic nature of BlackJack, in standard Q-learning I would have to make Q-table/function for every possible state-action pair. The number of possible states is huge due to the nature of blackjack's random drawing, creating a Q-table for blackjack wouldn't be feasibly due to all the possibilites you'd have to account for.
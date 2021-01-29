# Fundamentals_of_Reinforcements_Learning

### What is the K-armed bandit problem?

An agent taking actions and receiving rewards based on the action selected

### How do we define value of an action?

The value of each action is estimated by the expected value of an action: Sample average method

### How do we improve the estimated value of an action?

Incremental update rule, recursively update rule where we store the number of steps each action is taken and the previous estimate

### Exploration vs. Exploitation dilemma

Exploration - improve knowledge for long term benefit

Exploitation - exploit knowledge for short-term benefit

### Clever methods to solve the exploration exploitation dilemma

1. Epsilon-Greedy action selection

Explore epsilon percent of times and exploit 1-epsilon percent of times, takes greedy action 1-epsilon percent of time, and take epsilon/N percent of time for any other action

2. Optimistic Initial Values

If we have insight and set the value for each action larger than the sample average of the action, we will systematically explore the actions. This optimism fades over time

3. Upper Confidence Bound(UCB) Selection

Mixes expoitation and exploration through the use of confidence intervals, it uses the strategy of optimism in the face of uncertainty

### Finite Markov Decision Process

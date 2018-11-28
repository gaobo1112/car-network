import tensorflow as tf
from collections import deque
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from Env.env import Env
import numpy as np
import random


class Agent:
    def __init__(self, env):
        self.state_size = env.state_size
        self.action_size = env.action_size
        self.memory = deque(maxlen=2000)
        self.gamma = 0.95
        self.epsilon = 1.0
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.learning_rate = 0.001
        self.model = self._build_model()

    def _build_model(self):
        model = Sequential()
        model.add(Dense(24,input_dim=self.state_size,activation='relu'))
        model.add(Dense(24,activation='relu'))
        model.add(Dense(self.action_size,activation='linear'))
        model.compile(loss='mse',
                      optimizer=Adam(lr=self.learning_rate))

    def act(self,state):
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        act_values = self.model.predict(state)
        return np.argmax(act_values[0])

    def remember(self,state,action,reward,next_state):
        self.memory.append((state, action, reward, next_state))

    def replay(self,batch_size):
        minibatch = random.sample(self.memory,batch_size)
        for state ,action, reward, next_state in minibatch:
            target = reward + self.gamma\
                     *np.amax(self.model.predict(next_state)[0])
            target_f = self.model.predict(state)
            target_f[0][action] = target
            self.model.fit(state,target, epochs=1, verbose=0)
            if self.epsilon > self.epsilon_min:
                self.epsilon *= self.epsilon_decay

if __name__ == "__main__":
    env = Env()
    agent = Agent(env)
    batch_size = 32
    state = env.reset()
    while True:
        action = agent.act(state)
        next_state ,reward = env.step(action)
        agent.remember(state,action,reward,next_state)
        state = next_state
        if len(agent.memory) > batch_size:
            agent.replay(batch_size)






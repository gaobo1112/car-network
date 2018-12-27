from DQN import DeepQNetwork
from wireless.network import CellularNetwork

def run_maze():
    step = 0
    for episode in range(30000):
        # initial observation
        observation = env.reset()

        while True:
            # fresh env
            env.render()

            # RL choose action based on observation
            action = RL.choose_action(observation)

            # RL take action and get next observation and reward
            observation_, reward, done = env.step(action)

            RL.store_transition(observation, action, reward, observation_)

            # print("step %d = %d ",step,reward)

            if (step > 200) and (step % 5 == 0):
                RL.learn()

            # swap observation
            observation = observation_

            # break while loop when end of this episode
            if done:
                break
            step += 1
        print(episode)
        print(step)


if __name__ == "__main__":
    env = CellularNetwork()
    env.Generator.createBS(500)
    env.Generator.insertURrandomly(3)
    RL = DeepQNetwork(4**3, 12,
                      learning_rate=0.01,
                      reward_decay=0.9,
                      e_greedy=0.98,
                      replace_target_iter=300,
                      memory_size=10000,
                      # output_graph=True
                      )
    run_maze()
    RL.plot_cost()

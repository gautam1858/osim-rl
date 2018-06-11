from osim.env.osim import ProstheticsEnv
import pprint

env = ProstheticsEnv()
env.change_model(model='3D', prosthetic=True, difficulty=2, seed=None)
observation = env.reset()
for i in range(300):
    observation, reward, done, info = env.step(env.action_space.sample(), project = False)
#    print(len(observation))
    pprint.pprint(observation)
    if done:
        env.reset()

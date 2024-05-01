# Note that this script was created by ChatGPT for plotting purposes
import json
import numpy as np
import matplotlib.pyplot as plt
import os 

logfiles_locations = {
    'fish-swim_test-0_eval' : 'tmp/fish/fish-swim-04-25-im84-b128-s411637-pixel/eval.log',
    'fish-swim_test-0_train' : 'tmp/fish/fish-swim-04-25-im84-b128-s411637-pixel/train.log',
    'cartpole-swingup_test-0_eval' : 'tmp/cartpole/cartpole-swingup-04-27-im84-b128-s348228-pixel/eval.log',
    'walker-walk_test-0_eval' : 'tmp/walker/walk/walker-walk-04-29-im84-b128-s673499-pixel/eval.log',
    'swimmer-swimmer6_test-0_eval' : 'tmp/swimmer/swimmer-swimmer6-04-30-im84-b128-s683281-pixel/eval.log',
}

# Path to the log file
log_file_path = logfiles_locations['swimmer-swimmer6_test-0_eval']
results_directory = 'results'

# Function to load data from a log file
def load_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            data.append(json.loads(line))
    return data

# Load and process the data
data = load_data(log_file_path)
steps = np.array([entry['step'] for entry in data])
episode_rewards = np.array([entry['episode_reward'] for entry in data])
mean_episode_rewards = np.array([entry['mean_episode_reward'] for entry in data])

# Plot Episode Reward 
plt.figure(figsize=(10, 5))
plt.plot(steps, episode_rewards, label='Episode Reward', marker='o', color='Blue')
plot_title = 'Eval Episode Reward (CURL swimmer-swimmer6)'
plt.title(plot_title)
plt.xlabel('Step')
plt.ylabel('Reward')
plt.legend()
plt.grid(True)
plt.savefig(os.path.join(results_directory, plot_title))
plt.show()
plt.close()
from urban_heat_env.server.urban_heat_env_environment import UrbanHeatEnvironment

# Initialize environment
env = UrbanHeatEnvironment()

print("[START]")


# Function to find hottest valid cell
def find_hottest(state):
    max_temp = -1
    pos = (0, 0)

    for i in range(len(state["temperature"])):
        for j in range(len(state["temperature"][0])):
            # avoid buildings + pick hottest
            if (
                state["temperature"][i][j] > max_temp
                and state["buildings"][i][j] == 0
            ):
                max_temp = state["temperature"][i][j]
                pos = (i, j)

    return pos


# Run tasks
for task in ["easy", "medium", "hard"]:
    state = env.reset()
    done = False

    while not done:
        # Smart action: pick hottest location
        action = {"location": find_hottest(state)}

        state, reward, done, _ = env.step(action)

        print("[STEP]", reward)

    print("[END]", task)
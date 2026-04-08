import random

class UrbanHeatEnvironment:
    def __init__(self):
        self.size = 5
        self.max_steps = 5
        self.max_trees = 5

    def reset(self):
        self.grid = [[random.randint(30, 40) for _ in range(self.size)] for _ in range(self.size)]
        self.buildings = [[random.choice([0,1]) for _ in range(self.size)] for _ in range(self.size)]
        self.trees = []
        self.steps = 0

        self.initial_avg_temp = self.get_avg_temp()

        return self.state()

    def state(self):
        return {
            "temperature": self.grid,
            "buildings": self.buildings,
            "trees": self.trees
        }

    def step(self, action):
        x, y = action["location"]
        reward = 0
        done = False

        # invalid (building or already tree)
        if self.buildings[x][y] == 1 or (x, y) in self.trees:
            reward -= 0.5
        else:
            if len(self.trees) >= self.max_trees:
                reward -= 0.3
            else:
                self.trees.append((x, y))

                # cooling
                self.grid[x][y] -= 1.5

                # neighbors
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < self.size and 0 <= ny < self.size:
                        self.grid[nx][ny] -= 0.5

        # reward based on improvement
        new_avg = self.get_avg_temp()
        reduction = self.initial_avg_temp - new_avg

        reward += reduction * 0.2

        self.steps += 1

        if self.steps >= self.max_steps:
            done = True

        return self.state(), reward, done, {}

    def get_avg_temp(self):
        temps = [t for row in self.grid for t in row]
        return sum(temps) / len(temps)
from abc import ABC, abstractmethod
import random


class Reward(ABC):
    @abstractmethod
    def rewards(self):
        pass


class GenericReward:
    def __init__(self, name, ratio):
        self.name = name
        self.ratio = ratio


class RewardFactory:
    def __init__(self, rew):
        self.rewards = rew

    def create_reward(self):
        total_ratio = sum([reward.ratio for reward in self.rewards])
        choice = random.uniform(0, total_ratio)
        current = 0
        for reward in self.rewards:
            if current + reward.ratio >= choice:
                return reward
            current += reward.ratio
        return None


rewards = [
    GenericReward("1st place", 10),
    GenericReward("2nd place", 10),
    GenericReward("3rd place", 10),
    GenericReward("4th place", 10),
    GenericReward("5th place", 10),
    GenericReward("Gold", 3),
    GenericReward("Gem", 1)
]

factory = RewardFactory(rewards)

reward_counts = {reward.name: 0 for reward in rewards}
num_rewards = 54

for _ in range(num_rewards):
    reward = factory.create_reward()
    reward_counts[reward.name] += 1

for reward, count in reward_counts.items():
    print(f"{reward}: {count}")

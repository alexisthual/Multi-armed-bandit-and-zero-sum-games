import numpy as np
import random


# %% NFG class
class NormalFormGame:
    def __init__(self, verbose=False, DeterministicReward = True, random = False, nb_actions = 2):
        self.verbose = verbose

        if random:
            self.randomInitializer(nb_actions)
        else:
            self.nActions = [2,2]
            self.matrix = np.array([
                [[-4,4], [1,-1]],
                [[1,-1], [3,-3]]
            ])
        self.DeterministicReward = DeterministicReward

    def randomInitializer(self, nb_actions):
        self.nActions = [nb_actions,nb_actions]
        self.matrix = np.zeros((nb_actions, nb_actions, 2))
        for action1 in range(nb_actions):
            for action2 in range(nb_actions):
                rew = np.random.randint(-4, 4)
                self.matrix[action1, action2, 0] = rew
                self.matrix[action1, action2, 1] = -rew

    def rewards(self, actions):
        '''
        Input: actions as a 2-uplet (a1, a2)
        Output: rewards for each player
        '''
        if self.DeterministicReward:
            rewards = self.matrix[actions]
        else:
            rewards = np.random.normal(loc=self.matrix[actions], scale = [0.5,0.5])
        return rewards

    def bestReward(self, playerIndex, opponentAction):
        # If column-player:
        if playerIndex == 0:
            return np.max(self.matrix[opponentAction, :, playerIndex])
        else:
            return np.max(self.matrix[:, opponentAction, playerIndex])


class ExtensiveFormGame:
    ## The markets for lemon
    def __init__(self, verbose=False, DeterministicReward = True, random = False, nb_info = 2, nb_actions = 2):
        self.verbose = verbose

        if random:
            self.randomInitializer(nb_info, nb_actions)
        else:
            self.nActions = [2,2]
            self.nInfo = 2
            self.matrix = np.array([[ #Bad Car
                [[-1,1], [0,0]],        #Low price, Buy or not
                [[2,-2], [1,-1]]        #High price, Buy or not
            ],[                       #Good Car
                [[-2,2], [-1,1]],       #Low price, Buy or not
                [[1,-1], [0,0]]         #High price, Buy or not
            ]])
            self.info = np.random.randint(0, 1)
        self.DeterministicReward = DeterministicReward


    def randomInitializer(self, nb_information, nb_actions):
        self.nActions = [nb_actions,nb_actions]
        self.nInfo = nb_information
        self.matrix = np.zeros((nb_information, nb_actions, nb_actions, 2))
        print(nb_information)

        for info in range(nb_information):
            for action1 in range(nb_actions):
                for action2 in range(nb_actions):
                    rew = np.random.randint(-4, 4)
                    self.matrix[info, action1, action2, 0] = rew
                    self.matrix[info, action1, action2, 1] = -rew
        self.info = random.randint(0, self.nInfo-1)


    def rewards(self, actions):
        '''
        Input: actions as a 2-uplet (actionSeller, actionBuyer)
        Output: rewards for each player
        '''
        if self.DeterministicReward:
            rewards = self.matrix[self.info, actions[0], actions[1]]
        else:
            rewards = np.random.normal(loc=self.matrix[self.info, actions[0], actions[1]], scale = [0.5,0.5])
        return rewards

    def newDeal(self):
        self.info = random.randint(0, self.nInfo-1)
        return self.info

    def bestReward(self, playerIndex, opponentAction):
        if playerIndex == 0:
            return np.max(self.matrix[self.info, :, opponentAction, playerIndex])
        else:
            return np.max(self.matrix[self.info, opponentAction, :, playerIndex])



if __name__ == "__main__":
    a = ExtensiveFormGame(DeterministicReward = False)
    print(a.rewards((0,1)))

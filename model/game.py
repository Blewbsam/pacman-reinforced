import sys
import os
import numpy
import matplotlib.pyplot as plt
import torch
from utils import *
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'build')) # relative path to build folder used for import
import pacman

DIRECTIONS = ["Up","Down","Left", "Right"]

class Game:
    def __init__(self):
        self.gs = pacman.GameState()
        self.display = pacman.Display(self.gs)
        self._step_count = 0
    def update(self):
        self.display.update()
        self.display.render()
    def get_state(self):    
        if self.gs.game_over():
            return None
        image = transform_image_with_thresholding(self.display.get_screenshot())
        image = image.transpose(2,0,1)
        return torch.from_numpy(image).float()
    def get_score(self):
        return self.gs.get_score()
    def running(self):
        return not self.gs.game_over()
    def decision_available(self):
        return self.display.pacman_contained()
    def step(self,action):
        # makes action in environment
        assert action >= 0 and action <= 3
        self._step_count += 1
        cur_state = self.get_state()
        self.display.step(action)
        self.update()
    def get_step_count(self):
        return self._step_count
    def is_game_lost(self):
        # to be called only when game is over.
        assert self.gs.game_over()
        return self.gs.is_game_lost()



if __name__ == "__main__":
    game = Game()
    while game.running():
        game.update()   

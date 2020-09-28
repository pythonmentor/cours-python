
from maze import Maze
from position import Position
import settings as constants

class MacGyver:
    """ """
    def __init__(self, maze):
        """ Initialize position and bag. """
        self.maze = maze
        self.paths = maze.paths
        self.mg_pos = self.maze.start_pos
        self.item1_pos = self.maze.item1_pos
        self.item2_pos = self.maze.item2_pos
        self.item3_pos = self.maze.item3_pos
        self.bag = []
        self.mac_goal = False

    def move(self, direction):
        """ """
        if direction == 'UP':
            if Position.up(self.mg_pos) in self.paths:
                self.mg_pos = Position.up(self.mg_pos)
                special_cell = self.maze.is_special_cell(self.mg_pos)
                if special_cell != False:
                    self.what_special(special_cell)
                return True
        if direction == 'DOWN':
            if Position.down(self.mg_pos) in self.paths:
                self.mg_pos = Position.down(self.mg_pos)
                special_cell = self.maze.is_special_cell(self.mg_pos)
                if special_cell != False:
                    self.what_special(special_cell)
                return True
        if direction == 'RIGHT':
            if Position.right(self.mg_pos) in self.paths:
                self.mg_pos = Position.right(self.mg_pos)
                special_cell = self.maze.is_special_cell(self.mg_pos)
                if special_cell != False:
                    self.what_special(special_cell)
                return True
        if direction == 'LEFT':
            if Position.left(self.mg_pos) in self.paths:
                self.mg_pos = Position.left(self.mg_pos)
                special_cell = self.maze.is_special_cell(self.mg_pos)
                if special_cell != False:
                    self.what_special(special_cell)
                return True

    def what_special(self, special_cell):
        """ """
        if special_cell == 'item1':
            self.pouch_bag(special_cell)
        elif special_cell == 'item2':
            self.pouch_bag(special_cell)
        elif special_cell == 'item3':
            self.pouch_bag(special_cell)
        elif special_cell == 'goal':
            self.mac_goal = True
            print(special_cell)
            print(self.mac_goal)
        
    def pouch_bag(self, item):
        """ """
        self.bag.append(item)
        print(len(self.bag), self.bag)


if __name__ == '__main__':
    
    instance_maze = Maze(constants.FILENAME) 
    instance_macgyver = MacGyver(instance_maze)

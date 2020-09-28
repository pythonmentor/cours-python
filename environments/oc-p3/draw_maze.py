import pygame

from maze import Maze
from position import Position
from macgyver import MacGyver

import settings as constants

class MazeScreen:
    """ """
    def __init__(self, paths, walls, start, goal, item1, item2, item3):
        # pygame.init()
        self.window = pygame.display.set_mode((660, 660))
        self.paths = paths
        self.walls = walls
        self.start = start
        self.goal = goal
        self.item1 = item1
        self.item2 = item2
        self.item3 = item3

        self.screen_paths()
        self.screen_walls()
        self.screen_start()
        self.screen_goal()
        self.screen_item1()
        self.screen_item2()
        self.screen_item3()
        # self.display_mac()
        # self.move_mac(self.position_perso)

        # self.draw_maze()

    # def draw_maze(self):
    #     """ """
    #     while True:
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 sys.exit()

    def screen_paths(self):
        """ """
        a_paths = list(self.paths)
        self.image = pygame.image.load('images/floor.bmp').convert()
        i = 0
        for path in a_paths:
            pos = list(a_paths)[i]
            pos_x = pos.y * 44
            pos_y = pos.x * 44
            self.window.blit(self.image, (pos_x, pos_y))
            i = i + 1

        pygame.display.flip()

    def screen_walls(self):
        """ """
        self.a_walls = list(self.walls)
        self.image = pygame.image.load('images/wall.bmp').convert()
        i = 0
        for wall in self.a_walls:
            # pos = list(self.a_walls[i])
            pos = list(self.a_walls)[i]
            pos_x = pos.y * 44
            pos_y = pos.x * 44
            self.window.blit(self.image, (pos_x, pos_y))
            i = i + 1

        pygame.display.flip()

    def screen_start(self):
        """ Put MacGyver on the start position. """
        self.img_mg = pygame.image.load('images/MacGyver.png').convert()
        a_start = list(self.start)[0]
        pos_x = a_start.y * 44
        pos_y = a_start.x * 44
        self.window.blit(self.img_mg, (pos_x, pos_y))

        pygame.display.flip()

    def screen_goal(self):
        """ Put the Guard on the goal position. """
        a_goal = list(self.goal)[0]
        self.image = pygame.image.load('images/Gardien.png').convert()
        pos_x = a_goal.y * 44
        pos_y = a_goal.x * 44
        self.window.blit(self.image, (pos_x, pos_y))

        pygame.display.flip()

    def screen_item1(self):
        a_items = list(self.item1)
        self.image = pygame.image.load('images/ether.png').convert()
        i = 0
        for item in a_items:
            pos = list(a_items)[i]
            pos_x = pos.y * 44
            pos_y = pos.x * 44
            self.window.blit(self.image, (pos_x, pos_y))
            i = i + 1
        pygame.display.flip()

    def screen_item2(self):
        a_items = list(self.item2)
        self.image = pygame.image.load('images/seringue.png').convert()
        i = 0
        for item in a_items:
            pos = list(a_items)[i]
            pos_x = pos.y * 44
            pos_y = pos.x * 44
            self.window.blit(self.image, (pos_x, pos_y))
            i = i + 1
        pygame.display.flip()

    def screen_item3(self):
        a_items = list(self.item3)
        self.image = pygame.image.load('images/tube_plastique.png').convert()
        i = 0
        for item in a_items:
            pos = list(a_items)[i]
            pos_x = pos.y * 44
            pos_y = pos.x * 44
            self.window.blit(self.image, (pos_x, pos_y))
            i = i + 1
        pygame.display.flip()

    # def display_mac(self):
    #     """ Display MacGyver on the maze. """
    #     self.img_mg = pygame.image.load('images/MacGyver.png').convert()
    #     position_mac = list(self.start)[0]
    #     pos_x = position_mac.y * 44
    #     pos_y = position_mac.x * 44
    #     self.position_perso = pygame.Rect((pos_x, pos_y, 28, 38))
    #     self.window.blit(self.img_mg, self.position_perso)
    #     pygame.display.flip()

    # def move_mac(self, position_perso):
    #     self.position_perso = position_perso.move(0,44)
    #     self.window.blit(self.img_mg, self.position_perso)
    #     pygame.display.flip()        


# if __name__ == '__main__':
    
#     m = Maze(constants.FILENAME)  
#     ms = MazeScreen(m.paths, m.walls, m.start, m.goal, m.items)


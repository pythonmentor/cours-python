import settings as constants
from position import Position

class Maze:

    def __init__(self, filename):
        """ initialize the maze. """
        self.filename = filename
        self.paths = set()
        self.walls = set()
        self.start = set()
        self.goal = set()
        self.items = set()

        self.organize_the_maze()
        self.put_items()

    def is_valid_cell(self, position):
        """ Return if the cell is valid or not. """     
        return position in self.paths

    def organize_the_maze(self):
        """ Organize the cells of the maze. """
        with open(self.filename) as infile:
            for x, line in enumerate(infile):
                for y, col in enumerate(line):
                    if col == constants.PATH_CHAR:
                        self.paths.add(Position(x, y))
                    elif col == constants.START_CHAR:
                        self.start.add(Position(x, y))
                        self.paths.add(Position(x, y))
                    elif col == constants.GOAL_CHAR:
                        self.goal.add(Position(x, y))
                        self.paths.add(Position(x, y))
                    elif col == constants.WALL_CHAR:
                        self.walls.add(Position(x, y))

    def put_items(self):
        """ put the items in the maze. """
        for item in constants.ITEMS:
            self.items.add(item)

#######################
# Tests & validations #
#######################

def main():
    maze = Maze(constants.FILENAME)

    # test de l'état de cellules
    p1 = Position(-1,0)
    print(maze.is_valid_cell(p1))

    p2 = Position(0, 0).right()
    print(maze.is_valid_cell(p2))

    p3 = Position(5, 5).right()
    print(maze.is_valid_cell(p3))

    # je verifie que j'ai toutes les cases ainsi que leurs coordonnées  
    print(f'Total des cases : {len(maze.paths) + len(maze.walls)}')
    
    print(f'la liste des positions des {len(maze.paths)} chemins  : {maze.paths}')
    print(f'la liste des positions des {len(maze.walls)} murs : {maze.walls}')

    print(f'The start is in this positions : {maze.start}')
    print(f'The goal is in this positions : {maze.goal}') 
    print(f'The items are in this positions : {maze.items}')



if __name__ == "__main__":
    main()



###########################

#    def open_file(self):
#         current_map = []
        
#         map_file = open(self.filename,'r')
#         for line in map_file:
#             current_map.append(line.strip())
#         map_file.close()

#         print('Map : ',current_map)

# ma_map = Maze('map-1.txt')

# print(ma_map.open_file())

    # def find_cell_attribute(self, x, y):
    #     return current_map[x-1][y-1]
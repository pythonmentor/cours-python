
# create the map

current_map = []

map_file = open('map-1.txt','r')

for line in map_file:
    current_map.append(line.strip())

map_file.close()

map_max_x = len(current_map[0])
map_max_y = len(current_map)

# what I have from the File
print('Map : ',current_map)

# print the maze
for x in range(map_max_x):
    print(current_map[x])

# # print each coord of the maze
# for x in range(map_max_x):
#     for y in range(map_max_y): 
#         print(f'case x={x+1},y={y+1}', current_map[x][y])

# # search a coordinate x,y
# def find_cell_attribute(x,y):
#     return current_map[x-1][y-1]

# print(f'what is the cell :', find_cell_attribute(14,8))

# # cell attribute rules
# cell_value = ''



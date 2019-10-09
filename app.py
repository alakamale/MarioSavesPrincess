###########################           PRESTACAP         ###########################
# First task (Mario saving the princess)
#  Mario and the princess are trapped in a square grid (N*N), Mario needs to reach the princess with minimum number of steps (shortest paths),
#  while avoiding any obstacles. Mario can move UP, DOWN, LEFT and RIGHT and can’t go outside of the grid. Create a function or a class that
#  given a square grid (N*N), the location of Mario and the princess will return a list of the shortest paths possible from Mario to the princess.
#     Mario denoted by (m)
#     Princess denoted by (p)
#     Obstacle denoted by (x)
#     Free cell denoted by (-)
###########################           PRESTACAP         ###########################

from graph import Graph

def find_shortest_path(N, grid):
  validate_grid(N, grid)

  # Create graph with cells at each index
  graph = Graph(N)
  for i, row in enumerate(grid):
    for j, value in enumerate(row):
      graph.insert(i, j, value.lower())

  # Get the mario cell
  mc = graph.get_mario()

  # list all possible paths and sort to valid shortest paths
  pp = bfs(mc, graph)
  shortest_list_length = len(min(pp, key=len))
  shortest_paths = [p for p in pp if len(p) == shortest_list_length]
  return shortest_paths


def bfs(mc, graph):
  queue = [[mc]]
  possible_paths = []

  while queue:
    # Gets the first path in the queue
    path = queue.pop(0)

    # Gets the last node in the path
    node = path[-1]

    # Checks if we got to the end
    if node.value == 'p':
      possible_paths.append(trace_path(path))
    # Add neighbor nodes that aren't in the path to the list and append paths to the queue
    for current_neighbour in graph.get_neighbors(node):
      new_path = list(path)
      if current_neighbour not in new_path:
        new_path.append(current_neighbour)
        queue.append(new_path)
  return possible_paths


def trace_path(path):
  # return back tuple of the word path
  word_path = []
  for index in range(len(path) - 1):
    word_path.append(check_direction(path[index], path[index + 1]))
  return tuple(word_path)


def check_direction(cell_one, cell_two):
  # Convert the directions to required format
  if cell_one.c < cell_two.c:
    return "RIGHT"
  elif cell_one.c > cell_two.c:
    return "LEFT"
  elif cell_one.r < cell_two.r:
    return "DOWN"
  else:
    return "UP"


def validate_grid(N, grid):
  # Check if the grid size is valid?, Is princess and mario included?
  print(grid)
  print(len(grid))
  if len(grid) <= 1 or N <= 1:
    raise Exception("Grid not sufficiently large")
  if N != len(grid):
    raise Exception("Grid size does not match the length provided N")

  mario_check(grid)
  princess_check(grid)


def princess_check(grid):
  # Check if princess left mario ;-)
  PRINCESS_FLAG = False
  for row in grid:
    if 'p' or 'P' in list(row):
      PRINCESS_FLAG = True
  if not PRINCESS_FLAG:
    raise Exception("Princess not found in grid")


def mario_check(grid):
  # Check if mario no more intrested finding princess
  MARIO_FLAG = False
  for row in grid:
    if 'm' or 'M' in list(row):
      MARIO_FLAG = True
  if not MARIO_FLAG:
    raise Exception("Mario not found in grid")
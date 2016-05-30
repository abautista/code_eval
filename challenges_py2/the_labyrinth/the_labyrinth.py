import sys


def get_successors(grid, position):
    succesors = []
    x = position[0]
    y = position[1]

    if x > 0 and grid[x-1][y] != "*":
        succesors.append((x-1, y))
    if grid[x+1][y]  != "*":
        succesors.append((x+1, y))
    if y > 0 and grid[x][y-1] != "*":
        succesors.append((x, y-1))
    if grid[x][y+1] != "*":
        succesors.append((x, y+1))
    return succesors


def read_grid(f):
    grid = []
    with open(f, "r") as text:
        row = []
        for line in text:
            grid.append(line.strip())
    return grid


if __name__ == "__main__":
    g = read_grid(sys.argv[1])
    start_position = (0, len(g[0])/2)
    visited = {start_position}
    frontier = [[start_position]]

    while len(frontier) > 0:
        path = frontier.pop()
        current_position = path[-1]

        if current_position[0] == (len(g) - 1):
            break

        for position in get_successors(g, current_position):
            if position not in visited:
                frontier.insert(0, path + [position])
                visited.add(position)

    for position in path:
        line = list(g[position[0]])
        line[position[1]] = "+"
        g[position[0]] = "".join(line)

    for line in g:
        print line

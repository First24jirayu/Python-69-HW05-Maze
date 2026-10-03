def maze_solver_with_conveyors(maze: list[list[str]]) -> dict:
    from heapq import heappush, heappop

    R, C = len(maze), len(maze[0])
    D = {'>': (0,1), '<': (0,-1), '^': (-1,0), 'v': (1,0)}
    S = E = None

    for r in range(R):
        for c in range(C):
            if maze[r][c] == 'S': S = (r,c)
            if maze[r][c] == 'E': E = (r,c)

    if E is None: E = S

    q = [(0, S)]
    dist = {S: 0}
    prev = {S: None}

    while q:
        d, (r,c) = heappop(q)
        if d != dist[(r,c)]: continue

        if maze[r][c] in D:
            ds = [D[maze[r][c]]]
        else:
            ds = [(-1,0),(1,0),(0,-1),(0,1)]

        for dr,dc in ds:
            nr,nc = r+dr,c+dc
            if 0 <= nr < R and 0 <= nc < C and maze[nr][nc] != '#':
                nd = d + (0 if maze[r][c] in D else 1)
                if (nr,nc) not in dist or nd < dist[(nr,nc)]:
                    dist[nr,nc] = nd
                    prev[nr,nc] = (r,c)
                    heappush(q,(nd,(nr,nc)))

    if E not in dist:
        return {"distance": -1, "path": []}

    path = []
    while E is not None:
        path.append([E[0], E[1]])
        E = prev[E]

    return {"distance": dist[path[0][0], path[0][1]], "path": path[::-1]}
if __name__ == "__main__":
    maze = [
        ['S', '.', '>', '>', 'E'],
        ['#', '#', '#', '#', '#']
    ]
    result = maze_solver_with_conveyors(maze)
    print(result)
    #Output: {'distance': 2, 'path': [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]]}

    maze = [
        ['S', '.', '>', '#', 'E'],
        ['#', '#', '#', '#', '#']
    ]
    result = maze_solver_with_conveyors(maze)
    print(result)
    #Output: {"distance": -1, "path": []}


    maze = [
        ['S', '.', 'v', '.', 'E'],
        ['#', '#', 'v', '.', '#'],
        ['.', '.', 'v', '.', '.'],
        ['#', '#', '.', '.', '#'],
        ['.', '.', '.', '.', '.']
    ]
    result = maze_solver_with_conveyors(maze)
    print(result)
    #Output: {'distance': 7, 'path': [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2], [3, 2], [3, 3], [2, 3], [1, 3], [0, 3], [0, 4]]}

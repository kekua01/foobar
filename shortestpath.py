#takes an input that is a matrix
#1's are walls, 0's are open. 
#calculates the shortest path from top left to bottom right, with the feature of being able to knock down one wall

def solution(map):

	moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
	def routes(x_start, y_start, maze):
		w = len(maze[0])
		h = len(maze)
		board = [[None for i in range(w)] for i in range(h)]
		board[x_start][y_start] = 1

		checkem = [(x_start, y_start)]
		while checkem:
			x, y = checkem.pop(0)
			for j, k in moves:
				nx, ny = x + j, y + k
				if nx in range(h) and ny in range(w):
					if board[nx][ny] is None:
						board[nx][ny] = board[x][y] + 1
						if maze[nx][ny] == 1:
							continue
						checkem.append((nx, ny))
		return board
	w = len(map[0])
	h = len(map)
	path_init = routes(0, 0, map)
	path_reverse = routes(h-1, w-1, map)
	length = (w * h) + 1
	for i in range(h):
		for j in range(w):
			if path_init[i][j] and path_reverse[i][j]:
				length = min(path_init[i][j] + path_reverse[i][j] - 1, length)
	return length

print(solution([[0,0,1,0], [1,0,1,1], [0,0,1,0], [0,1,0,0]]))

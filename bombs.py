#you start with two bombs of different kinds, so (1, 1) and can increase your number of bombs by adding one number to the other in each 'step'
#so after one step you can have (2, 1) bombs or (1, 2) bombs, and so on
#this calculates the number of steps needed to achieve some combo of bombs (x, y)


def solution(x, y):
	nx, ny = long(x), long(y)
	counter = 0
	while True:
		if nx <= 0 or ny <= 0:
			return "impossible"
		if ny == 1: 
			return str(counter + nx - 1)
		else:
			counter += (nx // ny)
			nx, ny = ny, nx % ny

	return str(counter)

print(solution("4", "7"))
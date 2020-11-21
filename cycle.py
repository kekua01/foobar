def solution(n, b):
	k = len(n)
	s = n
	seen = {}
	counter = 0
	def from_base_10(x, base):
			num = int(x)
			new_num = []
			if num != 0:
				while num:
					new_num.append(int(num % base))
					num /= base
			while len(new_num) != k:
				new_num.append(0)

			return ''.join(map(str, new_num[::-1]))

	seen[s] = counter
	counter += 1
	while True:
		y = ''.join(sorted(s))
		x = y[::-1]
		for i in x:
			if int(i) >= b:
				return "Error"
		z = int(x, b) - int(y, b)
		new_id = from_base_10(z, b)
		print(new_id)
		if new_id in seen:
			return counter - seen[new_id]
		else:
			seen[new_id] = counter
			counter += 1
			s = new_id

print(solution('21222', 3))

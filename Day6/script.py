from math import prod

file = open("input")
lines = file.read().splitlines()

rows = []
for line in lines:
	rows.append([val for val in line.split(' ') if val != ""])
	
def part_one():
	total = 0
	for i in range(len(rows[0])):
		op = rows[-1][i]
		if op == "+":
			total += sum([int(row[i]) for row in rows[:-1]])
		else:
			total += prod([int(row[i]) for row in rows[:-1]])
	return total

def get_problems():
	opline = lines[-1]
	colwidths = []
	currentcolwidth = 0
	currentop = ''
	i = 0
	for c in opline:
		if c != ' ':
			if currentcolwidth > 0:
				opi = i - currentcolwidth
				colwidths.append((currentop, currentcolwidth-1, opi))
			currentop = c
			currentcolwidth = 0
		currentcolwidth += 1
		i += 1
	opi = i - currentcolwidth
	colwidths.append((currentop, currentcolwidth, opi))
	return colwidths
	
def solve_problem(problem):
	print("solving: " + str(problem))
	op = problem[0]
	cols = problem[1]
	opi = problem[2]
	nums = []
	for col in range(cols):
		digits = ""
		for row in range(len(lines)-1):
			digits += lines[row][opi+col]
		digitstring = ''.join([digit for digit in digits if digit != ' '])
		print(digitstring)
		num = int(digitstring)
		nums.append(num)
	if op == '+':
		return sum(nums)
	else:
		return prod(nums)
		
			
def part_two():
	total = 0
	problems = get_problems()
	for problem in problems:
		solution = solve_problem(problem)
		total += solution
	return total
		
print(part_one())
print(part_two())
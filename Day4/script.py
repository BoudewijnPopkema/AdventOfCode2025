file = open("input")
lines = file.read().splitlines()

size = len(lines)

matrix = [[lines[y][x] for x in range(size)] for y in range(size)]

def position_has_roll(x,y):
	if x > size-1 or y > size-1 or x < 0 or y < 0:
		return False
	else:
		return matrix[y][x] == '@'

def less_than_four_around(x,y):
	relative_positions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
	around = 0
	for rel_pos in relative_positions:
		relx = x + rel_pos[0]
		rely = y + rel_pos[1]
		if position_has_roll(relx,rely):
			around += 1
			if around > 3:
				return False
	return True
	
def part_one():
	removeable_rollpositions = []
	for x in range(size):
		for y in range(size):
			if position_has_roll(x,y) and less_than_four_around(x,y):
				removeable_rollpositions.append((x,y))
	return removeable_rollpositions
	
def part_two():
	total = 0
	while True:
		removeable_rollpositions = part_one()
		rrlen = len(removeable_rollpositions)
		total += rrlen
		if rrlen == 0:
			return total
		for pos in removeable_rollpositions:
			matrix[pos[1]][pos[0]] = '.'
		
print(len(part_one()))
print(part_two())

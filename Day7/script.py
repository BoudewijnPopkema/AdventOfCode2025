file = open("input")
lines = file.read().splitlines()

def part_one():
	splitcount = 0
	startindex = lines[0].find('S')
	beamindexes = {startindex}
	nextindexes = set()
	for line in lines[:-1]:
		for index in beamindexes:
			if line[index] == '^':
				splitcount += 1
				nextindexes.add(index + 1)
				nextindexes.add(index - 1)
			else:
				nextindexes.add(index)
		beamindexes = nextindexes
		nextindexes = set()
	return splitcount
	
def part_two():
	startindex = lines[0].find('S')
	beamindexes = {startindex: 1}
	nextindexes = {}
	for line in lines[:-1]:
		for index in beamindexes.items():
			if line[index[0]] == '^':
				nextindexes[index[0] + 1] = index[1] + nextindexes.get(index[0] + 1, 0)
				nextindexes[index[0] - 1] = index[1] + nextindexes.get(index[0] - 1, 0)
			else:
				nextindexes[index[0]] = index[1] + nextindexes.get(index[0], 0)
		beamindexes = nextindexes
		nextindexes = {}
	return sum(beamindexes.values())

print(part_one())
print(part_two())
file = open("input")
inputlines = file.read().splitlines()
breakindex = inputlines.index("")

ranges = [[int(line.split('-')[0]),int(line.split('-')[1])] for line in inputlines[:breakindex]]
ids = [int(id) for id in inputlines[breakindex+1:]]

print(ranges)
print(ids)

def id_in_ranges(id):
	for range in ranges:
		if id >= range[0] and id <= range[1]:
			return True
	return False

def part_one():
	total = 0
	for id in ids:
		if id_in_ranges(id):
			total += 1
	return total
	
def merge_ranges(ranges):
	sorted_ranges = sorted(ranges, key=lambda range: range[0])
	index = 0
	while index < len(sorted_ranges)-1:
		range = sorted_ranges[index]
		next_range = sorted_ranges[index+1]
		print("checking " + str(range) + " against" + str(next_range))
		if next_range[0] > range[1]:
			print(str(next_range) + " starts after " + str(range))
			index += 1
		else:
			if next_range[1] <= range[1]:
				print(str(next_range) + " falls within " + str(range))
				sorted_ranges.remove(next_range)
				continue
			else:
				print(str(next_range) + " ends after " + str(range))
				range[1] = next_range[1]
			sorted_ranges.remove(next_range)
		continue
	return sorted_ranges
	
def part_two():
	total = 0
	merged_ranges = merge_ranges(ranges)
	for range in merged_ranges:
		amount = range[1] - range[0] + 1
		total += range[1] - range[0] + 1
	return total
	
print(part_one())
print(part_two())
file = open("input")
banks = file.read().splitlines()
banksize = len(banks[0])

def partone(): # For each character just loop through the ones after it to go through all combinations. not a very pretty solution in hindsight, shouldve just picked the biggest ones from a sorted list
	totaljoltage = 0
	for bank in banks:
		bankjoltage = 0
		for bat1pos in range(banksize-1):
			for bat2pos in range(bat1pos+1, banksize):
				joltage = int(bank[bat1pos] + bank[bat2pos])
				if joltage > bankjoltage:
					bankjoltage = joltage
		totaljoltage += bankjoltage
	return totaljoltage
	
def parttwo():
	totaljoltage = 0
	for bank in banks:
		joltagestr = ""
		bankints = [int(x) for x in bank]
		while len(joltagestr) < 11:
			protectlastamount = max(0, 11 - len(joltagestr)) 					# Some of the later characters can't be picked, or we won't have enough chars to get to 12
			maxint = sorted(bankints[:-protectlastamount], reverse=True)[0] 	# Find the largest pickable number
			joltagestr += str(maxint) 											# Add it to the joltage
			indexmax = bankints.index(maxint)									# Find the first occurance of the largest pickable number
			bankints = bankints[indexmax+1:]									# Remove it and the numbers in front of it and go to the next number
		joltagestr += str(sorted(bankints, reverse=True)[0])					# For the last character, all remaining are pickable since it don't matter anymore. 
		totaljoltage += int(joltagestr)											# Feels like that can be solved more cleanly though but i'm not sure
	return totaljoltage

print(partone()) 
print(parttwo())
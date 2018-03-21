# https://www.geeksforgeeks.org/check-if-an-array-can-be-divided-into-pairs-whose-sum-is-divisible-by-k/

def check_pairs(arr,k):
	remainders = {}
	if len(arr) % 2 != 0:
		return False
	else:
		for a in arr:
			remainder = a % k
			if remainder in remainders.keys():
				remainders[remainder] += 1
			else:
				remainders[remainder] = 1
		for a in arr:
			curr_remain = a % k
			if curr_remain == k // 2:
				if remainders[curr_remain] % 2 != 0:
					return False
			elif curr_remain == 0:
				if remainders[0] % 2 != 0:
					return False
			else:
				curr_no_of_occurances = remainders[curr_remain]
				temp_diff = k - curr_remain
				if temp_diff in remainders:
					if curr_no_of_occurances != remainders[temp_diff]:
						return False
				else:
					return False
		return True

arr = [91, 74, 66, 48]
k = 10
if check_pairs(arr,k):
	print ("true")
else:
	print ("false")
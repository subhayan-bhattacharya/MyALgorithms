# using recurison to generate all the binary numbers for a fixed number of digits

def generate_bin_strs(n):
    if n == 0:
        return []
    elif n == 1:
        return ["1","0"]
    else:
        return [digit + bitstring for digit in generate_bin_strs(1) for bitstring in generate_bin_strs(n-1)]
        
n  int(input())
check = generate_bin_strs(2)
for c in check:
    print(c)
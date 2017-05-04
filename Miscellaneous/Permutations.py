#Used to find permutations of a given string

def permute(arr):
    final = set()
    if len(arr) <= 1:
        return arr
    else:
        perms = permute(arr[1:])
        base = arr[0]
        for perm in perms:
            for i in range(len(perm)+1):
                concat = perm[:i] + base + perm[i:]
                final.add(''.join(concat))
    return final
            

str = "aabc"
final = permute(list(str))
print (final)
            
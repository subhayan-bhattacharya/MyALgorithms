testcases = int(input())

for i in range(testcases):
    grid = []
    lines = int(input())
    for i in range(lines):
        characters = input()
        grid.append(sorted(characters))
    start = 0
    possible = 0
    for i in range(len(grid)):
        for j in range(len(grid) - 1):
            if grid[j][i] > grid[j+1][i]:
                possible = 1
    if possible == 0:
        print ("YES")
    else:
        print ("NO")
            
            
    

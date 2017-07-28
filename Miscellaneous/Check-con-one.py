#Convert a decimal to binary and check for consequetive one's


number = int(input())
check = "{0:b}".format(number)
prev = 0
con = 0
max = 1
for c in check:
    if c == '1' and prev == 1:
        con = con + 1
    elif c == '1' and prev == 0:
        prev = 1
        con = con + 1
    elif c == '0':
        prev = 0
        if con > max:
            max = con
        con = 0
        
if con > max:
    print (con)
else:
    print (max)
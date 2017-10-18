def find_triplets(limit):
    #counter = 0
    for x in range(1,limit):
        y = x +1
        z = y + 1
        while z <= limit:
            while z * z < y * y + x * x:
                z = z + 1
            if z * z == y * y + x * x and z <= limit:
                #counter = counter + 1
                #print (x,y,z)
                if x + y + z == 1000:
                    print (x,y,z)
            y = y + 1
    #return counter
            
    
find_triplets(1000)
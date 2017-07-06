def fibI():
    print ("Entering the generator function")
    global a,b
    while True:
        print ("Inside the True loop")
        a,b = b, a+b
        yield a
		
a,b = 0,1	
f=fibI()
print (f)
for i in range(5):
    print (next(f))

#Just a small try to generate fibonacci series using Python and recursion #
def genfibonacci(no):
    if no <= 1:
        return no
    else:
        return genfibonacci(no - 1) + genfibonacci(no - 2)
  	
number = int(input("Enter the number of terms wanted:"))

for n in range(number):
    #print ("For number:",n)
    print (genfibonacci(n))




    
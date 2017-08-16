# Given an array A[] and a number x, check for pair in A[] with sum as x
# http://www.geeksforgeeks.org/write-a-c-program-that-given-a-set-a-of-n-numbers-and-another-number-x-determines-whether-or-not-there-exist-two-elements-in-s-whose-sum-is-exactly-x/

def hasArrayTwoCandidates(arr,number):
    sorted_arr = sorted(arr)
    first = 0
    second = len(arr) - 1
    
    while (first < second):
        sum = sorted_arr[first] + sorted_arr[second]
        if sum < number:
            first += 1
        elif sum > number:
            second -= 1
        else:
            return (sorted_arr[first],sorted_arr[second])
        
    

arr = list(map(int,input().split(' ')))
number = int(input())
first,second = hasArrayTwoCandidates(arr,number)
if first == None and second == None:
    print ("There is no such element")
else:
    print ("The first element is {} and the second parameter {}".format(first,second))
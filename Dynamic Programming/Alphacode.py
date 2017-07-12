#http://www.spoj.com/problems/ACODE/
#Explanation of the problem : https://www.youtube.com/watch?v=Y3y64ge9ioU

def calc_acode(inputstr):
    error = 0
    
    #Section for the first two digits
    dp = [0] * len(inputstr)
    dp[0] = 1
    first = int(inputstr[0])
    second = int(inputstr[1])
    
    if first < 3:
        if first == 1:
            if second == 0:
                dp[1] = 1
            else:
                dp[1] = 2
        elif first == 2:
            if second > 0 and second <= 6:
                dp[1] = 2
            else:
                dp[1] = 1
    else:
        if second == 0:
            error = 1
        else:
            dp[1] = 1
        
    if error == 0:
        #Section for the digits from position 2 till end
        for i in range(2,len(inputstr)):
            prevdigit = int(inputstr[i-1])
            curdigit = int(inputstr[i])
            #The maximum code for any letter would be 26, so if the previous digit is 3 then we cannot have letter starting with 3
            if (prevdigit >= 3) or (prevdigit == 0):
                if curdigit == 0:
                    error = 1
                    break
                else:
                    dp[i] = dp[i-1]
            else:
                #Imagine the case of example code 210 , here 1 cannot combine with 2 since that would make the 0 invalid, 
                #hence it would be 2 and 10 as letters
                if curdigit == 0:
                    if prevdigit > 2:
                        error = 1
                        break
                    else:
                        dp[i] = dp[i-2]
                else:
                    if prevdigit == 1:
                        dp[i] = dp[i-1] + dp[i-2]
                    elif prevdigit == 2:
                        if curdigit > 6:
                            dp[i] = dp[i-1]
                        else:
                            dp[i] = dp[i-1] + dp[i-2]
            #print ("At every step:",dp)
    if error == 1:
        print (0)
    else:
        print (dp[len(inputstr) - 1])
    #print (dp)
     
try:
    while True:
        inputstr = input()
        if inputstr == '0':
            break
        calc_acode(inputstr)
except:
    pass
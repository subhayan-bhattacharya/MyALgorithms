# https://leetcode.com/problems/count-and-say/description/

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        word = "1"
        
        if n == 1:
            return "1"
        else:
            for i in range(2,n+1):
                prev = ""
                count = 0
                temp_str = ""
                for digit in word:
                    #print "checking digit:",digit
                    if digit == prev:
                        count += 1
                        #print "Incrementing count to :",count
                    else:
                        #print "Does not match prev which is : ",prev
                        if prev == "":
                            count = 1
                        else:
                            temp_str = temp_str + str(count) + prev
                            count = 1
                    
                    prev = digit
                temp_str = temp_str + str(count) + digit
                word = temp_str
        return word
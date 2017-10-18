class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        binary_str = "{0:b}".format(n)
        alternate = True
        for i in range(len(binary_str) - 1):
            if binary_str[i] != binary_str[i+1]:
                continue
            else:
                alternate = False
                break
        if alternate:
            return True
        else:
            return False
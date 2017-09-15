class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        import string
        from collections import OrderedDict
        letters = string.ascii_uppercase[:26]
        alphabets_pos_mapping = OrderedDict()
        alphabets_pos_mapping = {index + 1:key for index,key in enumerate(letters)}
        column_name = []
        while n > 0:
            rem = n % 26
            if rem == 0:
                column_name.append("Z")
                n = n//26 - 1
            else:
                column_name.append(alphabets_pos_mapping[rem])
                n = n//26
        column_name.reverse()
        return ''.join(column_name)
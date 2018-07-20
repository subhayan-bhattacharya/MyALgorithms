class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        currencies = {5:0,10:0,20:0}
        for index,bill in enumerate(bills):
            if index == 0:
                if bill > 5:
                    return False
                else:
                    currencies[5] = currencies[5] + 1
            else:
                if bill == 5:
                    currencies[5] = currencies[5] + 1
                else:
                    diff = bill - 5
                    if diff == 15:
                        if currencies[10] == 0:
                            if currencies[5] < 3:
                                return False
                            else:
                                currencies[5] = currencies[5] - 3
                        else:
                            if currencies[5] == 0:
                                return False
                            else:
                                currencies[10] = currencies[10] - 1
                                currencies[5] = currencies[5] - 1
                    elif diff == 5:
                        if currencies[5] == 0:
                            return False
                        else:
                            currencies[5] = currencies[5] - 1
                    currencies[bill] = currencies[bill] + 1
                            
                        
        return True
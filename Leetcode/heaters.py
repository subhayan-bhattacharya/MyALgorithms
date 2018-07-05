# https://leetcode.com/problems/heaters/description/
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        
        radius = 0
        end = len(heaters) - 1
        start = 0
        for index,house in enumerate(houses):
            required_radius = 0
            
            if house <= heaters[0]:
                #Special case there is no heater in front
                required_radius = heaters[0] - house
            elif house >= heaters[-1]:
                # Special case when there is no heater after it
                required_radius = house - heaters[-1]
            else:
                flag = False
                #Other case when the house has heaters before and after it
                while flag is not True:
                    if house == heaters[start]:
                        required_radius = 0
                        flag = True
                    elif house > heaters[start]:
                        if house < heaters[start + 1]:
                            required_radius = min(house - heaters[start],heaters[start + 1] - house)
                            flag = True
                    if not flag:
                        start = start + 1

            #print (house,required_radius)
            radius = max(required_radius,radius)
        return radius
            
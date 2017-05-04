# Comparators are used to compare two objects. In this challenge, you'll create a comparator and use it to sort an array. The Player class is provided in the editor below; it has two fields:

# A string, .
# An integer, .
# Given an array of  Player objects, write a comparator that sorts them in order of decreasing score; 
#if  or more players have the same score, sort those players alphabetically by name. 
#To do this, you must create a Checker class that implements the Comparator interface,
# then write an int compare(Player a, Player b) method implementing the Comparator.compare(T o1, T o2) method.



from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __repr__(self):
        pass
    def comparator(a, b):
        if a.score < b.score:
            return 1
        elif a.score > b.score:
            return -1
        else:
            if a.name == b.name:
                return 0
            elif a.name < b.name:
                return -1
            elif a.name > b.name:
                return 1
           
        
def cmp_to_key(mycmp):
    class Checker(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return Checker  
    
    


    


    







    
    
    

        
    
    





    
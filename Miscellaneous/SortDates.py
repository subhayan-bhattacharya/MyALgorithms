from datetime import datetime
from operator import attrgetter

class Person:
    def __init__(self,name,day,month,year):
        self.name = name
        self.day = day
        self.mon = month
        self.year = year
        
    def __str__(self):
        if self.day < 10:
            day = "0" + str(self.day)
        else:
            day = str(self.day)
        if self.mon < 10:
            mon = "0" + str(self.mon)
        else:
            mon = str(self.mon)
        display = day + "-" + mon + "-" + str(self.year)
        return display
        
    def __repr__(self):
        if self.day < 10:
            day = "0" + str(self.day)
        else:
            day = str(self.day)
        if self.mon < 10:
            mon = "0" + str(self.mon)
        else:
            mon = str(self.mon)
        display = day + "-" + mon + "-" + str(self.year)
        return display
     
    def __eq__(self, other):
        return self.day == other.day and self.mon == other.mon and self.year == other.year

    def __hash__(self):
        return hash(self.__str__())
        
def sortdates(l1):
    for dates in l1:
        dates.finalbirthdate = datetime.strptime(repr(dates),"%d-%m-%Y")
    return sorted (l1,key=attrgetter('finalbirthdate'),reverse=True)
           
if __name__ == '__main__':
    p1 = Person("Subhayan",18,9,1984)
    p2 = Person("Poulomi",13,1,1988)
    p3 = Person("Dummy",13,1,1988)
    p4 = Person("Shaayan",25,11,1988)
    p5 = Person("Father",1,1,1954)
    
    check = sortdates(set([p1,p2,p3,p4,p5]))
    for persons in check:
        print (persons)


    
    
            
            
        


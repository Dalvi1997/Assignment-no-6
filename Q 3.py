from heapq import nlargest
d={'Java':6,'Perl':2,'C++':5,'Python':8,'AngularJs':3,'Ruby':9,'Bootstrap':1}
three_largest=nlargest(3,d,key=d.get)
print(three_largest)

    


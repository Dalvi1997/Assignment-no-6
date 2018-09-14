sub_list=['Maths','Phy','Chem','Java','Mech']
marks_list=[78,74,68,77,67]
d={}
count=0
for each in sub_list:
    d[each]=marks_list[count]
    count=count+1
print(d)

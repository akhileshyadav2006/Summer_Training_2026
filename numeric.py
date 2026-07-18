
c = 2+4j

print(c)



name = "Akhilesh Yadav"
#
student_data=[23,"Akhilesh Yadav","BCA","C",4.5]
print(student_data)

student = ["Akhilesh","BCA",[60,70,80]]
for item in student:
    if isinstance(item,list):
        for x in item:
            print("->",x)
    else:
        print(item)        


student = ["Akhilesh","BCA",[60,70,80]]
count=1
for items in student:
    if isinstance(items,list):
        print(count,end="")
        count=count+1
        for x in items:
            print("*",x)
    else:
        print(count ,"",items) 
        count=count+1

        # slicing 
list = [10,20,30,40,50]
print(list[:3])
print(list[2:])
print(list[1:4])
print(list[-3::])
print(list[:2])
print(list[::-1])

# modifying element
lst = [10,20,30,40]
lst[1] = 99
lst[2] = 100

lst[-1] = 44
print(lst)

# Adding Elements
# append()

lst = [10,20]
lst.append(30)
print(lst)

# insert(index, value)

lst = [10,20,30]
lst.insert(1,99)
print(lst)
# extend(itrable)
lst = [10,20,30]
lst.extend([40,50,60])
print(lst)

# Concatenation(+)- combine lists

a = [1,2];b = [3,4]
c=a+b
print(c)


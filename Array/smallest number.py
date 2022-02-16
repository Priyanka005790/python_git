#program to find smallest
# list1 = [10,20,4,45,99]
# list1.sort()
# print("smallest element is:",*list1[:1])


#creating empty list
list1 = []
#asking number of elements to put in list
num = int(input("Enter number of element in list:"))
#iterating till num to append element in list
for i in range(1,num+1):
    a=int(input("Enter element:"))
    list1.append(a)
#print maximum element
print("smallest element is:",min(list1))

list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
for i in range(1, 100):
    if i%7==0 and i%3!=0:
        list1.append(i)
    if i % 7 == 0 and i % 3 == 0:
        list2.append(i)
        if i%2!=0:
            list3.append(i)
    sum_of_digits = sum(int(digit) for digit in str(i))
    if (pow(sum_of_digits, 2)) == i:
        list4.append(i)
    if i%sum_of_digits==0:
        list5.append(i)
print ("Numbers divisible by 7 but not divisible 3:",list1)
print ("\nNumbers divisible by 7 and divisible 3:",list2)
print ("\nodd Numbers divisible by 7 and divisible 3:",list3)
print ("\nnumbers that are divisible by the sum of its digits:",list5)
print("\nnumbers that are equal to the square of the sum of its digits:",list4)
'''
#Counting Variables
arr = [1 , 2 , 3 , 4 , 5 , 6] 
count = 0
for n in arr:
    count += 1
print(count)'''

'''#Checking Of List Sorted Or Not
l = [1 , 2 , 8 , 4 , 5]
is_sort = True
for n in range(0 , len(l)-1):
    if l[n] > l[n+1]:
        is_sort = False
if is_sort==True:
    print("True")
else:
    print("False")'''

'''#Finding The Max In The List
l = [1 , 5 , 7 , 9 , 0]
max = l[0]
for n in l:
    if n > max:
        max = n
print(max)'''
    
'''#Splitting Of A List Into Two Lists One Into---> Even And One Into Odd
l = [1 , 2 , 3 , 4 , 5 , 6]
even_l = []
odd_l = []
for n in l:
    if n % 2 == 0:
        even_l.append(n)
    else :
        odd_l.append(n)
print(even_l)
print(odd_l)'''

'''#Counting The Frequency Of Each element in the list
l = [1, 2, 2, 3, 3, 3]
freq = {}
for n in l:
    if n not in freq:
        freq[n] = 1
    else :
        freq[n]+=1
print(freq)'''

'''#Removal Of Duplicates In The List
l = [1, 2, 2, 3, 1, 4]
l_d = []
for n in l:
    if n not in l_d:
        l_d.append(n)
print(l_d)'''

'''#Reversing A List
l = [1, 2, 3, 4, 5]
l_r = []
for n in range(len(l)-1 , -1 , -1):
    l_r.append(l[n])
print(l_r)'''

'''#Rotating A List To Left Position
l = [1 , 2 , 3 , 4] 
x = l[0]
l_r = []
for n in range(0 , len(l)-1):
    l[n] = l[n+1]
    l_r.append(l[n])
l_r.append(x)
print(l_r)'''

'''#Finding The Second Max Element

l = [1 , 2 , 3 , 4 , 5]
max_1 = l[0]
for n in l:
    if n > max_1:
        max_1 = n
max_2 = None
for n in l:
    if n  != max_1:
        if max_2 is None or n > max_2:
            max_2 = n
print(max_2)'''

'''#Merging Dicts Alternatively
l1 = [1 , 2 , 3]
l2 = [4 , 5 , 6]
l3 = []
for n in range(0 , len(l1)):
    l3.append(l1[n])
    l3.append(l2[n])
print(l3)'''

'''#Finding Common Elemnts In Two Lists
l1 = [1, 2, 2, 3, 4]
l2 = [2, 3, 5]
l = []
l4 = []
for n in l1:
    if n in l2:
        l.append(n)
for n in l:
    if n not in l4:
        l4.append(n)
print(l4)'''

'''#Large Function
def stats(arr):
    sum = 0
    max = arr[0]
    count = 0
    for n in arr:
        sum += n
        count += 1
        avg = sum / count
        if n > max:
            max = n
    return max , avg , sum
x = [ 1 , 2 , 3 , 4 ,5]
print(stats(x))
'''

'''#Function To Check Prime
def is_prime(n):
    if n <= 1:
        print("Not Prime")
    
    is_prime = True
    for i in range(2 , n):
        if n % i ==0:
            is_prime = False
            break
    


x = 1
print(is_prime(x))'''

'''def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


print(is_prime(7))   # True
print(is_prime(10))  # False
print(is_prime(1))   # False


'''
    
'''def remove_duplicates(arr):
    result = []
    for n in arr:
        if n not in result:
            result.append(n)
    return result


print(remove_duplicates([1, 2, 2, 3, 1, 4]))
# Output: [1, 2, 3, 4]'''









    

            




    
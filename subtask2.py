#SUBTASK 8.2

n = 0 #count
s = 0 #sum
m = 0 #minimum
a = 0 #mean

num = [4,5,1,18,-1] #list of numbers

x = num[n] #assign first number in list to x
m = x #minimum value = first number in list

while x != -1: #loop until last value
    s = s + x #add to sum
    if m > x: #if x is less than min value, change min value
        m = x
    n = n + 1 #count
    x = num[n] #take next number in list


if n == 0: #if list only has -1, a = -1 & m = -1
    a = -1
    m = -1
else: #else calc mean
    a = s/n

print (n,s,m,a) #print all values

# looks like i learned how to use git today
    
    

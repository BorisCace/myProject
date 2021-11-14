#SUBTASK 8.1

q = 0 #setting variable q to zero
n = int(input()) #assigning value to n

while q*q < n: #loop until q^2 is greater than n
    q = q + 1

if q*q == n: #if equal print q^2
    print(q*q)
else: #if not subtract 1 from q and square
    q = q -1
    print(q*q)

# looks like i learned how to use git today

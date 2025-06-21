#for loop

#for i in range(5):
  #  print(i)

# range (start, end - 1, step size)
#for i in range(1, 10, 2):
 #   print(i)

#strings
string = "Mehul"

for i in string:
    print(i)

#Reverse a string
for i in string[::-1]:
    print(i)


# WHILE LOOP - Continues to execute as long as the condition given is true

count = 0
while (count <= 5):
    print(count)
    count+=1

# Loop Control Statements

for i in range(10):
    if ( i == 5):
        continue
    elif ( i == 6):
        pass
    elif(i == 8):
        break
    print(i)

## Nested Loop
for i in range(3):
    for j in range(2):
        print(f"i :{i} and j : {j}")

# Example - Calculate the sum of N Natural Numbers using for and while loops

n = int(input("Enter N Natural Number: "))
count = 0
# for loop
for i in range(1, n + 1):
    if (n == 0):
        break
    count += i

print(f"Sum of {n} Natural Numbers: {count}")




# # Question 1: Create an Empty List called my_list

my_list = []
print(my_list)

# Question 2: Append the following elements to my_list: 10, 20, 30, 40

my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

# Question 3: Insert the value 15 at the second position in the list

my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.insert(1, 15)
print(my_list)

# Question 4: Extend my_list with the following elements: 50, 60, 70

my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.insert(1, 15)
my_list.extend([50, 60, 70])
print(my_list)

# Question 5: Remove the last element from my_list

my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.insert(1, 15)
my_list.extend([50, 60, 70])
my_list.pop()
print(my_list)

# Question 6: Sort my_list in ascending order

my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.insert(1, 15)
my_list.extend([50, 60, 70])
my_list.pop()
my_list.sort()
print(my_list)

# Question 7: find the index of 30 in my_list

my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.insert(1, 15)
my_list.extend([50, 60, 70])
my_list.pop()
my_list.sort()
print(my_list.index(30))

import random 

numbers = [3, 1, 4, 12, 8, 5, 2, 9]
names= ['Wyatt', 'Brandon', 'Kumar', 'Eugene', 'Elise']


# Apply the sort() funtion to the lists
numbers.sort()
names.sort()

# Display the output
print(numbers)
print(names)

# we can say that sort() applies to any lists and is a function in the
# mathematical sense. Indeed, it meets all the criteria:
# 1. The domain is all lists that can be sorted.
# 2. The range is the set of all such lists that have been sorted.
# 3. sort() always maps each list that can be inputted to a unique sorted list
# in the range.

# Set a random seed so the code is reproducible
random.seed(1)

# Run the random.shuffle() function 5 times and display the outputs
for i in range(0,5):
numbers = [3, 1, 4, 12, 8, 5, 2, 9]
random.shuffle(numbers)
print(numbers)

# In each iteration, the Python function shuffle() takes the same input, 
# but the output is different each time. Therefore, the Python function 
# shuffle() is not a mathematical function. It is, however, a relation 
# that can pair each list with any ordering of itself.

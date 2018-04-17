# Implementing the task
# Find out the final coordinats of turtle by calculating input commands
d = {}

# Function to update values in the dictionary
def update_coordinates(d, key, value):
    if key in d:
        d[key] += value
    else:
        d[key] = value

# Number of commands
n = int(input())
string = ''

# Going through all commands
for i in range(n):
    string = input().split()  # Splitting the line by gap into command and value
    update_coordinates(d, string[0], int(string[1]))

print(d)  # Checking if the dictionary was updated properly
    
first = 0
second = 0
# Calculating the final point of the turtle
for x in d:
    if x == 'east':
        first += d[x]
    elif x == 'north':
        second += d[x]
    elif x == 'west':
        first -= d[x]
    elif x == 'south':
        second -= d[x]

# Showing the results - final point
print(first, second)
    

    

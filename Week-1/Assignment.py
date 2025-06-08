rows = 5  
# Lower-Triangle
print("Lower Triangle:")
for i in range(1, rows + 1):
    print("* " * i)
print() 
# Upper-Triangle
print("Upper Triangle:")
for i in range(rows, 0, -1):
    print("  " * (rows - i) + "* " * i)
print()
# Pyramid
print("Pyramid:")
for i in range(1, rows + 1):
    spaces = ' ' * (rows - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)

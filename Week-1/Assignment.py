# Lower-Triangle
rows = 0
for i in range(rows,0,-1):
  print("  " * (rows - i) + "* " * i)

# Upper-Triangle
rows = 5
for i in range(1, rows + 1):
    print("* " * i)
  
# Pyramid
rows = 5
for i in range(1, rows + 1):
    spaces = ' ' * (rows - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)

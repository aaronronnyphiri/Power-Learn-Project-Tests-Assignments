#   Write a Python program to construct the following pattern of stars(*), using a nested for loop.
#   *
#   * *
#   * * *
#   * * * *
#   * * * * *
#   * * * *
#   * * *
#   * *
#   *

for rows in range(5):
    for colums in range(rows + 1):
        print("#", end=" ")
    print()
for rows in range(5):
    for colums in range(4 - rows):
        print("#", end=" ")
    print()    


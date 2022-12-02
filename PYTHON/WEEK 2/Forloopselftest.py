#   QUESTION :
#   For Loops Self Test
#   In this exercise, you will practice control flow with loops to solve problems. You will be given a list of integers and you will 
#   have to add some code to find a specific number in a list and return it.
#   Instructions :
#   1. Under the num_list create a new for loop and print out each value on the list in sequential order.
#   2. Inside the for loop, create a condition that will look for all numbers that are greater than 45 and print out only numbers 
#      that meet that condition
#   3. Change the print statement to “Over 45” and add an else condition with a print statement of “Under 45”.
#   4. Update the for loop to use the enumerate function so you can get and use the index. Alter the condition to look for number 36 
#      and print out the following: ‘Number found at position: ‘, index number
#   5. Next, create a new variable called count and assign it a value of 0 and place it outside the for loop.
#   6. Inside the for loop increment the counter by 1.
#   7. Add a print statement outside the for loop to print the value of the count variable.
#   8. Finally, add a break statement directly after the print statement inside the if condition for finding the number. 
#   Here is the List to use in this test:
#       num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]
sorted_num_list = sorted(num_list)       #sorts num_list in ascending order
print("===============Q1===============")
print("The values in sequential order are : ")
for num in sorted_num_list:
    print(num)

print("===============Q2===============")
print("The values greater than 45 are :")
for num in sorted_num_list:   
    if num > 45 :
        print(num)

print("==============Q3===============")
print("Over 45 : ")
for num in num_list:    
    if num > 45 :
        print(num)
print("Under 45 :")
for num in num_list:
    if num < 45 :
        print(num)

print("===========Q4,Q5,Q6,Q7,Q8===============")
count = 0
for index,number in enumerate(sorted_num_list) :
    count = count+1
    if number == 36 :
        print("Number 36 is found at position : ",index)
        break
print( "The value of the count variable is : ",count)







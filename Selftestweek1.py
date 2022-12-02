#A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. 
#Ask the user for their salary and year of service and print the net bonus amount. Write a python 
#code to implement this scenario.
employee_name = input("Enter eployee's name : ")
salary = int(input("Enter current salary : "))
current_year = int(input("Enter current year :"))
year_of_employment = int(input("Entrer the year of employment : "))
print("----------------------------------------------------------------")
years_of_service = current_year - year_of_employment
bonus_amount = ( 5 / 100 ) * salary
net_salary = bonus_amount + salary
if years_of_service > 5 : 
  print("Employee Name : ", employee_name)
  print("Current year : ", current_year)
  print("Year of Employment : ", year_of_employment)
  print("Current salary : ", salary)  
  print("Congratulations! Your net salary is : ", net_salary)
else :
  print("Employee Name : ", employee_name)
  print("Current year : ", current_year)
  print("Year of Employment : ", year_of_employment)
  print("Current salary : ", salary)  
  print("Your net salary is : ", salary)
  print("Comment : You are not eligible for 5% bonus. ")
#QUESTION 1
#Write a functionto print "hello_USERNAME!" USERNAME is the input of the function.

def hello_name(user_name):
        print("Hello_ " + user_name.upper() + "!")

hello_name(("USERNAME"))



#QUESTION 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing. 

def odd_numbers():
   i = 1
   while i < 100:
        print(i)
        i += 2
   return

print(odd_numbers())



#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
 
def max_num_in_list(a_list):
        return max([item for item in a_list])

print(max_num_in_list(([1,66,7,12])))
        

max_num_in_list()



#Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
#The return should be a boolean Type (true/false). 

def is_leap_year(a_year):
        not_a_leap_year = False
       
        if (a_year % 400 == 0) and (a_year % 4 == 0) or (a_year % 100 != 0):
                print("Is a leap year")
        
        else:
                not_a_leap_year = True
                print("Is not a leap year")

a_year = int(input("What is the year: "))

is_leap_year(a_year)



#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers
#The return should be boolean Type. 

def is_consecutive(a_list):
    if sorted(a_list) == list(range(min(a_list),max(a_list)+1)):
        return True
    else:
        return False


print(is_consecutive([12,16,14]))

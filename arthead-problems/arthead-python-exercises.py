# Python Algorithm Exercises Explanation

# problems: https://arthead.se/python/exercises/ 

# # question 10: 
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

def main():
    for i in range(2000,3201):
        if i % 7 == 0 and i % 5 != 0:
            print(i,",", end="")

    
#  # question 11:
#  With a given number n, write a program to generate a dictionary that contains (i, i*i).
#  The dictionary shall include all integer values for i from 1 to n (both included).
#  Then the program should print the dictionary.

def built_n_dict():
    n = int(input("Enter a number: "))
    dict_n = {}
    for i in range(n+1):
        dict_n[i]= i*i
    print(dict_n)


# # question 12:
# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

def find_even():
    even = []
    for i in range(1000, 3001):
        if i % 2 == 0:
            even.append(str(i))
    print(even)        


if __name__ == "__main__":
    find_even()


# ## question 13 - 24:
# Define a function max() that takes two numbers as arguments and returns the largest of them. Use the if-else construct available in Python.
# The function max(), from exercise 13, and the function max_of_three(), from exercise 14, will only work for two and three numbers, respectively. But 
# suppose we have a much larger number of numbers, or suppose we cannot tell in advance how many they are? Write a function max_in_list() 
# that takes a list of numbers and returns the largest one.

def find_max(list_):
    if list_ :
        if len(list_) == 1:
            return list_[0]
        else:
            max = list_[0]
            for i in list_[1:]:
                if i > max:
                    max = i
        return max
    
    else:
        return None


if __name__ == "__main__":
    print(find_max([8,1,2,7,19,45,1]))

# ## question 19:
# Define a function reverse() that computes the reversal of a string. For example, reverse("I am testing") should return the string "gnitset ma I".

def reverse_str(str_):
    new_str = ""

    for i in range(len(str_)-1, 0, -1):
        new_str = new_str + str_[i]
    return print(new_str)


if __name__ == "__main__":
    reverse_str("AYSE")


### question 20:
# Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards).
#  For example, is_palindrome("radar") should return True.


def is_palidrome(input_x):
    front = 0
    end = len(input_x) - 1
    while input_x[front].lower() == input_x[end].lower() and front < end:
        front += 1
        end -= 1
    if front < end:
        return False
    else:
        return True

if __name__ == "__main__":
    print(is_palidrome("aya"))
    print(is_palidrome("ayse"))



# # question 21:
# Define a function overlapping() that takes two lists and returns True if they have at least one member in common,
#  False otherwise. You may use your the in operator, but for the sake of the exercise, you should (also) write 
#  it using two nested for-loops. That two for-loops are nested means that one loop is placed inside the other loop

# solution 1:
def overlapping(list1, list2):
    for i in list1:
        if i in list2:
            return True
    return False

# solution 2:
def overlapping2(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    else:
        return False

if __name__ == "__main__":
    print(overlapping2([1,2,3], [4,5,6]))
    print(overlapping2([1,2,3],[4,5,1]))

# ## question 22:
# Define a function generate_n_chars() that takes an integer n and a character c and returns a string, n characters long,
#  consisting only of c:s. For example, generate_n_chars(5,"x") should return the string "xxxxx". 
# (Python is unusual in that you can actually write an expression 5 * "x" that will evaluate to "xxxxx".
#  For the sake of the exercise you should ignore that the problem can be solved in this manner.)

def generate_chars(n, c):
    new_str = ""
    for i in range(n):
        new_str += c
    return new_str


if __name__ == "__main__":
    print(generate_chars(2, "a"))
    print(generate_chars(5, "b"))




# # question 23:
# Define a function histogram() that takes a list of integers and prints a histogram to the screen.
#  For example, histogram([4, 9, 7]) should print the following:


def histogram(list1):
    for i in range(len(list1)):
        print(list1[i]* "*")
    
if __name__ == "__main__":
    histogram([4, 9, 7])


# # question 27:
# Write a function find_longest_word() that takes a list of words and returns the length of the longest one. Look at solution

def max_length(word_list):

    len_list = []

    for s in word_list:

        len_list.append(len(s))

    return len_list

if __name__ == "__main__":

    word_list = ["Ayse", "Derya","Çanakkale","Dünya"]

    len_list = max_length(word_list)

    print(len_list)

    # second way

    len_list2 = [len(s) for s in word_list]

    print(len_list2)




# ## question 29:
# A prime number is an integer greater than 1 that is only divisible by one and itself.
#  Write a function that determines whether or not its parameter is prime, returning True
# if it is, and False otherwise. Write a main program that reads an integer
# from the user and displays a message indicating whether or not it is prime.
# Ensure that the main program will not run if the file containing your solution
# is imported into another program.

def is_prime(n):

    if n <= 1:

        return False
    
    for i in range(2, n):

        if n % i == 0:

            return False
    
    return True


if __name__ == "__main__":

    print(is_prime(29))



# # qustion 32:
# Write a program that reads integers from the user and stores them in a list. Your program should
# continue reading values until the user enters 0. Then it should display all of the values entered
# by the user (except for the 0) in order from smallest to largest, with one value appearing on each line.

def print_num():

    num_list = []

    flag = False

    while not flag:

        number = int(input("Enter a number. To exit please enter 0 : "))

        if number != 0:

            num_list.append(number)

        else:

            flag = True

    sorted_list = sorted(num_list)
    
    print(sorted_list)

if __name__ == "__main__":

    print_num()




#1Write a Python program to get a single string from two given strings,
#separated by a space, and swap the first two characters of each string
 name1="magdaline"
 name2="wambui"
 new_name1=name2[:2]+name1[2:]
 new_name2=name1[:2]+name2[2:]
 result= new_name1+''+new_name2
print(result)
# 2.  Write a Python function that takes a list of words and
#  returns the longest word and the length of the longest one
def longest_word(names):
    longest_word=""
    length=0
    for names in names:
        if len(name)>length:
           longest_word=name
           length=len(name)
    return longest_word
print(logest_Word(["mary","faith","ann","princess"]))    
# 3. Write a Python program that accepts a comma-separated sequence
#  of words as input and prints the distinct words in sorted form (alphanumerically).


#  4.. Write a Python function that takes two lists and
#  returns True if they have at least one common member.
def common_member(list1, list2):
    nums1 = word(list1)
    nums2 = word(list2)
    if item in list2:
        return True
    else:
        return False
list1=[10,18,50]
list2=[25,38,87,90]
# 5. Write a Python program to convert a list to a list of dictionaries.
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]


#  6. Write a Python program to check whether all dictionaries in a list are empty or not
def dict_empty(places):
    for places in places:
        if place:
            return False
    return True
print(dict_empty(["Nakuru","Nyahururu","sipili","Kinamba"]))    
# 7. Given a list of numbers, use list comprehension to remove all odd numbers from the list:
 numbers = [5,8,90,76,54,34,56]
numEven=[n for n in numbers if n%2==0]
print(numEven)
#  8. Find the common numbers in two lists (without using a tuple or set)
nums1 = [1, 2, 3, 4]
nums2= [2, 3, 4, 5]
common_nums = [num1 for num1 in num1 if num1 in nums2]
print(common_nums)
# 9. Use a nested list comprehension to find all of the numbers from 1-1000 that
#  are divisible by any single digit besides 1 (2-9) in python



# 10. Write a Python function to remove all vowels in a string
def remove_vowels(name):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in name:
        if char not in vowels:
            result += char
    return result
print(name("margaret")) 
remove_vowels()   
    
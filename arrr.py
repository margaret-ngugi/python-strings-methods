#1. Write a Python program to get a single string from two given strings, separated by
# a space, and swap the first two characters of each string
word1="mercy"
word2="orishaba"
word1_swapt=word2[:2]+word1[:2]
word2_swapt=word1[:2]+word2[2:]
results=word1_swapt+' '+word2_swapt
print(results)
# 2.  Write a Python function that takes a list of words and returns the longest word and the length of the longest one
# def get_longest(words):
words=["orishaba","mercy","lowice"]
logest_Word=''
for word in words:
        if len(word)>len(logest_Word):
            logest_Word=words
print (len(logest_Word))
# 3. Write a Python program that accepts a comma-separated sequence of
# words as input and prints the distinct words in sorted form (alphanumerically).
# list =["god","holla","kla"]
# new_list=list.sorted()
# print(new_list)
# 4.. Write a Python function that takes two lists and
#  returns True if they have at least one common member.
# def two_lists(list_a,list_b):
#     for i in list_a:
#      for i in list_b:
#           if list_a==list_b:
#             return True
#           return False
# print(two_lists(list_b=[1,2,3,4,5,6,7]))
# print(two_lists(list_a=[0,9,8,7,6,5]))
# 5. Write a Python program to convert a list to a list of dictionaries.
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
colors=["Black", "Red", "Maroon", "Yellow"]
color_codes=["#000000", "#FF0000", "#800000", "#FFFF00"]
colored=zip(colors,color_codes)
for colors,color_codes in colored:
    print(colors,color_codes)


    #1. Write a Python program to get a single string from two given strings,
#   separated by a space, and swap the first two characters of each string
def del_string(str1,str2):
    new_str1=str2[:2]+str1[2:]
    new_str2=str1[:2]+str2[2:]
    return new_str1+''+new_str2
    str1="Akirachix"
    str2="school"
    print(result)
# 2.  Write a Python function that takes a list of words and
#  returns the longest word and the length of the longest one
def longest_word(words):
    longest_word=""
    length=0
    for word in words:
        if len(word)>length:
           longest_word=word
           length=len(word)
    return longest_word,length
# 3. Write a Python program that accepts a comma-separated sequence
#  of words as input and prints the distinct words in sorted form (alphanumerically).


#  4.. Write a Python function that takes two lists and
#  returns True if they have at least one common member.
def common_member(list1, list2):
    nums1 = group(list1)
    nums2 = group(list2)
    if item in list 2:
        return True
    else:
        return False
list1=[23,78,90]
list2=[15,78,87,90]
# 5. Write a Python program to convert a list to a list of dictionaries.
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]


#  6. Write a Python program to check whether all dictionaries in a list are empty or not
def all_dictionaries_empty(dictionary_list):
    for dictionary in dictionary_list:
        if dictionary:
            return False
    return True
# 7. Given a list of numbers, use list comprehension to remove all odd numbers from the list:
#  numbers = [3,5,45,97,32,22,10,19,39,43]
# evens=[n for n in numbers if n%2==0]
# print(even)
#  8. Find the common numbers in two lists (without using a tuple or set)
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
common_numbers = [num_a for num_a in list_a if num_a in list_b]
print(common_numbers)
# 9. Use a nested list comprehension to find all of the numbers from 1-1000 that
#  are divisible by any single digit besides 1 (2-9) in python
divisible_numbers = [num for num in range(1, 1000) if any(num % digit == 0 for digit in range(2, 10))]
print(divisible_numbers)
# 10. Write a Python function to remove all vowels in a string
def remove_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in word:
        if char not in vowels:
            result += char
    return result
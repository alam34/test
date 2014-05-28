#!/usr/bin/python
#Author: Shah Alam
#Date: May 13, 2014
#Description: This Python script needs to be run as
#                   python anagram_position CAT
#             The first argument can be upto 20 characters in length. Input word
#             is converted to all uppercase before processing. Numbers are not allowed.

import sys

def factorial(num):
    "Calculates factorial of a number"
    fact = 1;
    for i in range (1,num+1):
        fact = fact * i
    return fact

def anagram_position (str):
    "Prints out the position of the input word in the list of anagrams"
    position = 0
    str_list = list(str)
    str_list_sorted = list(str)
    str_list_sorted.sort()	
	
    list_len = len (str_list)
		
    j = 0
	#for each char in the sorted list, check if that is in the first position
	#of the unsorted list. If there is not a match, add the permutation
	#of remaining positions in the position counter. If there is a match
	#then eliminate the char from consideration
    while (str_list_sorted):
		if str_list_sorted[j] != str_list[0]:
			position += factorial(list_len-1)
			j += 1
		else:
			del(str_list_sorted[j])
			del(str_list[0])
			list_len -= 1
			j = 0
			
    return position+1
			

#Check if the input string is present in the command line
try:
    arg = sys.argv[1]
except IndexError:
	print 'Please enter a string in the command line, as the first argument. E.g., python anagram_position.py CAT'
else:
	if arg.isdigit():
		print "Sorry, this script doesn't accept numbers"
		exit()
		
	if (len(arg) > 20):
		print "Sorry, this script doesn't accept words more then 20 characters"
		exit()
		
	#convert input to uppercase	
	uppercase = arg.upper()
	position = anagram_position (uppercase)
	print 'Position of `' + arg + '` in the sorted anagram list is: ' + str(position)
	
	
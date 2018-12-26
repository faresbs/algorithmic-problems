"""
bitap algorithm implementation for exact string matching + shift-or
"""

#Complexity is O(mn)
def bitap(text, pattern):
	m = len(pattern)

	if(m == 0):
		return text

	#Init a bit array of size m
	R = [0] * (m + 1) 
	#Set the first element as 1
	R[0] = 1

	#print R

	#loop over the text 
	for i in range(len(text)):

		#print R

		#loop over the pattern + update
		for j in range(m, 0, -1):

			if(R[j-1] == 1 and text[i] == pattern[j-1]):
				R[j] = 1 
		
		#we found a complete match
		if(R[m]):	
			print 'found it'
			
			#return the position of the matched pattern
			return i - m + 1

	return None


#TO FINISH
#Bitap bitwise (shift-or / shift-and)
#PROBLEM: FASTER TO CODE ALPHABET AND EASILY RETRIVE THE BITWISE VALUE
#Complexity is O(n)

import locale

def bitap_bitwise(text, pattern):

	#max length of alphabet
	alph = locale.CHAR_MAX + 1

	m = len(pattern)

	if(m == 0):
		return text

	#Preprocessing step

	#init the mask by 0s for all the alphabet
	#T[m, alph] = T[row, column]
	T = [x[:] for x in [[0] * 2] * 10]

	#init the mask by 0s for all the alphabet
	for i in range(alph):
		pass



	#Init a bit array of size m
	R = [0] * (m + 1) 
	#Set the first element as 1
	R[0] = 1

	#print R





text = ['a','a','b','a','a','a','c','a','a','b']
pattern = ['a','a','c']

print text
print pattern

print bitap(text, pattern)
#print bitap_bitwise(text, pattern)
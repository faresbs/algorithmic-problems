#Problem: find if x can be a possible result of a sequence of multiplication 
# + find a possible multiplication brackets that gives x

# Naive method : trying all possibilities and check if it return the right output every time
# Naive method is exponontial (catalan numbers)

#Return a boolean value that indicates if x is the result of sequence of multiplication
#and save the paranthesis places
#complexity is polynomial

#Temporal complexity is O(n^3*k^2) 
def find(X, T, A, x):

	#length of the input 
	n = len(X)

	#length of alphabet 
	k = len(A)

	#Save results
	#Every element of the table have k possibilities
	M = [[[None for y in range(k)] for i in range(n)] for j in range(n)]

	#Fill the diagonal with the elements of the input
	for i in range(n):
		M[i][i][0] = X[i]


	#to recover the position of the parentheses
	p = [[[None for y in range(k)] for i in range(n)] for j in range(n)]

	## Step 1
	# find out

	# s + 1 is the number of element to multiply 
	for s in range(n):
		for i in range(n-s):

			# j is lastest element to multiply 
			j = i + s

			h = 0

			for c in range(i, j):

				#loop over all the possibilities for the two 
				#sub-elements (first and second)
				for y in range(k):
					for z in range(k):
						
						#elements of multiplication										
						first = M[i][c][y]
						second = M[c+1][j][z]

						#if one value is None then skip
						if(first == None or second == None):
							continue
						

						#search the multiplication 
						#result in the multiplication table
						result = T[A.index(first)][A.index(second)]

						if result not in M[i][j]:
							M[i][j][h] = result

							#save all posibilities
							p[i][j][h] = c

							#increase h to save different 
							#results
							h += 1

	
	### Step 2 
	
	#Find multiplication brackets using the stored c values
	#begin with the last element
	
	current = M[0][n-1]

	#save position of multi
	m = []

	i = 0
	j = n-1

	wanted = x

	while(i + 1 < j): 

		#take the wanted result index		
		if(wanted in current):
			k = current.index(wanted)
		else:
			return None

		#retrieve position
		c = p[i][j][k]

		#Save position of parentheses
		m.append(c)

		
		if(i == c or i + 1 == c):

			current = M[c+1][j]

			#find the wanted element by testing all possibilities
			for a in M[c+1][j]:
				
				#if one value is None then skip
				if(a == None):
					continue

				if(wanted == T[A.index(M[i][c][0])][A.index(a)]):
					wanted = a 

			i = c + 1

		elif(j == c+1 or j - 1 == c):

			current = M[i][c]

			#find the wanted element by testing all possibilities
			for a in M[i][c]:

				#if one value is None then skip
				if(a == None):
					continue

				if(wanted == T[A.index(a)][A.index(M[c+1][j])]):
					wanted = a 

			j = c


	#Make parentheses
	newX = []

	for i in range(len(X)):
		newX.append(X[i])
		
		if(i in m):
			newX.append('(')

	newX = newX + [')'] * len(m)

	#Check if the last element have the wanted x or not
	#Last element of the matrice is the solution
	if x in M[0][n-1]:
		return True, newX
	else:
		return False


#sequence of multiplications
X = 'bbbab'

#Table of multiplication
T = [['a','c','c'],['a','a','b'],['c','c','c']]

#Alphabet used 
A = ['a','b','c']

#result that we want to find
x = 'a'

exist, parentheses = parantheses(X, T, A,x)
print exist
print parentheses

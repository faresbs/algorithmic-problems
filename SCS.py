"""
Smallest common superstring of U and V

1/length of the smallest common superstring
2/the smallest common superstring

"""

#returns the length of the smallest common superstring
#Using dynamic programming
#O(mn)
def lSCS(U,V):
	n = len(U)
	m = len(V)

	M = [[0 for i in range(m)] for j in range(n)]


	#Base cases
	if(V[0] != U[0]):
		M[0][0] = 2

	if(V[0] == U[0]):
		M[0][0] = 1


	#first column
	for i in range(1, n):
		if(U[i] == V[0]):
			M[i][0] = M[i-1][0]
		else:
			M[i][0] = M[i-1][0] + 1



	#first row
	for i in range(1, m):
		if(V[i] == U[0]):
			M[0][i] = M[0][i-1]
		else:
			M[0][i] = M[0][i-1] + 1


	#Loop over U and V
	for i in range(1, n):
		for j in range(1, m):

			#recursion cases
			if(U[i] == V[j]):
				M[i][j] = min(M[i][j-1], M[i-1][j])
			else:
				M[i][j] = min(M[i][j-1], M[i-1][j]) + 1 


		

	return M[n-1][m-1]



#Returns the smallest common superstring
#using dynamic programming
#O(mn)
def SCS(U, V):
	n = len(U)
	m = len(V)

	#Save the results
	M = [[0 for i in range(m)] for j in range(n)]

	#Base cases
	#concat of both chars
	if(V[0] != U[0]):
		M[0][0] = V[0] + U[0]

	#return one of them
	if(V[0] == U[0]):
		M[0][0] = V[0]


	#first column
	for i in range(1, n):
		if(U[i] == V[0]):
			M[i][0] = M[i-1][0]
		else:
			M[i][0] = M[i-1][0] + U[i]



	#first row
	for i in range(1, m):
		if(V[i] == U[0]):
			M[0][i] = M[0][i-1]
		else:
			M[0][i] = M[0][i-1] + V[i]


	#Loop over U and V
	for i in range(1, n):
		for j in range(1, m):

			#recursion cases
			if(U[i] == V[j]):
				if (len(M[i][j-1]) <= len(M[i-1][j])):
					M[i][j] = M[i][j-1]
				else:
					M[i][j] = M[i-1][j]
			else:
				if (len(M[i][j-1]) <= len(M[i-1][j])):
					M[i][j] = M[i][j-1] + V[j]
				else:
					M[i][j] = M[i-1][j] + U[i]


	print M
	return M[n-1][m-1]




V = 'informatique'
U = 'fourniture'

print V
print U


print 'Find the length of the smallest common superstring of both strings: '
length = lSCS(U, V)
print length

print 'Find the smallest common superstring of both strings: '
result = SCS(U, V)
print result
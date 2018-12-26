"""
change-making problem
"""

#Using the greedy approach
#time complexity is O(n)
#Dont always give the optimal solution 
def greedy(coins, value):
	sol = []

	for i in range(len(coins)-1, -1, -1):
		
		while value >= coins[i]:
			
			#Take the most from the current biggest coin
			#or you can just substract
			temp = value - coins[i] * (value/coins[i])

			#Append the current coin (value/coins[i]) times to sol
			sol += ([coins[i]]*(value/coins[i]))
			value = temp
	
	return sol


#Using the recusive approach
#exponontial time
#Get the min number of coins every time
def minCoins(value, coins, n):
	
	#base cases
	if (value == 0):
		result = 0

	elif (n == 0):
		if(value % coins[n] == 0):
			result = value / coins[n]
		else:
			#None if you can't return the change 
			result = None 
	
	#recursive cases
	elif(value >= coins[n]):
		r = (value - (value % coins[n])) / coins[n] 
		result = r + minCoins(value % coins[n], coins, n-1)

	else:
		result = minCoins(value, coins, n-1)

	return result



#Dynamic approach, get rid of those repetitive recurences using an inter array
#we use a 2d array to save the itermediate values
#Time complexity O(mn)
def dynamic(value, coins, n):

	#we dont have to go to recursive computation if we have the result already stored in array
	if(C[n][value] != None):
		return C[n][value]

	#base cases
	if (value == 0):
		result = 0

	elif (n == 0):
		if(value % coins[n] == 0):
			result = value / coins[n]
		else:
			#None if you can't return the change 
			result = None 
	
	#recursive cases
	elif(value >= coins[n]):
		r = (value - (value % coins[n])) / coins[n] 
		result = r + dynamic(value % coins[n], coins, n-1)

	else:
		result = dynamic(value, coins, n-1)

	#save result in the array before returning it
	C[n][value] = result
	return result




#Instead of using a 2d array, we can only use 1d array to save only the last iter
#Time complexity O(mn)
def dynamic2(value, coins, n):

	#base cases
	if (value == 0):
		result = 0

	elif (n == 0):
		if(value % coins[n] == 0):
			result = value / coins[n]
		else:
			#None if you can't return the change 
			result = None 
	
	#recursive cases
	elif(value >= coins[n]):

		r = (value - (value % coins[n])) / coins[n] 
		
		if(C[value] != None):
			#Choose the min between the value of previous coins and using current coin
			result = min(C[value], C[value % coins[n]] + r)
		else:
			result = r + dynamic2(value % coins[n], coins, n-1)

	else:
		
		if(C[value] != None):
			result = C[value]

		else:
			result = dynamic2(value, coins, n-1)

	#save result in the array before returning it
	C[value] = result
	return result



#greedy approach to 
#using the array result of the dynamic approach (the last array) and return the min coins for M <= L using greedy
def dynamic_greedy(value, C, coins):

	sol = []

	minCoins = C[value]

	#Returns the wanted coins
	for i in range(len(coins)-1, -1, -1):
		
		if(value >= coins[i]):
			count = C[value - coins[i]] + C[coins[i]]

			if(count <= minCoins):
				sol.append(coins[i])

	#Returns the combination using the wanted coins for optimal solution
	change = []

	for i in range(len(sol)):

		while value >= sol[i]:
			value -= sol[i]
			change.append(sol[i])

	return change




v = 16
a = [1,5,12,25]
#a = [1,25,50,100,200]

#Recursive sol
print minCoins(v, a, len(a)-1)

#greedy sol
print greedy(a, v)

#dynamic prog sol

#init the intermediate table for saving results
#C[i,j] with i from 1 to n and j from 0 to V+1 
C = [x[:] for x in [[None] * (v + 1)] * (len(a))]
#store values in a 2d table
for val in range(v + 1):
	for i in range(len(a), -1, -1):
		l = a[:i]
		dynamic(val, l, len(l)-1)

#print C


#We store the values in 1d array
C = [None] * (v + 1)
#store values in a 1d table
for i in range(len(a)):
	l = a[:i+1]
	for val in range(v + 1):
		dynamic2(val, l, len(l)-1)

#print C

#Return the min coins using greedy approach and using the last result array of C
print dynamic_greedy(v, C, a)
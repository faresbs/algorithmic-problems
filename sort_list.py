"""
Sorting lists in linear time 
"""

#return sorted list of 1s and 0s + the number of occurence of 0s
#Time complexity O(n)
#Space Complexity O(1)
def sort_01(arr):
	index_debut = 0
	index_fin = len(arr) - 1

	count = 0

	while(index_debut < index_fin): 

		if(arr[index_fin] == 0): 
			(arr[index_debut],arr[index_fin]) = (arr[index_fin], arr[index_debut]) 

			index_debut += 1
			count += 1

		elif(arr[index_fin] == 1): 
			index_fin -= 1

	return arr, count



#return sorted list of 1s, 2s and 0s + the number of occurence of 0s
#Dutch flag problem + solution
"""def sort_012(a):
	count = 0
	index_debut = 0
	index_fin = len(a) - 1
	index_milieu = 0

	while(index_milieu <= index_fin): 

		if(a[index_milieu] == 0): 
			(a[index_debut],a[index_milieu]) = (a[index_milieu], [index_debut]) 

			index_debut += 1
			index_milieu += 1
			count += 1

		if(a[index_milieu] == 2):
			(a[index_milieu],a[index_fin]) = (a[index_fin], a[index_milieu]) 
			index_fin -= 1

		else: 
			index_milieu += 1

		
	return a, count
"""

#Return sorted list of 1s, 2s and 0s + the number of occurence of 0s
#Time complexity: O(n) + O(n) = O(n)
#Space Complexity O(constant)

#We sort first the 0s and the 1s & 2s together, then sort the 1s and 2s
#We can do this for any constant number of variables

def sort_012(arr):
	index_debut = 0
	index_fin = len(arr) - 1

	count = 0

	#Sort 0 and 1 & 2 together
	while(index_debut < index_fin): 

		if(arr[index_fin] == 0): 
			(arr[index_debut],arr[index_fin]) = (arr[index_fin], arr[index_debut]) 

			index_debut += 1
			count += 1

		else: 
			index_fin -= 1

	index_debut = 0
	index_fin = len(arr) - 1

	#Sort the 1 and the 2s
	while(index_debut < index_fin): 

		if(arr[index_debut] == 0):
			index_debut += 1

		elif(arr[index_fin] == 1): 
			(arr[index_debut],arr[index_fin]) = (arr[index_fin], arr[index_debut]) 

			index_debut += 1

		else: 
			index_fin -= 1
		

	return arr, count




if __name__ == "__main__":

	l = [1, 1, 0, 1, 0]
	l2 = [1, 2, 0, 2, 1, 0, 0]

	#Sort 1s and 0s
	sorted_l, c = sort_01(l)

	print (c)
	print (sorted_l)

	#Sort 2s, 1s and 0s
	sorted_l, c = sort_012(l2)

	print (c)
	print (sorted_l)


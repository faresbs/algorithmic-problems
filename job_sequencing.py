"""
Job sequencing problem
"""


#Solution with O(n^2) using greedy approach
def fn(arr):
	
	# length of array 
    n = len(arr)  


    #Instead od this O(n^2) sort, we can use a merge sort which is O(nlogn)
    # Sort all jobs according to  
    # decreasing order of profit 
    for i in range(n): 
        for j in range(n - 1 - i): 
            if arr[j][2] < arr[j + 1][2]: 
                arr[j], arr[j + 1] = arr[j + 1], arr[j] 


    #Sequence of jobs)
    job = [None] * n

    #Keep track of tasks done in time
    done = [False] * n

    #profit from tasks done in time 
    gain = 0

    # Iterate through all given jobs 
    for i in range(len(arr)): 
  		#Iterate through all the spots
        for j in range(len(arr)): 

        	if job[j] == None: 
	        	job[j] = arr[i][0]
	        	done[i] = True
	        	gain += arr[i][2] 
	        	break
	        else:
	        	break

    # O(n) but dont work sometimes when we have a None at the middle
    #Fill other uncompleted tasks
    """j = n - 1
    for i in range(len(arr) - 1, -1, -1): 
    	if (done[i] == False):
    		job[j] = arr[i][0]
	"""

    # O(n^2)
    #for i in range(len(arr)):
    #	if (done[i] == False):
    #		for j in range(len(job)): 
    #			if (job[j]==None):
    #				job[j] = arr[i][0]
    #				break



    print(done)
    print(job)
    print(gain)


    ############## Solution with a complexity of nlogn ###################

#The idea is to sort according to finish time and use binary search
#you dont need to loop over the sequence n times to find an available spot
#search the wanted spot directly using binary search
#Inspired from here https://www.geeksforgeeks.org/weighted-job-scheduling-log-n-time/


       
def binarySearch(arr, x): 

	low = 0
	high = len(arr) - 1

	# Perform binary Search iteratively
	while low <= high:

		mid = (low + high) // 2

		if(arr[mid] <= x):
			low = mid + 1

		if(arr[mid] >= x):
			high = mid - 1

		if(arr[mid] == x):
			return mid

		

	return None



#Instead of looping over the slots just compare the current one with the associated slot
def fn2(arr):

   	# length of array 
    n = len(arr)  


    #Instead od this O(n^2) sort, we can use a merge sort which is O(nlogn)
    # Sort all jobs according to  
    # decreasing order of profit 
    for i in range(n): 
        for j in range(n - 1 - i): 
            if arr[j][2] < arr[j + 1][2]: 
                arr[j], arr[j + 1] = arr[j + 1], arr[j] 


    #Sequence of jobs
    job = [None] * n

    #Keep track of tasks done in time
    done = [False] * n

    #profit from tasks done in time 
    gain = 0


    # Iterate through all given jobs 
    for i in range(n):
    	if job[arr[i][1] - 1] == None:
    		job[arr[i][1] - 1] = arr[i][0]
    		done[i] = True
    		gain += arr[i][2]
    
    print done
    print job
    	
   	# O(n^2)
    #for i in range(n):
    #	if (done[i] == False):
    #		for j in range(len(job)): 
    #			if (job[j]==None):
    #				job[j] = arr[i][0]
    #				break
    

    # TO FIX
  #  j = 1
 #   for i in range(n):
#
    #	if (done[i] == False and job[j] == None):
    #		job[j] = arr[i][0]
    #	
    #	if (job[j] != None):
    #		j += 1	


def fn3(arr):
	# length of array 
    n = len(arr) 

    #ensemble job wait
    S = []

    for i in range(n): 
        for j in range(n - 1 - i): 
            if arr[j][1] > arr[j + 1][1]: 
                arr[j], arr[j + 1] = arr[j + 1], arr[j] 

    print arr

    #Sequence of jobs
    job = [None] * n

    #profit from tasks done in time 
    gain = 0


    # Iterate through all given jobs 
    for i in range(n):

    	if(len(S) < arr[i][1]):
    		S.append(arr[i])

    	else:
    		for j in range(len(S)-1):
    			c = S[j]
    			if(arr[i][1] > c[j][1]):
    				S[j] = arr[i]




arr = [['a', 2, 100],
       ['b', 1, 60], 
       ['c', 5, 40], 
       ['d', 3, 20], 
       ['e', 3, 20]] 


fn2(arr)
  

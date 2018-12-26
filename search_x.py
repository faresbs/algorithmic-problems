#find x in a sorted list of m that have n finite values at first then infinite values
#find x (finite number) in log n not log m
#We dont know n (number of the finite number)

#Time Complexity is O(logn) not O(log m)
def find(arr, x, L):

	i=1

	#number of finite numbers in the list
	n = 0

	#logn
	while(i < len(a)):

		if(arr[i] == L):
			end = i
			start = i / 2 
			break
		else:
			i = i * 2

	print start 
	print end

	#find the index of the last finite number in the list
	#it takes : 2^k - 2^{k-1} < 2k <= n
	j = start
	for j in range(end):
		if(arr[j]==L):
			n = j - 1
			break

	return n


#Search in the n first elements on the value x in the list using binary search 
#Time complexity O(logn)
def binarySearch (arr, l, r, x): 
  
    if r >= l: 
  
        mid = l + (r - l)/2
  
        if arr[mid] == x: 
            return mid 
          
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 

        else: 
            return binarySearch(arr, mid + 1, r, x) 
  
    else: 

        return -1

#69 is the infinity value
a = [0,1,2,5,6,8,69,69,69,69]
#Value to find
x = 2
print a


#find the first finite number in the list 
index = find(a, x, 69)

#Use the binary search in the array[0:n] section
a = a[0:index]
#logn
print binarySearch (a, 0, len(a)-1, x)
def add(a, b):
	return a+b

# add a substraction function
def subtract(a, b):
	return a-b

# add a division function
def divide(a, b):
	assert (b!=0)
	return a/b

# add a multiplication function
def multiply(a,b):
	return a*b

# add a image of a smile face
def smile():
	print("     000000000     ")
	print("   00         00   ")
	print("  0             0  ")
	print(" 0    00   00    0 ")
	print(" 0               0 ")
	print(" 0    0     0    0 ")
	print("  0    00000    0  ")
	print("   00         00   ")
	print("     000000000     ")

# add the insertion sort function for lists of numbers (increasing order)
def insertion_sort(l):
	N = len(l)
	if(N < 2):
		return
	for i in range(N):
		insertion_value = l[i]
		inserted = False
		for j in range(i-1, -1, -1):
			if(l[j] > insertion_value):
				l[j+1] = l[j]
			else:
				l[j+1] = insertion_value
				inserted = True
				break
		if(not inserted):
			l[0] = insertion_value
	return l

# test suite
def test_suite():
	assert add(1, 2)==3
	assert subtract(2, 1)==1
	assert divide(6, 2)==3
	assert multiply(2,3)==6
	assert insertion_sort([5,4,3,2,1])==[1,2,3,4,5]

	print("passed all tests")
	smile()


#############################
# main function
#############################
if __name__ == "__main__":
	test_suite()

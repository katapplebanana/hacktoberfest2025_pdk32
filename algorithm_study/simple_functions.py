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

# test suite
def test_suite():
	assert add(1, 2)==3
	assert subtract(2, 1)==1
	assert divide(6, 2)==3
	assert multiply(2,3)==6
	print("passed all tests")


#############################
# main function
#############################
if __name__ == "__main__":
	test_suite()

def add(a, b):
	return a+b

# add a substraction function
def subtract(a, b):
	return a-b

# add a division function
def divide(a, b):
	assert (b!=0)
	return a/b

def test_suite():
	assert add(1, 2)==3
	assert subtract(2, 1)==1
	assert divide(6, 2)==3
	print("passed all tests")


if __name__ == "__main__":
	test_suite()

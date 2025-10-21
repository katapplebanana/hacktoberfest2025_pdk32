def add(a, b):
	return a+b

# add a substraction function
def subtract(a, b):
	return a-b

def test_suite():
	assert add(1, 2)==3
	assert subtract(2, 1)==1
	print("passed all tests")


if __name__ == "__main__":
	test_suite()

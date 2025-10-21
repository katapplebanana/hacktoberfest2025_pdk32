def add(a, b):
	return a+b


def test_suite():
	assert add(1, 2)==3
	print("passed all tests")


if __name__ == "__main__":
	test_suite()

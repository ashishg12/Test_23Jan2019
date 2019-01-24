def test_suite():
    for tst, exp in test_inputs.items():
        actual = check_palindrome(tst)
        if actual == exp:
            print("OK")
        else:
            print("NOK")
    """
        This checks if the given input string is a palindrome
        It returns True if the input string is a palindrome
        It returns False if the input string is not a palindrome
    """
def check_palindrome(string):

	if string == string[::-1]:
		return True # to indicate that the input string is a palindrome
	return False
# Main test cases
test_inputs = \
    {
        "radar" : True, # test string : expected status
        "panama" : False,
        "Madman" : False,
        "TCATGAACGTCTTCTGCAAGTACT" : True,
        "GACATACTCCTCCACCTCATACAG" : False,
    }


test_suite() 
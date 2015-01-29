required_age_for_lisence = 18

def person_can_take_test_check():
	print "Test"
def person_can_take_test_check(person_age):
	if person_age >= required_age_for_lisence:
		print "Person is", person_age, "years old, and can take the test."
	else:
		print "Person is", person_age, "years old, and cannot take the test!"	

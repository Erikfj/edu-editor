your_age = input("Type your age: ")

person1_age = 17
person2_age = 18
person3_age = 20

required_age_for_lisence = 18

# Functions will lessen the constraints.

def person_can_take_test_check(person_age):
	if person_age >= required_age_for_lisence and person_age < 80:
		print "Person is", person_age, "years old, and can take the test."
	else:
		print "Person is", person_age, "years old, and cannot take the test!"	

person_can_take_test_check(person1_age)
person_can_take_test_check(person2_age)
person_can_take_test_check(person3_age)

person_can_take_test_check(your_age)



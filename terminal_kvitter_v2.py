kvittr_messages = []
health_bar = 3
menu_index = 0
goto_start_menu = True
adventure_main_menu_index = 0
adventure_menu_index = 0
adventure_school_index = 0
adventure_sub_index = 0
adventure_sub_sub_index = 0
adventure_sub_sub_sub_index = 0
adventure_sub_sub_sub_romance_index = 0


while menu_index != 9:
	print "1. Show all messages"
	print "2. Add new message"
	print "3. Delete a message"
	print "4. Edit message"
	print "5. Show length of message"
	print "9. Exit"
	print "0. Choose Your Own Adventure"
	menu_index = input("What would you like to do?: ")
	if menu_index == 1:
		print kvittr_messages
		print "There are", len(kvittr_messages), "stored messages.: "
	elif menu_index == 2:
		message = raw_input("Type in your message.: ")
		if len(message) > 140:
			print "ERROR: Message not delivered. You can only type 140 characters.: "
		elif len(message) < 5:
			print "ERROR: Message not delivered. You have to type more than 5 characters.: "
		elif "Filip" in message:
			print "ERROR: Message not delivered. This name is holy and subjected to copyright.: "
		else:
			kvittr_messages.append(message)
	elif menu_index == 3:
		for message_index in range(len(kvittr_messages)):
			print message_index, kvittr_messages[message_index]
		message_delete_index = input("Which message do you want to delete?: ")
		del kvittr_messages[message_delete_index]
	elif menu_index == 4:
		for message_index in range(len(kvittr_messages)):
			print message_index, kvittr_messages[message_index]
		message_edit_index = input("Which message do you want to edit?: ")
		new_message = raw_input("Type your replacement message.: ")
		kvittr_messages.insert(message_edit_index, new_message)
		del kvittr_messages[message_edit_index +1]
	elif menu_index == 5:
		for message_index in range(len(kvittr_messages)):
			print message_index, kvittr_messages[message_index]
		message_show_length_index = input("Select to show length.: ")
		print "The message", kvittr_messages[message_index], "is",len(kvittr_messages[message_index]), "characters long.: "
	elif menu_index == 0:
		while adventure_main_menu_index != 9:
			print "Welcome To Choose Your Own Adventure!"
			print "1. START"
			print "9. EXIT"
			
			adventure_main_menu_index = 0
			adventure_menu_index = 0
			adventure_school_index = 0
			adventure_sub_index = 0
			adventure_sub_sub_index = 0
			adventure_sub_sub_sub_index = 0
			adventure_sub_sub_sub_romance_index = 0

			adventure_main_menu_index = input("Press 1 to START the game or 9 to EXIT.: ")
			if adventure_main_menu_index == 1:
				
			elif adventure_main_menu_index == 9:
				break
			else:
				print "Try Again.", adventure_main_menu_index ,"is not a valid number."
		continue
				
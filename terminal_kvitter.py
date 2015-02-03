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
				while adventure_menu_index != 9:
					print "1. The School"
					print "2. The Worn Down Structure"
					print "3. The Lonesome Road"
					print "9. Main Menu / Retry"
					adventure_menu_index = input("You take your first step out of the Vault. You see a worn down structure to the South, a school to the North, a lonesome road to the East. Where do you go?: ")
					if adventure_menu_index == 1:
						while adventure_school_index != 9:
							print "1. You pull your gun and take cover behind a wall"
							print "2. You take a step back and make a run for it"
							print "3. You carry supplies and figure you could barter your way out of the situation"
							print "9. Main Menu / Retry"
							adventure_school_index = input("You enter the school and find it populated by bandits. Your gun is currently holstered, and they have not spotted you yet. How do you proceed?: ")
							if adventure_school_index == 1:
								print "You spot three bandits and can pinpoint a fourth, snooring in between a couple of trash cans. You prepare your weapon and pull the trigger, blowing a hole through the left eye of bandit 1. Bandit 2 and 3 spot you and reach for their weapons, a baseballbat and shotgun. You fire off three more shots, one in the thigh and knee of bandit 3 and miss bandit 2. Bandit 4 is waking up and making a move for a grenade. You concentrate hard and shoot the grenade straight out of bandit 4s hands, blowing half his body off and splitting bandit 2s neck."
								print "You took quite a hit from the explosion and make your way back out of the school and back towards the Vault."
								break
							elif adventure_school_index == 2:
								print "As you turn around and make your way out the door, you trip and crash into a cabinet filled with empty bottles. The sound echos through the hallways. You make a run for it, but before you make it out of sight the bandits spot you and put a bullet in the back of your head. GAME OVER!"
								break
							elif adventure_school_index == 3:
								print "You find your most valuble equipment and make your way through the halls, calmy making the impression that you are unarmed. The bandits take you to their leader and before long they decide to rob and leave you for dead. GAME OVER!"
								break
						break
					elif adventure_menu_index == 2:
						while adventure_sub_index != 9:
							print "1. You tell him you are here on vacation and are looking for someplace to party and hang out."
							print "2. You tell him it's none of his business and to get out of your way."
							print "3. You tell him you are the messiah of old and are here to gather your diciples for the end times."
							print "4. You tell him you are a drifter by trade and come to town looking for work."
							print "9. Main Menu / Retry"
							adventure_sub_index = input("The worn down structure is actually a fortified town. As you approch the gates, a sheriff greets you and wants to know what your business is in town. What do you tell him?: ")
							if adventure_sub_index == 1:
								print "The sheriff tell you to get lost as this is no town for nogoers and lowtimers. You make your way back into the wasteland. GAME OVER!"
								break
							elif adventure_sub_index == 2:
								print "Before the sheriff can reach for his holstered gun, you pull out a knife and slit his throat. The other inhabitants of the city spot you and start firing. You drop dead like a mongoose on a field trip. GAME OVER!"
								break
							elif adventure_sub_index == 3:
								print "The sheriff raises his eyebrow and measure you head to toe. You stare at him with a quizzical look while the sheriff turns and closes the gate behind him. GAME OVER!"
								break
							elif adventure_sub_index == 4:
								while adventure_sub_sub_index != 9:
									print "1. You tell the bartender you will have a beer (1 Cap) and while waiting you lean over and grab some caps from the tip jar."
									print "2. You join the local poker table and get ready for a game of Texas Hold'em."
									print "3. You choose to sit by the bar and try to flirt your way into the heart of the barkeep."
									print "9. Main Menu / Retry"
									adventure_sub_sub_index = input("The sheriff reaches for your hand and accepts you into town for the time being, on the condition of keeping to yourself and keeping out of trouble. You enter the local tavern and spot a beautiful bartender. Approching the bar she tells you a room is 20 Caps and without it you can get lost. You only have 8 Caps. How do you proceed?: ")
									if adventure_sub_sub_index == 1:
										print "A local poker player spots you and before you know it you are thrown the fuck out and told you will never set foot in this town again. GAME OVER!"
										break
									elif adventure_sub_sub_index == 2:
										while adventure_sub_sub_sub_index != 9:
											print "1. You admit defeat and give up while you still have 1 Cap. You were never fond of gambling anyway. "
											print "2. You take a deep breath and call all in, sweating as the tension is rising."
											print "3. You try to cheat your way into a better hand with a spare deck you keep in your wallet."
											print "9. Main Menu / Retry"
											adventure_sub_sub_sub_index = input("After relentless hours of play your down to your last Cap. Now what?: ")
											if adventure_sub_sub_sub_index == 1:
												print "Walking out of the bar with your head hanging down, you spot a crow sitting on a fence. Immediately you are intrigued by the creature, but before you know it the crow grabs your last Cap, sprouts the words Fuck You and fly away. GAME OVER! "
												break
											elif adventure_sub_sub_sub_index == 2:
												print "All players lay their hands on the table and just as the tumbleweeds roll in the wind, you turn your hand revealing the winning deck! You recieve 100 Caps total which will serve you enough bed, drink and company for the rest of the week."
												print "Congratulations! You won!"
												break
											elif adventure_sub_sub_sub_index == 3:
												print "While pretending to check for spare Caps, you pull out a Pair of Queens and play it on the next hand. Unfortunately, no queen will help you now. GAME OVER!"
												break
										break
									elif adventure_sub_sub_index == 3:
										while adventure_sub_sub_sub_romance_index != 9:
											print "1. [Lady Killer] Your earrings are the mirrors which reflect the moonlight into your eyes. Your eyes are as blue as the sea after a storm. And if beauty were time, you'd be an eternity..."
											print "2. [Speech] Ugh! Come hither, for you maketh mine heart boileth with loveth, thou wench."
											print "3. [Low Intelligence] Are those sacks in your pants, or are you just happy to see me? Or wait... was it the other way around?"
											print "4. [Strength] Whoa! Is it just me or did it get a little bit hotter in here? I sure could need someone to lick these abs!"
											print "9. Main Menu / Retry"
											adventure_sub_sub_sub_romance_index = input("You sit by the bar and flirt with the barmaid. After an hour of small talk you muster up courage to seduce her. Which line do you pull?: ")
											if adventure_sub_sub_sub_romance_index == 1:
												print "The barmaid blushes and smiles, seemingly shy as she is not used to poetry reading on her behalf. She offers you a bed to share for the evening and as the sun sets you can finally rest your eyes and relieve yourself of worries."
												print "Congratulations! You won!"
												break
											elif adventure_sub_sub_sub_romance_index == 2:
												print "The barmaid halts and reveals a thin yet wavy mustache on her top lip. Suddenly she spurts out the words... Have at thee! I will heave the gorge on thy livings, naughty mushrump, 'ere i quench thy thirst! GAME OVER!"
												break
											elif adventure_sub_sub_sub_romance_index == 3:
												print "The barmaid laughs at you and lifts her skirt up, revealing a penis. Thank god you are this stupid. GAME OVER! But hey, you could still go for it... If... That's your... Thing?"
												break
											elif adventure_sub_sub_sub_romance_index == 4:
												print "The barmaid stares in disbelief of your ridiculous behavior and tells you to sit down or leave. A single tear crawls out of your eye socket and slides down your face. GAME OVER! "
												break
										break
								break
						break
					elif adventure_menu_index == 3:
						print "You make your way down the road and feel like something is wrong. Out of the bushes jumps three ghouls and drag you back to their crypt, devouring your flesh. GAME OVER!"
						break
			elif adventure_main_menu_index == 9:
				break
			else:
				print "Try Again.", adventure_main_menu_index ,"is not a valid number."
		continue
				
amount = 0
print("Welcome to the bank.")
while(True):
	question = input("What may I help you with? ")
	if(question == "amount"):
		if(amount == 0):
			print("You have no money in your account.")
		elif(amount == 1):
			print("You have", amount, "dollar in your account.")
		else:
			print("You have", amount, "dollars in your account.")
	elif(question == "deposit"):
		dep = int(input("How much money? "))
		if(dep == 1):
			amount += dep
			if(amount == 1):
				print(dep, "dollar has been deposited. You now have", amount, "dollar in your account.")
			else:
				print(dep, "dollar have been deposited. You now have", amount, "dollars in your account.")
		else:
			amount += dep
			if(amount == 1):
				print(dep, "dollars have been deposited. You now have", amount, "dollar in your account.")
			else:
				print(dep, "dollars have been deposited. You now have", amount, "dollars in your account.")
	elif(question == "withdraw"):
		wit = int(input("How much money? "))
		if(wit > amount):
			print("You do not have that much to withdraw.")
		else:
			if(wit == 1):
				amount -= wit
				if(amount == 1):
					print(wit, "dollar has been withdrawn. You now have", amount, "dollar in your account.")
				else:
					print(wit, "dollar have been withdrawn. You now have", amount, "dollars in your account.")
			else:
				amount -= wit
				if(amount == 1):
					print(wit, "dollars has been withdrawn. You now have", amount, "dollar in your account.")
				else:
					print(wit, "dollars have been withdrawn. You now have", amount, "dollars in your account.")
	else:
		print("Thank you for coming to the bank.")
		break
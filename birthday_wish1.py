# This program first converts birthday wish, which is string to ascii and then that ascii to binary

print('Enter the birthday wish you want to encode:')
wish=input()

while True:
	try:
		print('Enter 1 to encode to ASCII and 2 to encode to binary:')
		decision=int(input())
	except ValueError:
		print("Sorry, You can enter numbers and that too only 1 or 2. Try again.")
		continue
	else:
		
		if(decision!=1 and decision!=2): #or will not work here
			continue
		else:	
			break


wish_list=list(wish) #breaks the birthday string into list of characters
ascii_ans_list=[]	 #will store ascii value of each character	
binary_ans_list=[]	 #will store binary value of each character
l=len(wish_list)	 #calculates length of character in the birthday string

def text_to_ascii():
		
	for i in wish_list:
		i=ord(i)
		ascii_ans_list.append(i)

if(decision==1):
	text_to_ascii()
	for p in ascii_ans_list:
		print(p,end='')
	print()			#Inserts a blank line for better formatting
	for p in range(0,l):
		print(str(wish_list[p])+'-->'+str(ascii_ans_list[p]))

elif(decision==2):
	text_to_ascii()
	for i in ascii_ans_list: #building binary list from ascii list
		binary_ans_list.append('{0:08b}'.format(i))
	
	for p in binary_ans_list:
		print(p,end='')
	print()			# for better formatting
	for p in range(0,l):
		print(str(wish_list[p])+'-->'+str(ascii_ans_list[p])+'-->'+str(binary_ans_list[p]))
	


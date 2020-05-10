import random
def password_generator():
	password=""	
	uppercase=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	lowercase=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	symbol=[":","!","\\","*","^",",","@","#","&","?","<",">"]
	number=[1,2,3,4,5,6,7,8,9,0]
	for i in range(12):#now it will choose 12 random loops in everyloop it woll select one character from all those arrays randomly
		var=uppercase
		a=random.randint(1,5)
		if a==1:
			var=uppercase
		elif a==2:
			var=lowercase
		elif a==3:
			var=symbol
		elif a==4:
			var=number
		m=len(var)
		t=random.randint(0,m-1)
		pas=var[t]
		password+=str(pas)
	return password
	
	
print("WELCOME TO PASSWORD GENERATOR")
print("Please select the option:\n (i)Press 1 for LOG IN:\n(ii)Press 2 for new password generation")
n=int(input("please enter your choice: "))
if n==1:
	print("SIGN IN")
	id=input("please enter your id: ")
	passinp=input("please enter your password: ")
	d={}
	with open("id.txt","r") as idmanager:
		for text in idmanager:
			(key,val) = text.split()
			d[key] = val
			pass1=d.get(id)
			if pass1 == passinp:
				print("welcome buddy")
				print("Press 1 for new password generation\nPress 2 for old password retrival")
				inp = int(input("Please enter: "))
				if inp==1:
					social=input("enter the name of the site or app for which you want to generate the password: ")
					inp1=""
					while inp1!="Y":
						password=password_generator()
						print(password)
						y=input("Type Y to select this one of N for another one")
						inp1=y
					print("Your password for" + social + "is" + password )
					n =open(id+".txt" , "a")
					n.write("\n"+social+ " " + password)	
					
				elif inp==2:
					social=input("enter your app/website's name: ")
					retdict={}
					with open(id+".txt","r") as data:
						for lines in data:
							(key,val)=lines.split()
							retdict[key]=val
					print(retdict.get(social))
elif n==2:
	print("SIGN UP")
	id=input("please create a id: ")
	id1=open("id.txt","r+")
	ids=id1.read()
	if not(id in ids):
		pass1 =input("please create your password: ")
		pass2=input("confirm your password: ")
		if pass1==pass2:
			id1.write(id+ " "+ pass2)
			idfile=open(id+".txt" ,"w")
			print("sign up is done")
			
			social = input("enter the social network for which you want to create a password: ")
			inp=""
			while inp!="Y":
				password=password_generator()
				print(password)
				k=input("If you can remeber this password easily press Y else press any key")
				inp=k
			print("Here's your password" + password)
			idfile.write(social + " " + password)
		else:
			print("please signup again again")
	else:
		print("You already have an id please signup")
			
				
			
							
					
	
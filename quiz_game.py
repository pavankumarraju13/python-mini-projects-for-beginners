print("Welcome")
playing=input("Are you interested for playing? ")

if playing!="yes":
     quit()
print("Let's start the game ")  
points=0
answer=input("What does CPU stands for? ")
if answer=="Central Processing Unit".lower() or answer=="Central Processing Unit":
    print("Correct!")
    points+=1
else:
     print("Wrong!")
answer=input("What does gpu stands for? ")
if answer=="Global Processing Unit".lower() or answer=="Global Pprocessing Unit":
    print("Correct!")
    points+=1
else:
     print("Wrong!")
answer=input("What does ROM stands for? ") 
if answer=="Read Only Memory".lower or answer=="Read Only Memory":
    print("Correct!")
    points+=1
else:
     print("Wrong!")
answer=input("What does RAM stands for?")
if answer=="Random Access Memory".lower() or answer=="Random Access Memory":
    print("Correct!")
    points+=1
else:
     print("Wrong!")
     
answer=input("What does IP stands for?").lower()
if answer=="internet protocol" or answer=="Internet Protocol":
    print("Correct!")
    points+=1
else:
     print("Wrong!")    
print("You got",points,"points")
print("You got",points/5*100,"%")
print("Thank you for playing")

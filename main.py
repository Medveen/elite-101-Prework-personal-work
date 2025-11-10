def meddy_store():
  print ("Welcome to Meddy's store!")
  print ("We just opened recently , so our menu is small  but we will add more soon!")

  language= input("Please choose your language/ Choisissez votre langue(English?Francias):").strip().lower()
  if language in ["francais", "french", "fr"]:
    print("\nBienvenue dans la boutique de Meddy!")
    name=input("Comment t'appeles tu ?")
    print("Bonjour"+name+"! Merci d'etre venue!")
    age=input("Quel age as tu ?")

  print("\n Que veux tu faire en premier?:")
  print ("1.Voir le menu")
  print ("2. Poser une questiom")
  print ("3.Donner un avis")
  print ("4.Quitter")

  choice_in_between = input ("Choisis une option parmi les quatres suivantes:")

  if choice_in_between =="1":
    print("\nMenu du jour:")
    print ("1.Chips- 1,50$")
    print ("2. Boissonss- 1,50$")
    print ("3.Bonbons-2$")

    need= input("\nQu'est ce que tu aimerais acheter?")
    print(f"Tres bien, {name}! Nous allons te preparer des {need}")
    print("Merci d'avoir visiter notre boutique! De nouveaux produits arrivent bientot!")
  
  elif choice_in_between =="2":
     question= input("nPose  ta question")
     print ("Merci pour ta question, notre equipe te repondra bientot!!")
  elif choice_in_between==3:
     feedback= input ("Quelle est  ton avis sur cette boutique?")
     print (""Merci pour ton avis , ca nous aide a nous ameliorer")
            
  else:
  print ("Merci d avoir visiter notre Boutique ! a bientot!")
   
else:
 print("\nWelcome to Meddy's store!")
 name= input("What is your name?")
 print(f"Hello, " + name + "! Thank you for coming here!")
 age= input ("How old are you?")


print ("\nWhat would you like to do?")
print ("1.View our menu")
print ("2. Ask a question")
print ("3.Leave feedback")
print (4."Exit")

choice_in_between= input ("Choose an option:")
 if choice_in_between =="1":
    print("\nMenu of the day:")
    print ("1.Chips- 1,50$")
    print ("2. Drinks- 1,50$")
    print ("3.Candy-2$")

    need= input("Great, what would you like to buy today?.")


    print("Great choice, "+ name +" We'll get you some" + need + ".")

    print("Thank you for shopping at Meddy's store !new product are on their way") 
  
  elif choice_in_between =="2":
     question= input("nAsk your question")
     print ("Thanks for the question, we'll answer you soon !!")
  elif choice_in_between==3:
     feedback= input ("Please share your feedback with us :?")
     print (""Thanks for your feedback , it helps us grow")
            
  else:
  print ("Thank you for shopping at Meddy's store ! Come see us again")
   
meddy_store()
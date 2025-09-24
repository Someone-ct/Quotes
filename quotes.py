print("This program will give you a quote about any\ncategory you like.")
print("Just choose one of these categories:")
print("Note 1 : There will be more categories in the next updates, maybe.")
print("Note 2 : This program requires an internet connection to work properly.")
print("You don't need to write the whole word, just the number.")
print("\n[1] Life\n[2] Love\n[3] Science\n")
def inpt() :
    global choice
    choice = input("Choose a Number ==> ")
    return choice
def error() :
        print("You Did Not Choose number !\nDont write <" + str(choice) + "> or any Letters\nJust NUMBERS")
while True :
  choice = inpt()
  try :
    choice = float(choice)
  except ValueError :
    error()
    continue
  if not choice.is_integer():
    print("Dont Choose number with(,)like : 1.5 ; 2.3 ...")
    continue
  elif choice not in (1,2,3) :
     print("You Did Not Choose The right number!\njust choose 1 or 2 or 3")
     continue
  else :
     break
import requests
import random
if choice == 1 :
    url = requests.get ("https://zenquotes.io/api/quotes/life")
    respond1 = url.json()
    quote = random.choice(respond1)
    print("Here your quote : \n")
    print("==> : " + quote["q"])
    print("\n")
    print("--" + quote["a"])
    print("age : " + quote["c"])
elif choice == 2 :
    url = requests.get ("https://zenquotes.io/api/quotes/love")
    respond1 = url.json()
    quote = random.choice(respond1)
    print("Here your quote : \n")
    print("==> : " + quote["q"])
    print("\n")
    print("--" + quote["a"])
    print("age : " + quote["c"])
elif choice == 3 :
    url = requests.get ("https://zenquotes.io/api/quotes/science")
    respond1 = url.json()
    quote = random.choice(respond1)
    print("Here your quote : \n")
    print("==> : " + quote["q"])
    print("\n")
    print("--" + quote["a"])
    print("age : " + quote["c"])
    
    



     


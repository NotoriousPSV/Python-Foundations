'''
This project will be a currency converter, with a twist! It will be a semi-story game, with aspects of currency exchange. 

This project is to primarily speed up my learning for python, and I will be using functions. Yay!!

So, yeah!
'''
#Introduction
print("Hello! You are the newest employee in the currency exchange department. Yay! You will be sooo good, I can already feel it!")
print("\nLet me give you the rundown on this place, your main job is to help people exchange their currency, but you can get into a little forex trading if you want.") 
print("\nJust don't trade using insider info, that's a big no no.")
print("\nDepending on different events, the price of the currency will either rise or fall.") 
print("\nYou want to buy low and sell high if you go long, and sell high and buy low if you short.")
print("\nCertain clients may ask for advice along the way, though they should likely be seeking advice from others.") 
print("\nNevertheless, it's in your best interest to give them good advice, because you get 10 percent of their profits from their trade. ")
print("\nAt times, certain goverment officials may come towards you. Don't be scared! They can on slim occasions be nice. ")
print("\nYour goal is to keep a profit, if you have too much debt, you could be thrown in jail for tax evasion. ")
print("\nThat concludes the tutorial! If you have any questions, go to the menu and find the FAQs area to see if your queries can be answered. ")

#Establish Converting Mechanism

def convert_HL(a, b):
    return a * b 
def convert_LH(a, b):
    return a/b


#Menu UI
while True:
    menu_ques = input("What would you like to do? \nCurrency Trade Yourself (Trade Yourself)?\nHelp Customers (Help Customers)?\nQuestions (FAQs)?")
    menu_ques = menu_ques.lower()
    if menu_ques == "trade yourself":
        print("H")
    elif menu_ques == "help customers":
        print("F")




print("""
------ this is all iteam which is available on our shop ------
samosa - 15
tea - 12
black tea - 10
vada pav - 20
""")

dic={'samosa':15,'tea':12,'black tea':10, 'vada pav': 20}
order_price = 0

like_to_order =input("\n would you like to order something ? yes/no : ")

if(like_to_order == 'yes'or like_to_order=='y'):
    order = input("\n please enter your order : ")

    if(order =='samosa' or order =='SAMOSA' or order =='Samosa'):
        order_price = order_price+dic[order]     # -- taking price from the dictionary and adding
        print("\n *** thank you sir, your Order received *** ")

    elif(order =='tea' or order =='TEA' or order =='Tea'):
        order_price = order_price+dic[order]
        print("\n *** thank you sir, your Order received *** ")

    elif(order == 'Black tea' or order =='BLACK TEA' or order == 'black tea'):
        order_price = order_price + dic[order]
        print("\n *** thank you sir, your Order received *** ")

    elif(order == 'voda pav' or order =='VODA PAV' or order =='Voda pav'):
        order_price = order_price + dic[order]
        print("\n *** thank you sir, your Order received *** ")
    else:
        print(" \n--- sorry, asked order not in the list of the menu ! -----")

    # inner if else end here


    like_to_order_again = input("\n would you like to order more  ? yes/no : ")
    if(like_to_order_again == 'yes' or like_to_order_again == 'y' or like_to_order_again == 'YES'):
        order_again = input("\n please enter your order : ")

        order_price = order_price + dic[order_again]
        print("\n *** thank you, your Order received *** ")

    elif(like_to_order_again == 'n' or like_to_order_again == 'no' or like_to_order_again == 'N'):
        print(" \n------ ok no issue sir, have your order sir ! ------")
    else:
        print(" \n------ sorry sir i can't understand you so skip that question, god day sir ! ------")


    print(f"\n Sir your Total bill is  : {order_price}")
    print("\n\n ---------- thank your sir please come again -------------")

else:
    print(" \n------ ok sir, no problem have a good day ! -------- ")

    # outer if else end here




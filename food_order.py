

print("*********** this is order system program ********************** \n")

print("""
------ this is all iteam which is available on our shop ------
samosa - 15
tea - 12
black tea - 10
vada pav - 20

""")
list=[]
dic={'samosa':15,'tea':12,'black tea':10, 'vada pav': 20}
total = 0
confirm = input("would you like to order some food ?  yes/no: ")
if(confirm == 'yes'):

    def order_func():
        order = input("please enter your order name : ")
        if(order =='samosa'):
            print(f"your order {order} is added. thank for your order")
            b= dic.get('samosa')
            list.append(b)
        elif (order == 'tea'):
            print(f"your order {order} is added. thank for your order")
            b = dic.get('tea')
            list.append(b)
        elif (order == 'black tea'):
            print(f"your order {order} is added. thank for your order")
            b = dic.get('black tea')
            list.append(b)
        elif (order == 'vada pav'):
            print(f"your order {order} is added. thank for your order")
            b = dic.get('vada pav')
            list.append(b)
        else:
            print("that food is not in the list ")
    order_func()
    again=input("would you like to add another order ? yes/no :")
    if(again=='yes'):
        order_func()
    else:
        print("thank you .....")

    for i in list:
        a = int(i)
        total = total+ a
    print(f"your total bill is : {total}")
else:
    print("thank you for your time ")
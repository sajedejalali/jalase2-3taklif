name = input("enter your name : ")
family = input("enter your family : ") 

season1 = float(input("enter your 1.season score : "))
season2 = float(input("enter your 2.season score : "))
season3 = float(input("enter your 3.season score : "))

average = (season1 + season2 + season3)/3

if average >= 17 :
    print("your score is greate" )

if average >=12 :
    if average >= 17:
        print( " ")
    else:
        print("your score is normal" )
    

if average < 12 :
    print("your score is fail" )

import random
user=1000
computer=1000
ans= "y"
while ans==("y"):
    print('Guest the number is 1 or 0', end="")
    num=int(input())
    print('Enter the amount of money ')
    m=int(input())
    com=random.randint(0,1)
    print('You r ', num)
    print('Computer is ', com)
    if num==1 and com==0:
        print('You win')
        user=user+m
        computer=computer-m
    elif num==1 and com==1:
        print('Draw')
    else :
        print('You lose')
        user=user-m
        computer=computer+m
    print('You have ', user)
    print('Computer have ', computer)
    if user<0 or computer<0:
        ans='n'
    else:
        print('Try Again(y/n)')
        ans=input()
    if user<=0:
        print('You have no chance')
        print('Do you take some lone?(y/n)')
    for i in range(3):
        i=input()
        if i=='y':
            print("You have 3 chance") 
            print("Enter the amount that you want to borrow from Computer")
            amount=int(input())
            user=user+amount             
        
    else:
        if computer<=0:
            print('You are the winner')
            
    

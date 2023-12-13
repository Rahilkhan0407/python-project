#!/usr/bin/env python
# coding: utf-8

# # Budget game

# In[1]:


def budget_game():
    #mumbai bot
    #user welcome
    print('welcome to mumbai! The city of Dreams')
    #user bhai tera name bata
    user_name=input('please enter your name:')
    #greeting kardo
    print('Hello',user_name.title())
    #budget kya hai?
    budget=int(input('enter your budget here:'))
    #1000> ola se ja
    if budget>=1000:
        print('ola se jaa')
    #500-1000 auto se jaa
    elif budget>=500 and budget<1000:
        print ('auto se jaa')
    #100-500 bus se jaa                 
    elif budget >=100 and budget<500:
        print ('bus se jaa')
    #10-100 train se jaa                 
    elif budget>=10 and budget<100:
        print('train se jaa')
    else:
        print ('ghar pe ja')


# # Heads and tails

# In[2]:


def heads_tails():
    #coin game 
    #welcome aser
    print('welcome to the world of chance!')
    #Take input from user
    user_input=input('enter heads of tails')
    #display user input
    print('you choose:',user_input.title())
    #coin toss
    import random
    if random.choice('ht')=='h':
        coin_toss='heads'
    else:
        coin_toss='tails'
    #display coin toss
    print('coin Result:',coin_toss.title())
    #compare user input==coin toss
    if user_input.lower()==coin_toss.lower():
        print('you wins!')
    else:
        print('you lose!')



# #  Dice game

# In[3]:


def dice_game():
    #dice game
    #welcome to dice game
    print('welcome to dice game!')
    #take the input form user
    user_input=input('enter the number 1to6:')
    #display the number you choose
    print('you choose',user_input.title())
    import random 
    dice_result=random.choice('123456')
    print('dice_result',dice_result)
    if dice_result==user_input:
        print('you win')
    else:
        print('you loss')


# # Table game

# In[4]:


def table_game ():
    print('welcome to the worlds of table')
    user_input=int(input ('enter the number'))
    print('you choose',user_input)
    for a in range (1,11):
        print(user_input,'*',a,'=',user_input*a)


# # Factorial game

# In[5]:


def factorial_game():
    print ('welcome to the factorial game')
    user_input=int(input('enter the number'))
    fact=1
    for i in range(1,user_input+1):
        fact=fact*i
    print("factorail number is:",fact)


# # fibonachi number

# In[6]:


def fibonachi_number ():
    print('fibonachi number')
    #enter the number 
    user_input=int(input('enter the number'))
    #if the number is equal to 0
    x=0
    #the number is equal to 1
    y=1
    #the number is equal to 0
    z=0
    #taken number is greater tham equal to user input
    while z<=user_input:
        print(z)
        x=y
        y=z
        z=x+y


# # password generator

# In[7]:


def password_generator():
    print('password generator')
    import random
    lower='abcdefghijklmnopqrstuvwxyz'
    uper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num='1234567890'
    char='!@#$%^&*'
    choose_from_password=lower+uper+num+char
    user_input=int(input('enter number of password here:'))
    for i in range (1,user_input+1):
        print(random.choice(choose_from_password),end='')


# # countdown timer

# In[8]:


def countdown_timer():
    user_input=int(input('please enter in min'))
    user_input2=int(input('please enter in sec'))
    from countdown import countdown
    countdown (mins=user_input,secs=user_input2)


# # cude wolrd

# In[9]:


def cube_wolrd():
    print('welcome to the cube wolrd')
    user_input=int(input('enter the number'))
    for i in range(1,user_input+1):
        print(i,'cube','=',i**3)


# In[ ]:





# In[29]:


import tkinter as tk
window=tk.Tk()
window.title('python project')
window.geometry('500x500')
tk.Label(window,text='Python Project',font=('Helvetica',28)).place(x=130,y=30)
tk.Label(window,text='Rahil Khan',font=('Helvetica',16)).place(x=200,y=80)
tk.Button(window,text='Heads and tails',height=2,width=15,command=heads_tails).place(x=40,y=130)
tk.Button(window,text='Budget game',height=2,width=15,command=budget_game).place(x=200,y=130)
tk.Button(window,text='Dice game',height=2,width=15,command=dice_game).place(x=350,y=130)
tk.Button(window,text='Table game',height=2,width=15,command=table_game).place(x=40,y=200)
tk.Button(window,text='Factorial game',height=2,width=15,command=factorial_game).place(x=200,y=200)
tk.Button(window,text='fibonachi number',height=2,width=15,command=fibonachi_number).place(x=350,y=200)
tk.Button(window,text='password generator',height=2,width=15,command=password_generator).place(x=40,y=280)
tk.Button(window,text='countdown timer',height=2,width=15,command=countdown_timer).place(x=200,y=280)
tk.Button(window,text='cude wolrd',height=2,width=15,command=cube_wolrd).place(x=350,y=280)
window.mainloop()


# In[ ]:





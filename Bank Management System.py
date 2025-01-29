# Bank Management System
# BY <<<<< Ajay >>>>>>


import pandas as pd
import numpy as np
import sys
import random


df=pd.read_csv("E:/Documents/Account_Details.csv",index_col="sno.")#location of csv file in system
df2=df.to_csv("E:/Documents/User_Names.csv", columns=['name'])


def fetchcsv():
    print(pd.read_csv("E:/Documents/Account_Details.csv",index_col="sno."))
    

def writecsv(df):
    df.to_csv("E:/Documents/Account_Details.csv",na_rep="NULL\n")
    q=input("PRESS ENTER TO SHOW MODIFIED TABLE:\n")
    fetchcsv()
    

print(".................................................")


def menu() :    
    print("\n______________________________________________________________________\n")
    print("               <<<<<<   BANK  MANAGEMENT   >>>>>>                        ")
    print("______________________________________________________________________\n")
    print("          0. ABOUT PROJECT              \n")
    print("          1. SHOW EXISTING ACCOUNTS     \n")
    print("          2. ADD A NEW ACCOUNT          \n")
    print("          3. DEPOSIT CASH               \n")
    print("          4. WITHDRAW CASH              \n")
    print("          5.CHECK BALANCE               \n")
    print("          6.DELETE ACCOUNT              \n")
    print("          7. EXIT                         ")
    print()

    
print("LOADING........\n")
print("        *******  WELCOME TO SBI   *******       \n")
print("               +-----------------+                ")
print("               |    LOGIN PAGE   |                ")
print("               +-----------------+              \n")
      

print('''NOTE: use your FIRST NAME AS USERNAME and 
PASSWORD IS 1234 ''')


X=input("ENTER YOUR USERNAME :")

Y=int(input("ENTER YOU PASSWORD :"))

print("LOADING......\n")
print("HELLO,",X,'\n')
m=input("PRESS ENTER TO GO IN MENU:")


menu()  #menu will printed


print("___________________________________________________________________________")
print("___________________________________________________________________________")



def about() :
    print()
    print("THIS PROJECT IS ABOUT BANK MANAGEMENT SYSTEM\n")
    print("USING PYTHON AND CSV FILE\n")
    print("IN THIS PROJECT THERE ARE 2 CSV FILE AND 7 OPTION\n")
    print("THANK YOU\n")
    

    

def add_acc():
    print(pd.read_csv("E:/Documents/Account_Details.csv",index_col="sno."))
    sno=int(input("ENTER S.NO:"))
    name=input("ENTER YOUR NAME:")
    age=input("ENTER YOUR AGE:")
    acc_no=random.randint(100000,999999)
    print()
    print("ENTER YOUR GENDER AS (M),(F),(O)")
    gender=input("ENTER YOUR GENDER:")
    bal=int(input('ENTER THE AMOUNT YOU WANT TO DEPOSIT:'))
    df.loc[sno,:] = [name,age,acc_no,gender,bal,]
    writecsv(df)
    


def dep():     #DEPOSIT OF CASH
    fetchcsv()
    sno=int(input("ENTER YOUR SERIAL NUMBER :"))
    balance=int(input("ENTER YOUR CURRENT BALANCE:"))
    m=int(input("ENTER AMOUNT TO DEPOSIT : "))
    rows_to_update = [sno]
    cols_to_update = ['balance']
    values = [balance+m,'\n']
    print("SUBMIT YOUR CASH OR CHEQUE\n")
    print("CASH SUBMITTED\n")
    print("LOADING......\n")
    print("YOUR BALANCE IS UPDATED :\n")
    L=input("PRESS ENTER to SHOW YOUR BALANCE:\n")
    g=df.loc[rows_to_update, cols_to_update] = values
    print(df)
    




    
def wc(): #WITHDRAWL OF CASH
    fetchcsv()
    sno=int(input("ENTER YOUR SERIAL NO.:"))
    balance=int(input("ENTER YOUR CURRENT BALANCE:"))
    m=int(input("ENTER THE AMOUNT YOU WANT TO WITHDRAW:"))
    rows_to_update = [sno]
    cols_to_update = ['balance']
    values = [balance-m,'\n']
    print("LOADING......\n")
    print("COLLECT YOUR CASH",m,'\n')
    print("YOUR BALANCE IS UPDATED :\n")
    L=input("PRESS ENTER to SHOW YOUR BALANCE:\n")
    g=df.loc[rows_to_update, cols_to_update] = values
    print(df)
    




def cb():  #CHECK BALANCE AND DETAILS
    #second csv file 
    print(pd.read_csv("E:/Documents/User_Names.csv",index_col=0),'\n')
    sno=int(input("ENTER YOUR SERIAL NUMBER (sno.):"),'\n')
    print("YOUR ACCOUNT DETAIL IS :\n")
    detail=df.loc[sno,:]
    print(detail)
    print("THANK YOU")
    


def da():#DELETE ACCOUNT
    print("FOR DELETING ACCOUNT ")
    fetchcsv()
    df=pd.read_csv("E:/Documents/Account_Details.csv",index_col="account no.")
    acc=int(input("ENTER YOUR ACCIOUNT NUMBER:"))
    df.drop(acc,axis=0,inplace=True)
    print("DELETING ACOOUNT PLEASE WAIT....\n")
    print("ACCOUNT DELETED :\n")
    VV=input("PRESS ENTER TO SHOW NEW TABLE\n")
    print(df)
    



inp=int(input("ENTER YOUR CHOICE :"))
if inp==0:
    about()
    '''print("FIRST CSV FILE:")
    print()
    fetchcsv()
    print()
    print()
    print("SECOND CSV FILE:")
    print()
    print(pd.read_csv("E:/Documents/User_Names.csv",index_col=0))
    print()'''

    
elif inp==1:
    print("EXISTING ACCOUNTS DETAILS ARE:\n")
    fetchcsv()
    print()

    
elif inp==2:
    add_acc()

    
elif inp==3:
    dep()

    
elif inp==4:
    wc()

    
elif inp==5:
    cb()

    
elif inp==6:
    da()

    
elif inp==7:
    sys.exit

    
else:
    print("WRONG INPUT ...")
    print("PLEASE RESTART THE PROGRAMME")




    

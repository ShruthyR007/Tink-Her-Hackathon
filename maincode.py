import mysql.connector as mys
import matplotlib.pyplot as plt
mycon=mys.connect(host="localhost",user="root",passwd="root")
mycursor=mycon.cursor()
mycursor.execute("if not exists create database userdb;")
mycursor.execute("use userdb;")
mycursor.execute("create table if not exists user(user_id varchar(30) unique, pw varchar(30),allowance int(10),exp_rec int(10),bal int(10),budget int(10),food int(10) default 0,groceries int(10) default 0,transport int(10) default 0,misc int(10) default 0,tot_expense int(10) default 0,week_expense int(10) default 0,entry int(10) default 0);")


while True:
    ch=input("1.User\n2.Admin\n3.Exit\nEnter Choice:")
    if ch=="1":           
           a=input("1.New User\n2.Existing User\nEnter Choice:")
           if a== "1":
               uid=input("Create User ID:")
               mycursor.execute("select user_id from user")
               rec=mycursor.fetchall()
               lst=[]
               for row in rec:
                   for i in row:
                       lst.append(i)
               if uid not in lst:
                   pw=input("Create password:")
                   al=int(input("Enter Monthly Allowance:"))
                   rec=int(input("Enter Recurring Expenses:"))
                   bal=al-rec
                   budget=int(input("Enter weekly budget goal:"))
                   query="insert into user(User_id,pw,allowance,exp_rec,bal,budget)values('{}','{}',{},{},{},{});".format(uid,pw,al,rec,bal,budget)
                   mycursor.execute(query)
                   mycon.commit()
               else:                   
                   print("Username already taken try again")                                                           
           elif a=="2":
               od=input("Enter user id:")
               pw=input("Enter password:")            
               def login():                    
                    mycursor.execute("Select * from user where user_id=%s and pw=%s;",(od,pw))
                    user=mycursor.fetchall()
                    if user:
                        return True
                    else:
                        return False
               if login()!=True:
                    print("Invalid credentials")
                    
               else:
                   print("Login succesful")
                   mycursor.execute("Select entry from user where user_id='{}';".format(od))
                   cou=mycursor.fetchall()
                   couu=0
                   for row in cou:
                       for i in row:
                           couu=couu+i
                   
                    
                   while True:
                       mycursor.execute("Select week_expense from user where user_id='{}';".format(od))
                       eh=mycursor.fetchall()
                       ehh=0
                       for row in eh:
                           for i in row:
                               ehh=ehh+i
                       mycursor.execute("Select budget from user where user_id='{}';".format(od))
                       bu=mycursor.fetchall()
                       buu=0
                       for row in bu:
                           for i in row:
                               buu=buu+i
                       bud=0.9*buu
                       if ehh>buu:
                           print("You have exceeded your weekly budget goals")
                       elif ehh>=bud:
                           print("You are near your weekly budget")

                           
                       ch=input("1.Update daily expenses\n2.Update allowance\n3.Update recurring expenses\n4.View graphical interface\n5.Edit weekly budget\n6.View Balance\n7.log out\n8.Exit\nEnter Choice:")
                       if ch=="1":
                            couu=couu+1
                            mycursor.execute("update user set entry=%s where user_id=%s;",(couu,od))
                            if couu%7==0:
                                mycursor.execute("update user set week_expense=0 where user_id=%s;",(od,))
                                mycon.commit()
                            food=int(input("Enter todays expenditure in food:"))
                            transport=int(input("Enter today's expenditure in transport:"))
                            groc=int(input("Enter today's expenditure in groceries:"))
                            misc=int(input("Enter today's miscellaneous expenses:"))
                            mycursor.execute("Select food from user where user_id='{}';".format(od))
                            c=mycursor.fetchall()
                           
                            s=0
                            for row in c:
                                for i in row:
                                    s=s+i
                            b=s+food
                            print("Your current total expenditure in food is",b)
                            mycursor.execute("Select transport from user where user_id='{}';".format(od))
                            d=mycursor.fetchall()
                            e=0
                            for row in d:
                                for i in row:
                                    e=e+i
                            f=e+transport
                            print("Your current total expenditure in transport is",f)
                            mycursor.execute("Select groceries from user where user_id='{}';".format(od))
                            g=mycursor.fetchall()
                            h=0
                            for row in g:
                                for i in row:
                                    h=h+i
                            j=h+groc
                            print("Your current total expenditure in groceries is",j)
                            mycursor.execute("Select misc from user where user_id='{}';".format(od))
                            k=mycursor.fetchall()
                            l=0
                            for row in k:
                                for i in row:
                                    l=l+i
                            m=l+misc
                            print("Your current total miscellaneous expenses is",m)
                            mycursor.execute("Select tot_expense from user where user_id='{}';".format(od))
                            p=mycursor.fetchall()
                            n=0
                            for row in p:
                                for i in row:
                                    n=n+i
                            o=n+misc+food+transport+groc
                            mycursor.execute("Select bal from user where user_id='{}';".format(od))
                            qe=mycursor.fetchall()
                            r=0
                            for row in qe:
                                for i in row:
                                    r=r+i
                            s=r-(misc+food+transport+groc)
                            mycursor.execute("Select week_expense from user where user_id='{}';".format(od))
                            t=mycursor.fetchall()
                            u=0
                            for row in t:
                                for i in row:
                                    u=u+i
                            weekk=u+food+transport+groc+misc
                            mycursor.execute("UPDATE user SET food=%s, groceries=%s, transport=%s, misc=%s, tot_expense=%s, bal=%s,week_expense=%s where user_id=%s;", (b, j, f, m, o, s, weekk, od))
                            mycon.commit()
                       elif ch=="2":
                            new_all=int(input("Enter new value for allowance"))
                            
                            mycursor.execute("Select exp_rec from user where user_id='{}';".format(od))
                            ba=mycursor.fetchall()
                            baa=0
                            for row in ba:
                                for i in row:
                                    baa=baa+i
                            baal=new_all-baa
                            mycursor.execute("Select tot_expense from user where user_id='{}';".format(od))
                            ac=mycursor.fetchall()
                            acc=0
                            for row in ac:
                                for i in row:
                                    acc=acc+i
                            ball=baal-acc
                            mycursor.execute("update user set allowance=%s,bal=%s where user_id=%s;",(new_all,ball,od))
                            mycon.commit()
                            print("Successfully updated")
                       elif ch=="3":
                            new_rec=int(input("Enter new value for recurring expense"))
                            mycursor.execute("Select allowance from user where user_id='{}';".format(od))
                            ba=mycursor.fetchall()
                            baa=0
                            for row in ba:
                                for i in row:
                                    baa=baa+i
                            baal=new_all-baa
                            mycursor.execute("Select tot_expense from user where user_id='{}';".format(od))
                            ac=mycursor.fetchall()
                            acc=0
                            for row in ac:
                                for i in row:
                                    acc=acc+i
                            ball=baal-acc
                            mycursor.execute("update user set exp_rec=%s,bal=%s where user_id=%s;",(new_rec,ball,od))
                            mycon.commit()
                            print("Successfully updated")
                       elif ch=="4":
                            mycursor.execute("Select food from user where user_id='{}';".format(od))
                            c=mycursor.fetchall()
                            s=0
                            for row in c:
                                for i in row:
                                    s=s+i
                            mycursor.execute("Select transport from user where user_id='{}';".format(od))
                            d=mycursor.fetchall()
                            e=0
                            for row in d:
                                for i in row:
                                    e=e+i
                            mycursor.execute("Select groceries from user where user_id='{}';".format(od))
                            g=mycursor.fetchall()
                            h=0
                            for row in g:
                                for i in row:
                                    h=h+i
                            mycursor.execute("Select misc from user where user_id='{}';".format(od))
                            k=mycursor.fetchall()
                            l=0
                            for row in k:
                                for i in row:
                                    l=l+i
                            mycursor.execute("Select tot_expense from user where user_id='{}';".format(od))
                            p=mycursor.fetchall()
                            n=0
                            for row in p:
                                for i in row:
                                    n=n+i
                                    
                            per_food=s/n*100
                            per_tran=e/n*100
                            per_groc=h/n*100
                            per_misc=l/n*100
                             
                            sizes = [per_food, per_tran, per_groc, per_misc]
                            names = ['Food', 'Transport', 'Groceries', 'Miscellaneous expenses']
                            colours = ['gold', 'lightblue', 'lightcoral', 'yellowgreen']
                            plt.pie(sizes,labels=names,colors=colours,autopct='%1.1f%%',shadow=True,)
                            plt.title("Pie Chart Example")
                            plt.show()
                       elif ch=="5":
                            new_week=int(input("Enter new value for weekly budget"))
                            mycursor.execute("update user set budget=%s where user_id=%s;",(new_week,od))
                            mycon.commit()
                            print("Successfully updated")
                       elif ch=="6":
                            mycursor.execute("select bal from user where user_id=%s;",(od,))
                            bala=mycursor.fetchall()
                            for row in bala:
                                for i in row:
                                    print("Balance is:",i)
                       elif ch=="7":
                            cho=input("Do you really want to log out? (yes or no):")
                            if cho.lower()=="yes":
                                mycursor.execute("delete from user where user_id=%s;",(od,))
                                mycon.commit()
                       elif ch=="8":
                            break
    elif ch=="2":
        while True:
            od=input("Enter user id:")
            pw=input("Enter password:")            
            def login():                    
                 mycursor.execute("Select * from user where user_id=%s and pw=%s;",(od,pw))
                 user=mycursor.fetchall()
                 if user:
                     return True
                 else:
                     return False
            if login()!=True:
                
                print("Invalid credentials")
                    
            else:
                print("Login succesful")
                a=input("Do you want to delete any user (yes or no):")
                if a.lower()=="yes":
                    uid=input("Enter id of user who is to be removed:")
                    mycursor.execute("delete from user where user_id=%s;",(uid,))
                    mycon.commit()
                else:
                    break
    elif ch=="3":
        break
    
    
                            
                            
                
                            
               
                
                   
              
                    
                
              
                           
                       

               
            
          
              
            
               
    
         
           
                 

import mysql.connector


connection = mysql.connector.connect(user = 'person',database='database',password='thenuka2007#')

cursor = connection.cursor()


def view():
    userId = input("Enter account userId: ")
    cursor.execute("SELECT * FROM userinfo where personId= '"+ userId +"'")
    for i in cursor:
        print(i)


def deposit():
    money = 0
   
    num = int(input("Enter account num: "))
    deposits = int(input("Enter your deposits: "))
    money = deposits
    insert = "INSERT INTO deposit (money, deposit,userId)VALUES(%s, %s,%s)"
    val = (money, deposits,num)
    cursor.execute(insert,val)
    n = "SELECT userinfo.personId, deposit.deposit FROM userinfo INNER JOIN  deposit ON userinfo.personId = deposit.userId;"  
    cursor.execute(n) 
    result = cursor.fetchall()
    cursor.execute("SELECT SUM(deposit) FROM deposit")
    print("Current balance")
    print(cursor.fetchall()[[0][0]])
    connection.commit()

def table():
    username = int(input("put your id: "))
    first = input("what is your firstname: ")
    insert = "INSERT INTO userinfo (personId, firstname) VALUES (%s,%s)"
    val = (username,first)
    cursor.execute(insert,val)
    connection.commit()
    cursor.close()
    connection.close()

def login():
    #function allows users to login to the bank
    count = 0
    while True: 
        select = "SELECT * FROM userinfo WHERE personId= %s"
        user = int(input("What is your userId: "))
        cursor.execute(select, (user, ))
        if cursor.fetchall():
            print("Successfully logged in")
            break
        else:
            print("Invalid")
            break
    main()
def main():
    while True:
        print("""
            1. Deposit
            2. Create
            3. View
            4. end
          
            
            """)
        choice = int(input("choose: "))
        if choice == 1:
            deposit()
        elif choice == 2:
            table()
        elif choice == 3:
            view()
        else:
            print("Thanks for going to Bank")
            break

choice = input("If you have an account press 1 if you don't press any other key")
if choice == "1":
    login()
else:
    table()
    

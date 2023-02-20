import pyodbc
import datetime

# opening the database (locally)
conn_str = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=C:\Users\Tim Na\Pictures\DB\My-Beautiful-Code\ChildhoodCare.accdb;'
            r'Trusted_Connection=yes;')
conn = pyodbc.connect(conn_str)

# opening the table within the DB
cursor = conn.cursor()
cursor.execute('SELECT * FROM Child')

# admin stuff
for i in cursor:
    print(i)


def dropoff():
    # user inputs child's first and last name
    childperson = input("What is the child's first name?: ")
    childLast = input("What is the child's last name?: ")
    guardianPhone = input("Phone Number: ")
    guardianName = input("Guardian's Full Name: ")

    # finds and records current hour
    current_time = datetime.datetime.now()
    current_hour = int(current_time.strftime("%H"))

    cursor.execute(f"INSERT INTO Child (firstname, lastname, checkinhour, guardianfullname, guardianphone) "
                   f"VALUES ('{childperson}', '{childLast}', {current_hour}, '{guardianName}', '{guardianPhone}');")
    print("Thanks!")
    conn.commit()


def pickup():
    # user inputs child's first and last name
    childperson = input("First Name: ")
    childLast = input("Last Name: ")
    guardianPhone = input("Phone Number: ")

    # searches for the child using the criteria (WHERE FIRSTNAME= ___ AND LASTNAME= ___ etc.)
    cursor.execute(f"select * from Child where firstName='{childperson}' and lastName='{childLast}' and guardianPhone='{guardianPhone}';")
    cost_per_hour = 12
    one_row = cursor.fetchone()
    current_time = datetime.datetime.now()  # finds the current time
    # adds the current hour and minute(div by 60) and subtracts that by the hour of when the child was dropped off then multiplying by the cost per hour.
    cost = round((float(current_time.strftime("%H")) + float(current_time.strftime("%M")) / 60 - one_row[3]) * cost_per_hour, 1)
    print(f"Total for today's hours: ${cost}0")
    print(one_row)  # for debug purpose!  WILL MAKE INTO A FORMATTED MESSAGE
    if input("Is this info correct?") == "y":  # for debug purpose!
        cursor.execute(f"DELETE FROM Child WHERE firstName='{childperson}' and lastName='{childLast}';")
        conn.commit()
    return


def admin(option):
    for b in cursor:
        print(b)
    if choice == "x":
        if input("type (y) if you want to delete ALL records.") == "y":
            cursor.execute("Delete from Child")
            conn.commit()


choice = input("(d)rop/(p)ick/(a)dmin (dont use admin if there are no-one in the table)")
if choice == "d":
    dropoff()  # sends to drop off menu
elif choice == "p":
    pickup()  # sends to the pickup menu
elif choice == "a":
    choice = input("e(x)it or (p)rint list")
    admin(choice)
else:
    print(f"choose d/p/a, not {choice}")

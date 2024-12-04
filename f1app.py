import mysql.connector
db = mysql.connector.connect(
    host= "localhost",
    #user= ,
    #passwd= ",
    database="f1manager"
)
mycursor = db.cursor()
mycursor.execute("SHOW TABLES")
print("This is a F1 manager application for the whaterver F1 season.")
while True:
    print("Freatures")
    print("Enter 1 to modify drivers")
    print("Enter 2 to add a pitstop")
    print("Enter 3 for add/remove sponsor")
    print("Enter 4 to show top 10 fastest pit stops")
    print("Enter 5 to show avg driver race result")
    print("enter 6 to show best engines by avg position")
    print("Enter 7 for titak champions of each driver and their team")
    print("Enter 8 to see how many wins each driver has")
    print("Enter 9 for performance report")
    print("Enter 10 to update drivers and teams points")
    x = input("Enter response(enter q to terminate application): ")
    if x == "1":
        print("Enter 1 to add a driver or 2 to update a driver to have no team")
        d = input("Enter response(if you want to exit enter nothing):")
        if d == "1":
            print("Please enter the following values")
            fn = input("Driver firstname:")
            ln = input("Driver lastname:")
            dnum = input("Driver number:")
            tn = input("Driver's teamname:")
            dc = input("Number of Drivers Championships:")
        elif d == "2":
            d2 = input("Enter driver number you want to update:")
    elif x == "2":
        print("Please enter the following information")
        rn = input("round number:")
        tn = input("team name:")
        dnum = input("Driver number:")
        lnum = input("Lap number:")
        ptime = input("pitstop time in seconds:")
    elif x == "3":
        print("Enter 1 to add a sponsor or 2 to remove one")
        d = input("Enter response(if you want to exit enter nothing):")
        if d == "1":
            print("Please enter the following values")
            sn = input("Enter sponsor name:")
            tn = input("Enter team name:")
            am = input("Enter sponsorship money(In whole dollars):")
        elif d == "2":
            sn = input("Please enter the sponsor name to remove:")
    elif x == "4":
        print("test")
    elif x == "5":
        print("test")
    elif x == "6":
        print("test")
    elif x == "7":
        print("test")
    elif x == "8":
        print("test")
    elif x == "9":
        print("test")
    elif x == "10":
        dn = input("Enter driver number:")
        points = input("Enter points to add:")
    elif x == "q":
        break
    else:
        print("Invalid input please try again!")
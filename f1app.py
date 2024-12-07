import mysql.connector
db = mysql.connector.connect(
    host= "localhost",
    user= "nick",
    passwd= "passwd",
    database="f1manager"
)
mycursor = db.cursor()
mycursor.execute("SHOW TABLES")
for tb in mycursor:
    print(tb)
print("This is a F1 manager application for the whaterver F1 season.")
while True:
    print("Freatures")
    print("Enter 1 to modify drivers")
    print("Enter 2 to add a pitstop")
    print("Enter 3 for add/remove sponsor")
    print("Enter 4 to show top 10 fastest pit stops")
    print("Enter 5 to show avg driver race result")
    print("enter 6 to show best engines by avg position")
    print("Enter 7 for total champions of each driver and their team")
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
            mycursor = db.cursor()
            sql = "INSERT INTO drivers VALUES (%s,%s,%s,%s,%s)"
            mycursor.execute(sql,(fn,ln,dnum,tn,dc))
            db.commit()
        elif d == "2":
            d2 = input("Enter driver number you want to update:")
            mycursor = db.cursor()
            sql = "UPDATE driver SET team = NULL WHERE dnum = %s"
            mycursor.execute(sql,(d2,))
            db.commit()
    elif x == "2":
        print("Please enter the following information")
        rn = input("round number:")
        tn = input("team name:")
        dnum = input("Driver number:")
        lnum = input("Lap number:")
        ptime = input("pitstop time in seconds:")
        mycursor = db.cursor()
        sql = "INSERT INTO pitstop VALUES (%s,%s,%s,%s,%s)"
        mycursor.execute(sql,(rn,tn,dnum,lnum,ptime))
        db.commit()
    elif x == "3":
        print("Enter 1 to add a sponsor or 2 to remove one")
        d = input("Enter response(if you want to exit enter nothing):")
        if d == "1":
            print("Please enter the following values")
            sn = input("Enter sponsor name:")
            tn = input("Enter team name:")
            am = input("Enter sponsorship money(In whole dollars):")
            mycursor = db.cursor()
            sql = "INSERT INTO sponsor VALUES (%s,%s, %s)"
            mycursor.execute(sql,(sn,tn,am))
            db.commit()
        elif d == "2":
            sn = input("Please enter the sponsor name to remove:")
            mycursor = db.cursor()
            sql = "DELETE FROM sponsor WHERE sname = %s"
            mycursor.execute(sql,(sn,))
            db.commit() 
    elif x == "4":
        sql = "SELECT pitstop.ptime, race.rname, pitstop.tname FROM pitstop, race WHERE pitstop.rnum = race.rnum ORDER BY pitstop.ptime ASC LIMIT 10"
        #sql = "SELECT pitstop.ptime FROM pitstop"
        mycursor = db.cursor()
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print("Top 10 pitstops")
        for row in result:
            print(row)
    elif x == "5":
        sql = "SELECT driver.fname, driver.lname, driver.dnum, AVG(race_results.pos) AS avg_position FROM driver, race_results WHERE driver.dnum = race_results.dnum GROUP BY race_results.dnum ORDER BY avg_position ASC"
        mycursor = db.cursor()
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print("Avg driver race result")
        for row in result:
            print(row)
    elif x == "6":
        sql = "SELECT car.engine, AVG(race_results.pos) AS avg_position FROM driver, race_results, team, car WHERE race_results.dnum = driver.dnum AND driver.team = team.tname AND car.tname = team.tname GROUP BY car.engine ORDER BY avg_position ASC"
        mycursor = db.cursor()
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print("Best engine by avg position")
        for row in result:
            print(row)
    elif x == "7":
        sql = "SELECT driver.fname, driver.lname,team.tname,SUM(driver.dchamps + team.tchamp) AS total_championships FROM driver, team WHERE driver.team = team.tname GROUP BY driver.dnum"
        mycursor = db.cursor()
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print("Total champions of drivers and team")
        for row in result:
            print(row)
    elif x == "8":
        sql = "SELECT driver.fname,driver.lname,driver.dnum, COUNT(race_results.pos) as win_amount FROM driver, race_results WHERE driver.dnum = race_results.dnum AND race_results.pos = 1 GROUP BY race_results.dnum ORDER BY win_amount DESC"
        mycursor = db.cursor()
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print("Wins of drivers")
        for row in result:
            print(row)
    elif x == "9":
        sql = "SELECT driver.fname,driver.lname,car.cname, team.tname, SUM(sponsor.amount) AS total_sponsorship FROM car JOIN team ON car.tname = team.tname JOIN sponsor ON sponsor.tname = team.tname JOIN driver on driver.team = team.tname GROUP BY car.cname, team.tname,driver.fname,driver.lname ORDER BY team.tname,driver.fname,driver.lname"
        mycursor = db.cursor()
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print("Performance report")
        for row in result:
            print(row)
    elif x == "10":
        dn = input("Enter driver number:")
        tn = input("Enter team name")
        points = input("Enter points to add:")
        try:
            mycursor = db.cursor("")
            mycursor.execute("UPDATE driver SET point = point + %s WHERE dnum = %s",(points,dn))
            mycursor.execute("UPDATE team SET point = point+ %s WHERE tname = %s",(points,tn))
            db.commit()
            print("Done")
        except mysql.connector.Error as err:
            db.rollback()
            print("Failed operation due to ",err)
    elif x == "q":
        break
    else:
        print("Invalid input please try again!")
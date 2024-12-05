import mysql.connector
db = mysql.connector.connect(
    host= "localhost",
    #user= ,
    #passwd= ,
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
        sql = "SELECT p.time, r.rname, p.team FROM pitstop p, race r WHERE p.roundnum = r.roundnum ORDER BY p.time DESC LIMIT 10"
        mycursor = db.cursor()
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print("Top 10 pitstops")
        for row in result:
            print(row)
    elif x == "5":
        sql = "SELECT d.dname, d.dnum, AVG(rp.position) AS avg_position FROM driver d, race_result rp WHERE d.dnum = rp.dnum GROUP BY rp.dnum ORDER BY avg_position DESC"
        mycursor = db.cursor()
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print("Avg driver race result")
        for row in result:
            print(row)
    elif x == "6":
        sql = "SELECT c.engine, AVG(rp.position) AS avg_position FROM driver d, race_result rp, team t, car c WHERE rp.dnum = d.num AND d.tname = t.tname AND c.tname = t.tname GROUP BY c.engine ORDER BY avg_position DESC"
        mycursor = db.cursor()
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print("Best engine by avg position")
        for row in result:
            print(row)
    elif x == "7":
        sql = "SELECT d.dname,t.tname,SUM(d.cnum + c.cnum) AS total_championships FROM driver d, team t WHERE d.tname = t.tname GROUP BY t.tname"
        mycursor = db.cursor()
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print("Total champions of drivers and team")
        for row in result:
            print(row)
    elif x == "8":
        sql = "SELECT d.dnane, COUNT(rp.position) as win_amount FROM driver d, race_position rp WHERE d.dname = rp.dname AND rp.position = 1 GROUP BY rp.dname ORDER BY win_amount DESC"
        mycursor = db.cursor()
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print("Wins of drivers")
        for row in result:
            print(row)
    elif x == "9":
        sql = "SELECT d.fname,d.lname,d.point,c.cname, b.bname,SUM(s.amount) AS sponsorship_money FROM driver d, team t, tboss b, car c, sponsor s WHERE d.tname = t.tname AND b.tname = t.tname AND c.tname = c.tname AND s.tname = t.name GROUP BY t.tname ORDER BY t.tpoint DESC"
        mycursor = db.cursor()
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print("Wins of drivers")
        for row in result:
            print(row)
    elif x == "10":
        dn = input("Enter driver number:")
        tn = input("Enter team name")
        points = input("Enter points to add:")
        try:
            mycursor = db.cursor("")
            mycursor.execute("UPDATE driver SET point = point + %s WHERE dnum = %s"(points,dn))
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
def signup_maya(name, phonno, email, user, passwd):
    import sqlite3 as sql
    with sql.connect("mayauser.db") as con:
        cur = con.cursor()
        cur.execute("SELECT email FROM users where email=? ", (email,))
        account = cur.fetchall()
        for row in account:
            emailid = row[0]

            if emailid == email:
                msg = "User already exists!"
                return msg
        try:
            with sql.connect("mayauser.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO users(name,phone_no,email,user_name,password)VALUES(?, ?, ?, ?,?)",
                            (name, phonno, email, user, passwd))
                con.commit()
                msg = "Record successfully added"
        except Exception as e:
            con.rollback()
            print(e)
            msg = "Error in insert operation!"

        finally:
            con.close()

    return msg

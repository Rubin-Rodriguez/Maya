def signup_maya(name, phonno, email, user, passwd):
    import sqlite3 as sql
    try:
        with sql.connect("mayauser.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO users(name,phone_no,email,user_name,password)VALUES(?, ?, ?, ?,?)",
                    (name, phonno, email, user, passwd))
            con.commit()
            msg = "Record successfully added"
    except:
        con.rollback()
        msg = "Error in insert operation!"

    finally:
        con.close()
    return msg

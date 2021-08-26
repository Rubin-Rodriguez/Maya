# LOGIN MODULE
import sqlite3 as sql
def login_maya(usrname, passwd):
    login_flag = 0
    with sql.connect("mayauser.db") as con:
        cur = con.cursor()
        cur.execute("SELECT user_name,password FROM users where user_name=? ", (usrname,))
        account = cur.fetchall()

        for row in account:
            database_user = row[0]
            database_password = row[1]

            if database_user == usrname and database_password == passwd:
                login_flag = 1
            else:
                login_flag = 0
    return login_flag

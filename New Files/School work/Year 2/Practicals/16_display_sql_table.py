# This Python program runs a function to display all the records stored in a table using Python and MYSQL interface
# (C) Yajat Gupta

def run():
    import mysql.connector
    db = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'test1')
    try:
        c = db.cursor()
        sql = 'SELECT * FROM employee;'
        c.execute(sql)
        countrow = c.rowcount
        print('Number of rows: ',countrow)
        data = c.fetchall()
        print('+----------------------------------------+')
        print('| ecode | ename | gender | grade | gross |')
        print('+----------------------------------------+')
        for eachrow in data:
            ecode = eachrow[0]
            ename = eachrow[1]
            gender = eachrow[2]
            grade = eachrow[3]
            gross = eachrow[4]
            print(f'|  {ecode} |  {ename} |    {gender}   |   {grade}  |  {gross} |')
        print('+----------------------------------------+')
    except:
        db.rollback()
        db.close()
run()
import sqlite3
db='rbac.db'
def activity_logs(user_id,action,access_granted):
    conn=sqlite3.connect(db)
    cursor=conn.cursor()
    cursor.execute('''INSERT INTO activitylogs(user_id,action,access_granted) VALUES(?,?,?)''',(user_id,action,access_granted))
    conn.commit()
    conn.close()

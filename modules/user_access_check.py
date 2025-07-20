import sqlite3
from logger import activity_logs
db="rdac.db"
def has_access(user_name,permission_name):
    conn=sqlite3.connect(db)
    cursor=conn.cursor()
    cursor.execute("SELECT user_id FROM users WHERE user_name=?",(user_name,))
    user=cursor.fetchone()
    if not user:
        print("user not found")
        return False
    query='''SELECT 1 FROM userrole ur JOIN rolepermission rp ON ur.role_id=rp.role_id 
        JOIN permission p ON rp.permission_id=p.permission_id 
        WHERE ur.user_id=? AND p.permission_name=?'''
    cursor.execute(query,(user[0],permission_name))
    result=cursor.fetchone()
    conn.close()
    if not result:
        activity_logs(user[0],f"permission check {permission_name}",False)
        print(f"The user {user_name} does not have the {permission_name} permission")
        return False
    else:
        activity_logs(user[0], f"permission check {permission_name}", True)
        print(f"The user {user_name} has the {permission_name} permission")
        return True

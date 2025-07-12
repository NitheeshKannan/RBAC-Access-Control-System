import sqlite3
DB="rbac.db"
def create_role(role_name):
    conn=sqlite3.connect(DB)
    cursor=conn.cursor()
    try:
        cursor.execute("INSERT INTO roles(role_name) VALUES(?)",(role_name,))
        conn.commit()
        print(f"role{role_name} is created")
    except sqlite3.IntegrityError:
        print('Role already exists')
def view_roles():
    conn=sqlite3.connect(DB)
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM roles")
    roles=cursor.fetchall()
    conn.close()
    for role in roles:
        print(role[1])
def assign_role_to_user(user_id,role_id):
    conn=sqlite3.connect(DB)
    cursor=conn.cursor()
    try:
        cursor.execute("INSERT INTO userrole(user_id,role_id) VALUES(?,?)",(user_id,role_id))
        conn.commit()
        print(f"user{user_id} is assigned to role {role_id}")
    except sqlite3.IntegrityError:
        print('Role already exists')
def view_user_roles(user_id):
    conn=sqlite3.connect(DB)
    cursor=conn.cursor()
    cursor.execute("SELECT r.role_id,r.role_name FROM roles r join userrole u on r.role_id=u.role_id where u.user_id=?",(user_id,))
    roles=cursor.fetchall()
    conn.close()
    for role in roles:
        print(f"{role[0]}-{role[1]}")




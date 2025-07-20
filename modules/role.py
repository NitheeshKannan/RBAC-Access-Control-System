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
    cursor.execute("SELECT r.role_id,r.role_name FROM roles r JOIN userrole u on r.role_id=u.role_id where u.user_id=?",(user_id,))
    roles=cursor.fetchall()
    if not roles:
        print('No roles found')
        return
    if roles:
        print(f"the role for the user{user_id} ")
        for role in roles:
            print(f"{role[0]}-{role[1]}")
    else:
        print('No roles found')
    conn.close()
def delete_role_from_user(user_name,role_name):
    conn=sqlite3.connect(DB)
    cursor=conn.cursor()
    cursor.execute("SELECT user_id FROM users WHERE user_name=?",(user_name,))
    user=cursor.fetchone()
    if not user:
        print("The user does not exist")
        return
    cursor.execute("SELECT role_id FROM roles WHERE role_name=?",(role_name,))
    role=cursor.fetchone()
    if not role:
        print("The role does not exist")
        return
    cursor.execute("SELECT user_id,role_id FROM userrole WHERE role_id=? and user_id=?",(role[0],user[0]))
    check=cursor.fetchone()
    if not check:
        print(f"The user {user_name} does not have the {role_name} role")
    if check:
        cursor.execute("DELETE FROM userrole WHERE user_id=? and role_id=?",(user[0],role[0]))
        conn.commit()
        print(f"The role {role_name} has been deleted from user {user_name}")
    conn.close()






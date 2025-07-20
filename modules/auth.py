import sqlite3
db='rbac.db'
def signup(user_name,passoword):
    try:
        with sqlite3.connect(db) as conn:
            cursor=conn.cursor()
            cursor.execute('INSERT INTO users(user_name,password) values(?,?)',(user_name,passoword))
            conn.commit()
        print(f'user{user_name} is signed up successfully')
    except sqlite3.IntegrityError:
        print(f'user{user_name} is already signed up')
def login(user_name,password):
    with sqlite3.connect(db) as conn:
            cursor=conn.cursor()
            cursor.execute('SELECT user_id,is_active FROM users WHERE user_name=? AND password=?',(user_name,password))
    users=cursor.fetchone()
    if users:
        user_id,active=users
        if active:
            print(f'user {user_name} is logged in')
            print(f'the {user_name} id is {user_id}')
        else:
            print(f'user {user_name} id is deactivated')
    else:
        print('Invalid credentials')
    return None
def deactivate(user_id):
    with sqlite3.connect(db) as conn:
        cursor=conn.cursor()
        cursor.execute('UPDATE users SET is_active=0 WHERE user_id=?',(user_id,))
        conn.commit()
        print(f'user{user_id} is deactivated')
def reactivate(user_id):
    with sqlite3.connect(db) as conn:
        cursor=conn.cursor()
        cursor.execute('UPDATE users SET is_active=1 WHERE user_id=?',(user_id,))
        conn.commit()
        print(f'user{user_id} is reactivated')




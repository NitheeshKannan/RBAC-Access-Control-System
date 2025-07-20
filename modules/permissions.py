import sqlite3
DB="rdbms.db"
def create_permission(permission_name):
        conn = sqlite3.connect(DB)
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO permission (permission_name) VALUES(?)",(permission_name,))
            conn.commit()
            print(f"{permission_name} has been created")
        except sqlite3.IntegrityError:
            print(f"{permission_name} already exists")
        finally:
            conn.close()
def view_all_permissions():
        conn = sqlite3.connect(DB)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM permission")
        permissions = cursor.fetchall()
        if permissions:
            for permission in permissions:
                print(f"{permission[0]}: {permission[1]}")
        else:
            print("No permissions in the database")
        conn.close()
def assign_permission_to_role(role_name,permission_name):
        conn = sqlite3.connect(DB)
        cursor = conn.cursor()
        cursor.execute("SELECT role_id FROM roles WHERE role_name =?",(role_name,))
        role=cursor.fetchone()
        cursor.execute("SELECT permission_id FROM permission WHERE permission_name =?",(permission_name,))
        permission=cursor.fetchone()
        try:
            if role and permission:
                cursor.execute("INSERT INTO rolepermission (role_id, permission_id) VALUES(?,?)",(role[0],permission[0]))
                conn.commit()
                print(f"{role[0]} has been assigned to {permission[0]}")
            else:
                print("Role or permission not found")
        except sqlite3.IntegrityError:
            print(f"{permission_name} already assigned to the {role_name} role")
        finally:
            conn.close()
def remove_permission_from_role(role_name,permission_name):
        conn = sqlite3.connect(DB)
        cursor = conn.cursor()
        cursor.execute("SELECT permission_id FROM permission WHERE permission_name =?",(permission_name,))
        permission=cursor.fetchone()
        if not permission:
            print("Permission not found")
            return
        cursor.execute("SELECT role_id FROM roles WHERE role_name =?",(role_name,))
        role=cursor.fetchone()
        if not role:
            print("Role not found")
            return
        if role and permission:
            cursor.execute("DELETE FROM rolepermission WHERE role_id = ? and permission_id=?",(role[0],permission[0]))
            conn.commit()
            print(f"{role[0]} has been removed from {permission[0]}")
        else:
            print("Role or permission not found")
        conn.close()
def view_permission_for_role(role_name):
        conn = sqlite3.connect(DB)
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM roles WHERE role_name =?",(role_name,))
            role=cursor.fetchone()
            if not role:
                print("Role not found")
                return
            cursor.execute("SELECT p.permission_name FROM permission JOIN rolepermission rp ON rp.permission_id = p.permission_id WHERE rp.role_id = ? ",(role[0],))
            permission=cursor.fetchall()
            if permission:
                print(f"permission for the {role_name} role is ")
                for perm in permission:
                    print(f"{perm[0]}")
            else:
                print("No permissions in the database")
        except sqlite3.IntegrityError:
            print(f"{role_name} already assigned to {role_name} role")
        finally:
            conn.close()






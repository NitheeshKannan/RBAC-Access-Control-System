# 🔐 RBAC Access Control System (Python + SQLite)

A complete **Role-Based Access Control (RBAC)** system built with **Python and SQLite**. This project enables user authentication, role assignment, permission enforcement, and activity logging — following best practices in secure software design.

---

## 📚 Overview

This project simulates a real-world **access control system** where:

- Users can register and log in
- Admins assign **roles** to users
- Roles are mapped to **permissions**
- Access control decisions (like `has_access()`) are made based on roles
- All actions are logged for auditability

---

## ⚙️ Features

### ✅ Authentication Module
- User signup and secure login
- Activation/deactivation of users

### ✅ Role & Permission Management
- Create roles and permissions
- Assign multiple roles to a user
- Assign multiple permissions to a role

### ✅ Access Control
- `has_access(user_id, permission_name)` function to verify access
- Logic to check whether a user can perform a given action

### ✅ Activity Logging
- Logs every access attempt (granted/denied)
- Tracks user_id, action name, timestamp, and result

---

## 🗃️ Database Schema

Built using **SQLite** and executed via Python using a `schema.sql` file.  
The schema includes the following tables:

- `users` — stores user credentials and status
- `roles` — defines roles like Admin, Viewer, Manager
- `permission` — defines system actions like read, write, delete
- `userrole` — junction table (many-to-many between users and roles)
- `rolepermission` — junction table (many-to-many between roles and permissions)
- `activitylogs` — logs user access attempts

---

## 🏗️ Project Structure
rbac_project/
├── ER diagram #ER diagram of the database schema
├── db/
│ └── schema.sql # SQL schema for all tables
├── main.py # Creates SQLite DB using schema.sql
├── rbac.db # Auto-generated SQLite database
├── modules/
│ ├── auth.py # Signup, login, activate/deactivate users
│ ├── roles.py # Create roles, assign roles to users
│ ├── permissions.py # Create permissions, assign to roles
│ ├── access.py # has_access() and action logging
│ └── db_utils.py # DB connection and query helpers
└── .gitignore # Ignore .db and cache files

DEMO PICTURE :









<img width="741" height="867" alt="image" src="https://github.com/user-attachments/assets/78396b22-d24f-413b-bf49-64634d05fbfc" />


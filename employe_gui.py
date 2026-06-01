import mysql.connector
import tkinter as tk
from tkinter import messagebox

# ---------------- DATABASE CONNECTION ----------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MySQL@123",
    database="employee_db"
)

cursor = conn.cursor()

# ---------------- FUNCTIONS ----------------

def add_employee():
    try:
        emp_id = entry_id.get()
        name = entry_name.get()
        dept = entry_dept.get()
        salary = entry_salary.get()

        sql = "INSERT INTO employees VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (emp_id, name, dept, salary))
        conn.commit()

        messagebox.showinfo("Success", "Employee Added Successfully")

    except Exception as e:
        messagebox.showerror("Error", str(e))


def view_employees():
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()

    result = ""
    for row in rows:
        result += f"ID: {row[0]} | Name: {row[1]} | Dept: {row[2]} | Salary: {row[3]}\n"

    messagebox.showinfo("Employees List", result)


def update_employee():
    try:
        emp_id = entry_id.get()
        salary = entry_salary.get()

        sql = "UPDATE employees SET salary=%s WHERE emp_id=%s"
        cursor.execute(sql, (salary, emp_id))
        conn.commit()

        messagebox.showinfo("Success", "Salary Updated")

    except Exception as e:
        messagebox.showerror("Error", str(e))


def delete_employee():
    try:
        emp_id = entry_id.get()

        sql = "DELETE FROM employees WHERE emp_id=%s"
        cursor.execute(sql, (emp_id,))
        conn.commit()

        messagebox.showinfo("Success", "Employee Deleted")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------------- GUI WINDOW ----------------

root = tk.Tk()
root.title("Employee Management System")
root.geometry("400x400")

# Labels & Inputs
tk.Label(root, text="Employee ID").pack()
entry_id = tk.Entry(root)
entry_id.pack()

tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Department").pack()
entry_dept = tk.Entry(root)
entry_dept.pack()

tk.Label(root, text="Salary").pack()
entry_salary = tk.Entry(root)
entry_salary.pack()

# Buttons
tk.Button(root, text="Add Employee", command=add_employee).pack(pady=5)
tk.Button(root, text="View Employees", command=view_employees).pack(pady=5)
tk.Button(root, text="Update Salary", command=update_employee).pack(pady=5)
tk.Button(root, text="Delete Employee", command=delete_employee).pack(pady=5)

root.mainloop()
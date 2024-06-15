import tkinter as tk
from tkinter import messagebox
import random

class StudentManagementSystem:
    def __init__(self, root, admin_password):
        self.admin_password = admin_password
        self.file_path = 'tudent_data.txt'
        self.removed_file_path = 'emoved_students.txt'
        self.root = root
        self.root.title("Student Management System")

        self.notebook = tk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True)

        self.register_frame = tk.Frame(self.notebook)
        self.remove_frame = tk.Frame(self.notebook)
        self.show_frame = tk.Frame(self.notebook)
        self.show_department_frame = tk.Frame(self.notebook)
        self.show_deleted_frame = tk.Frame(self.notebook)

        self.notebook.add(self.register_frame, text="Register Student")
        self.notebook.add(self.remove_frame, text="Remove Student")
        self.notebook.add(self.show_frame, text="Show Student")
        self.notebook.add(self.show_department_frame, text="Show Students in Department")
        self.notebook.add(self.show_deleted_frame, text="Especial Access (Admin Only)")

        self.register_widgets()
        self.remove_widgets()
        self.show_widgets()
        self.show_department_widgets()
        self.show_deleted_widgets()

    def generate_student_id(self):
        return random.randint(100000, 999999)

    def register_widgets(self):
        tk.Label(self.register_frame, text="First Name:").pack()
        self.first_name_entry = tk.Entry(self.register_frame)
        self.first_name_entry.pack()

        tk.Label(self.register_frame, text="Last Name:").pack()
        self.last_name_entry = tk.Entry(self.register_frame)
        self.last_name_entry.pack()

        tk.Label(self.register_frame, text="Phone Number:").pack()
        self.phone_number_entry = tk.Entry(self.register_frame)
        self.phone_number_entry.pack()

        tk.Label(self.register_frame, text="Department:").pack()
        self.department_entry = tk.Entry(self.register_frame)
        self.department_entry.pack()

        tk.Button(self.register_frame, text="Register", command=self.register_student).pack()

    def register_student(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        phone_number = self.phone_number_entry.get()
        department = self.department_entry.get()

        if not first_name.isalpha():
            messagebox.showerror("Error", "Invalid first name")
            return
        if not last_name.isalpha():
            messagebox.showerror("Error", "Invalid last name")
            return
        if not phone_number.isdigit():
            messagebox.showerror("Error", "Invalid phone number")
            return
        if not department.isalpha():
            messagebox.showerror("Error", "Invalid department")
            return

        student_id = self.generate_student_id()
        full_name = f"{first_name} {last_name}"
        student_info = f"{student_id},{full_name},{phone_number},{department}\n"

        with open(self.file_path, 'a') as file:
            file.write(student_info)

        messagebox.showinfo("Success", f"Student registered successfully! Student ID: {student_id}")

    def remove_widgets(self):
        tk.Label(self.remove_frame, text="Student ID to remove:").pack()
        self.remove_entry = tk.Entry(self.remove_frame)
        self.remove_entry.pack()

        tk.Button(self.remove_frame, text="Remove", command=self.remove_student).pack()

    def remove_student(self):
        student_id_to_remove = self.remove_entry.get()

        found = False
        with open(self.file_path, 'r') as file:
            lines = file.readlines()

        with open(self.file_path, 'w') as file:
            for line in lines:
                data = line.strip().split(',')
                if data[0]!= student_id_to_remove:
                    file.write(line)
                else:
                    found = True
                    with open(self.removed_file_path, 'a') as removed_file:
                        removed_file.write(line)

        if found:
            messagebox.showinfo("Success", f"Student with ID {student_id_to_remove} has been removed.")
        else:
            messagebox.showerror("Error", f"Student with ID {student_id_to_remove} not found in the records.")

    def show_widgets(self):
        tk.Label(self.show_frame, text="Student ID to show:").pack()
        self.show_entry = tk.Entry(self.show_frame)
        self.show_entry.pack()

        tk.Button(self.show_frame, text="Show", command=self.show_student).pack()

    def show_student(self):
        student_id = self.show_entry.get()
        found = False
        with open(self.file_path, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if data[0] == student_id:
                    messagebox.showinfo("Student Info", f"Student ID: {data[1
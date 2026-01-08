# School Management Python MySQL Project

## 📌 Project Overview

This is a simple Python program that demonstrates how to use **MySQL database operations** from Python.  
It connects to a local **MySQL server**, creates a database, creates tables, inserts sample data, displays data and performs update & delete operations.

✔ Uses `mysql-connector-python` to connect to MySQL  
✔ Performs basic **CRUD** operations  
✔ Helps you learn how Python interacts with databases  

---

## 🛠 Features

- Connects securely to MySQL
- Creates database (`SchoolDB`)
- Creates tables (`Students`, `Classes`)
- Inserts sample student and class data
- Displays student and score data
- Updates a record and deletes another  
- Safely resets and reuses tables

---

## 📁 Project Structure

├── school_db.py
├── README.md
├── requirements.txt
└── .gitignore

---

## 🚀 Getting Started

### ✅ Prerequisites

Make sure you have the following installed:

- **Python 3.x**
- **MySQL Server**
- Visual Studio Code (optional but recommended)

### 🎯 Install Dependencies

Open your terminal and run:

```bash
pip install mysql-connector-python
MySQL Setup

Start your local MySQL server and log in with:

mysql -u root -p


When prompted, enter your root password:

Ukalyani@123


If you get an authentication error, update your MySQL user to use native password (optional):

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Ukalyani@123';
FLUSH PRIVILEGES;

📌 How to Run

Open your project folder in Visual Studio Code

Open the integrated terminal (`Ctrl + ``)

Run:

python school_db.py


Or:

python3 school_db.py


You should see console output showing database creation, insertion, display, update & delete operations.

🧾 Expected Output

Sample output after running the script includes:

Connected to MySQL
Database ready
Tables ready
Sample data inserted safely
--- Students ---
(1, 'Alice', 14, '8th')
...
--- Student Scores (JOIN) ---
('Alice', 'Math', 85)
...
Update & delete complete safely

🧩 How It Works

The script includes functions to:

Connect to MySQL

Create database & tables

Reset tables (clear old data)

Insert sample data

Display data with SQL JOIN

Update & delete specific records

📝 Notes

You can change the sample data to test other scenarios.

This can be extended to a GUI, web app, or API layer (Flask/FastAPI).

🧪 Try It Yourself

You can modify the tables and add new operations like:

✔ Searching by grade
✔ Displaying average scores
✔ Deleting multiple student records

📞 Contact

If you have any issues or suggestions, send a message to:

yourname@example.com

📜 License

This project is licensed under the MIT License — feel free to reuse & improve!
(Add a LICENSE file if needed)


---

### ✅ Why This Works

A good README should:

✔ Explain **what** the project does  
✔ Show how to **install and run it**  
✔ Provide useful **examples and outputs**  
✔ Include any **notes about setup** (e.g., MySQL configuration) :contentReference[oaicite:0]{index=0}

---

If you want, I can also automatically generate a **GitHub friendly version** with badges (e.g., Python version, build status). Just ask!
::contentReference[oaicite:1]{index=1}

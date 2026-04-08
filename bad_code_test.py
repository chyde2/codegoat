import sqlite3
import os

# --- VULNERABILITY 1: Hardcoded Cloud Secrets ---
# Scanners will flag these as exposed AWS credentials.
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# --- VULNERABILITY 2: Hardcoded Database Secrets ---
DB_USER = "admin_root"
DB_PASSWORD = "SuperSecretPassword123!"

def lookup_employee(employee_name):
    """
    --- VULNERABILITY 3: SQL Injection ---
    Gluing strings together to make a database command allows attackers
    to manipulate the database.
    """
    conn = sqlite3.connect('company.db')
    cursor = conn.cursor()
    
    # Bad practice: String interpolation for SQL commands
    sql_command = f"SELECT * FROM employees WHERE name = '{employee_name}'"
    cursor.execute(sql_command)
    return cursor.fetchall()

def ping_server(ip_address):
    """
    --- VULNERABILITY 4: OS Command Injection ---
    Passing un-sanitized input directly to the operating system.
    """
    # Bad practice: Concatenating input directly into a system command
    os.system("ping -c 1 " + ip_address)

if __name__ == "__main__":
    print("Testing vulnerabilities...")


from werkzeug.security import generate_password_hash
from database import get_connection
import getpass

username = input("Enter admin username: ").strip()
password = getpass.getpass("Enter admin password: ")

if not username or len(password) < 8:
    print("Username required; password must be at least 8 characters.")
else:
    conn = get_connection()
    cursor = conn.cursor()

    try:
        password_hash = generate_password_hash(password)

        cursor.execute(
            """INSERT INTO users (username, password_hash)
               VALUES (%s, %s)""",
            (username, password_hash)
        )

        conn.commit()
        print("Admin account created successfully!")

    except Exception as error:
        conn.rollback()
        print("Account could not be created. Username may already exist.")

    finally:
        cursor.close()
        conn.close()

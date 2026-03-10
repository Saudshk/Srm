<<<<<<< HEAD
import sqlite3
from werkzeug.security import generate_password_hash

DB_NAME = "company_data.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS admins (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS companies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_name TEXT NOT NULL,
        notes TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS company_tables (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_id INTEGER NOT NULL,
        table_name TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (company_id) REFERENCES companies(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS table_columns (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        table_id INTEGER NOT NULL,
        column_name TEXT NOT NULL,
        column_type TEXT NOT NULL DEFAULT 'text',
        is_expiry INTEGER NOT NULL DEFAULT 0,
        display_order INTEGER NOT NULL,
        FOREIGN KEY (table_id) REFERENCES company_tables(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS table_rows (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        table_id INTEGER NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (table_id) REFERENCES company_tables(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS row_values (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        row_id INTEGER NOT NULL,
        column_id INTEGER NOT NULL,
        value TEXT,
        FOREIGN KEY (row_id) REFERENCES table_rows(id),
        FOREIGN KEY (column_id) REFERENCES table_columns(id)
    )
    """)
    cursor.execute("""
CREATE TABLE IF NOT EXISTS companies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT NOT NULL,
    heading TEXT,
    description TEXT,
    contact_person TEXT,
    phone TEXT,
    email TEXT,
    address TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
    cursor.execute("""
CREATE TABLE IF NOT EXISTS company_details (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    detail_label TEXT NOT NULL,
    detail_value TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (company_id) REFERENCES companies(id)
)
""")
    cursor.execute("""
CREATE TABLE IF NOT EXISTS audit_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    admin_username TEXT,
    company_id INTEGER,
    company_name TEXT,
    action_type TEXT NOT NULL,
    description TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
    # Create default admin if not exists
    cursor.execute("SELECT * FROM admins WHERE username = ?", ("admin",))
    admin = cursor.fetchone()

    if not admin:
        password_hash = generate_password_hash("admin123")
        cursor.execute(
            "INSERT INTO admins (username, password_hash) VALUES (?, ?)",
            ("admin", password_hash)
        )
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_table_permissions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        table_id INTEGER,
        FOREIGN KEY(user_id) REFERENCES users(id),
        FOREIGN KEY(table_id) REFERENCES company_tables(id)
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_detail_permissions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        detail_id INTEGER,
        FOREIGN KEY(user_id) REFERENCES users(id),
        FOREIGN KEY(detail_id) REFERENCES company_details(id)
    )
    """)
    try:
        cursor.execute("ALTER TABLE company_tables ADD COLUMN created_by_user_id INTEGER")
    except:
        pass

    try:
        cursor.execute("ALTER TABLE audit_logs ADD COLUMN actor_role TEXT")
    except:
        pass

    try:
        cursor.execute("ALTER TABLE audit_logs ADD COLUMN actor_username TEXT")
    except:
        pass

    try:
        cursor.execute("ALTER TABLE audit_logs ADD COLUMN table_id INTEGER")
    except:
        pass

    try:
        cursor.execute("ALTER TABLE audit_logs ADD COLUMN table_name TEXT")
    except:
        pass
    cursor.execute("PRAGMA table_info(audit_logs)")
    columns = cursor.fetchall()
    print("AUDIT_LOGS COLUMNS:")
    for col in columns:
        print(col)
    conn.commit()
    conn.close()
    print("Database initialized successfully.")

    
if __name__ == "__main__":
=======
import sqlite3
from werkzeug.security import generate_password_hash

DB_NAME = "company_data.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS admins (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS companies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_name TEXT NOT NULL,
        notes TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS company_tables (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_id INTEGER NOT NULL,
        table_name TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (company_id) REFERENCES companies(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS table_columns (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        table_id INTEGER NOT NULL,
        column_name TEXT NOT NULL,
        column_type TEXT NOT NULL DEFAULT 'text',
        is_expiry INTEGER NOT NULL DEFAULT 0,
        display_order INTEGER NOT NULL,
        FOREIGN KEY (table_id) REFERENCES company_tables(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS table_rows (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        table_id INTEGER NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (table_id) REFERENCES company_tables(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS row_values (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        row_id INTEGER NOT NULL,
        column_id INTEGER NOT NULL,
        value TEXT,
        FOREIGN KEY (row_id) REFERENCES table_rows(id),
        FOREIGN KEY (column_id) REFERENCES table_columns(id)
    )
    """)
    cursor.execute("""
CREATE TABLE IF NOT EXISTS companies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT NOT NULL,
    heading TEXT,
    description TEXT,
    contact_person TEXT,
    phone TEXT,
    email TEXT,
    address TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
    cursor.execute("""
CREATE TABLE IF NOT EXISTS company_details (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    detail_label TEXT NOT NULL,
    detail_value TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (company_id) REFERENCES companies(id)
)
""")
    cursor.execute("""
CREATE TABLE IF NOT EXISTS audit_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    admin_username TEXT,
    company_id INTEGER,
    company_name TEXT,
    action_type TEXT NOT NULL,
    description TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
    # Create default admin if not exists
    cursor.execute("SELECT * FROM admins WHERE username = ?", ("admin",))
    admin = cursor.fetchone()

    if not admin:
        password_hash = generate_password_hash("admin123")
        cursor.execute(
            "INSERT INTO admins (username, password_hash) VALUES (?, ?)",
            ("admin", password_hash)
        )

    conn.commit()
    conn.close()
    print("Database initialized successfully.")

if __name__ == "__main__":
>>>>>>> 64bfbef9fa20762ecf5499a190c88bf784a8ae4f
    init_db()
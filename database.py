import sqlite3

DB_NAME = "teja.db"


def get_connection():
    return sqlite3.connect(
        DB_NAME,
        check_same_thread=False
    )


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chats(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chat_id INTEGER,
        role TEXT,
        content TEXT
    )
    """)

    conn.commit()
    conn.close()


def create_chat():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO chats(title) VALUES(?)",
        ("New Chat",)
    )

    conn.commit()

    chat_id = cursor.lastrowid

    conn.close()

    return chat_id


def get_chats():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id,title FROM chats ORDER BY id DESC"
    )

    rows = cursor.fetchall()

    conn.close()

    return rows


def save_message(chat_id, role, content):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO messages
        (chat_id,role,content)
        VALUES(?,?,?)
        """,
        (chat_id, role, content)
    )

    conn.commit()
    conn.close()


def get_messages(chat_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT role,content
        FROM messages
        WHERE chat_id=?
        ORDER BY id
        """,
        (chat_id,)
    )

    rows = cursor.fetchall()

    conn.close()

    return rows
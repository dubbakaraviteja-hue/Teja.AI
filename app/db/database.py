import sqlite3

DB_NAME = "teja.db"


# =========================
# CONNECTION
# =========================

def get_connection():
    conn = sqlite3.connect(
        DB_NAME,
        check_same_thread=False
    )

    conn.execute(
        "PRAGMA foreign_keys = ON"
    )

    return conn


# =========================
# DATABASE INIT
# =========================

def init_db():

    conn = get_connection()
    cursor = conn.cursor()

    # =========================
    # CHATS
    # =========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chats(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT DEFAULT 'New Chat',
        pinned INTEGER DEFAULT 0,
        archived INTEGER DEFAULT 0,
        shared INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # =========================
    # MESSAGES
    # =========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chat_id INTEGER,
        role TEXT,
        content TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        FOREIGN KEY(chat_id)
        REFERENCES chats(id)
        ON DELETE CASCADE
    )
    """)

    # =========================
    # LIBRARY
    # =========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS library(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_name TEXT,
        file_type TEXT,
        file_path TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


# =========================
# CHAT FUNCTIONS
# =========================

def create_chat():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO chats(title)
        VALUES(?)
        """,
        ("New Chat",)
    )

    conn.commit()

    chat_id = cursor.lastrowid

    conn.close()

    return chat_id


def get_chats():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
    id,
    title,
    pinned,
    archived,
    shared,
    created_at,
    updated_at
    FROM chats
    ORDER BY pinned DESC,
    updated_at DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def rename_chat(chat_id, title):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE chats
        SET title=?,
        updated_at=CURRENT_TIMESTAMP
        WHERE id=?
        """,
        (title, chat_id)
    )

    conn.commit()
    conn.close()


def update_chat_title(chat_id, title):

    rename_chat(chat_id, title)


def touch_chat(chat_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE chats
        SET updated_at=CURRENT_TIMESTAMP
        WHERE id=?
        """,
        (chat_id,)
    )

    conn.commit()
    conn.close()


def pin_chat(chat_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE chats
        SET pinned=1,
        updated_at=CURRENT_TIMESTAMP
        WHERE id=?
        """,
        (chat_id,)
    )

    conn.commit()
    conn.close()


def unpin_chat(chat_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE chats
        SET pinned=0
        WHERE id=?
        """,
        (chat_id,)
    )

    conn.commit()
    conn.close()


def archive_chat(chat_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE chats
        SET archived=1
        WHERE id=?
        """,
        (chat_id,)
    )

    conn.commit()
    conn.close()


def unarchive_chat(chat_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE chats
        SET archived=0
        WHERE id=?
        """,
        (chat_id,)
    )

    conn.commit()
    conn.close()


def share_chat(chat_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE chats
        SET shared=1
        WHERE id=?
        """,
        (chat_id,)
    )

    conn.commit()
    conn.close()


def delete_chat(chat_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM chats
        WHERE id=?
        """,
        (chat_id,)
    )

    conn.commit()
    conn.close()


def search_chats(keyword):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id,title
        FROM chats
        WHERE title LIKE ?
        ORDER BY updated_at DESC
        """,
        (f"%{keyword}%",)
    )

    rows = cursor.fetchall()

    conn.close()

    return rows


# =========================
# MESSAGE FUNCTIONS
# =========================

def save_message(
        chat_id,
        role,
        content
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO messages
        (
        chat_id,
        role,
        content
        )
        VALUES
        (
        ?,
        ?,
        ?
        )
        """,
        (
            chat_id,
            role,
            content
        )
    )

    cursor.execute(
        """
        UPDATE chats
        SET updated_at=CURRENT_TIMESTAMP
        WHERE id=?
        """,
        (chat_id,)
    )

    conn.commit()
    conn.close()


def get_messages(chat_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
        role,
        content,
        created_at
        FROM messages
        WHERE chat_id=?
        ORDER BY id ASC
        """,
        (chat_id,)
    )

    rows = cursor.fetchall()

    conn.close()

    return rows


# =========================
# LIBRARY FUNCTIONS
# =========================

def save_file(
        file_name,
        file_type,
        file_path
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO library
        (
        file_name,
        file_type,
        file_path
        )
        VALUES
        (
        ?,
        ?,
        ?
        )
        """,
        (
            file_name,
            file_type,
            file_path
        )
    )

    conn.commit()
    conn.close()


def get_library():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM library
        ORDER BY id DESC
        """
    )

    rows = cursor.fetchall()

    conn.close()

    return rows


def get_library_by_type(file_type):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM library
        WHERE file_type=?
        ORDER BY id DESC
        """,
        (file_type,)
    )

    rows = cursor.fetchall()

    conn.close()

    return rows

# =========================
# ANALYTICS
# =========================

def get_total_chats():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM chats"
    )

    count = cursor.fetchone()[0]

    conn.close()

    return count


def get_total_messages():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM messages"
    )

    count = cursor.fetchone()[0]

    conn.close()

    return count


def get_messages_today():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM messages
    WHERE DATE(created_at)=DATE('now')
    """)

    count = cursor.fetchone()[0]

    conn.close()

    return count


def get_messages_this_month():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM messages
    WHERE strftime('%Y-%m', created_at)
          =
          strftime('%Y-%m','now')
    """)

    count = cursor.fetchone()[0]

    conn.close()

    return count


def get_most_active_chat():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        chats.id,
        chats.title,
        COUNT(messages.id) AS total
    FROM chats
    LEFT JOIN messages
    ON chats.id = messages.chat_id
    GROUP BY chats.id
    ORDER BY total DESC
    LIMIT 1
    """)

    row = cursor.fetchone()

    conn.close()

    return row
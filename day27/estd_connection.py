import psycopg2


def estd_connection():
    conn = psycopg2.connect(
        database="studentdb",
        user="postgres",
        password="password",
        host="127.0.0.1",
        port=5432
    )
    conn.autocommit = True
    cursor = conn.cursor()
    return cursor


if __name__ == "__main__":
    estd_connection()
    print("Connection established successfully !!")

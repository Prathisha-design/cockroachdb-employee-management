from db import get_connection


def create_schema():
    conn = get_connection()

    try:
        with open("schema.sql", "r") as file:
            sql = file.read()

        with conn.cursor() as cursor:
            cursor.execute(sql)

        conn.commit()
        print("Database schema created successfully!")

    except Exception as e:
        conn.rollback()
        print("Schema creation failed:")
        print(e)

    finally:
        conn.close()


if __name__ == "__main__":
    create_schema()
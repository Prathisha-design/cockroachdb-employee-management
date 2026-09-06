from db import get_connection


def transfer_employee():
    conn = get_connection()

    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT department_id
                FROM departments
                WHERE department_name = 'Engineering';
            """)

            engineering_id = cursor.fetchone()[0]

            cursor.execute("""
                UPDATE employees
                SET department_id = %s
                WHERE email = 'arun.kumar@example.com';
            """, (engineering_id,))

        conn.commit()
        print("Transaction completed successfully!")

    except Exception as e:
        conn.rollback()
        print("Transaction failed:")
        print(e)

    finally:
        conn.close()


if __name__ == "__main__":
    transfer_employee()
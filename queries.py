from db import get_connection


def show_employees():
    conn = get_connection()

    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT
                    e.first_name,
                    e.last_name,
                    e.job_title,
                    d.department_name,
                    e.salary
                FROM employees e
                JOIN departments d
                    ON e.department_id = d.department_id
                ORDER BY e.first_name;
            """)

            rows = cursor.fetchall()

            print("\nEmployees")
            print("-" * 70)

            for row in rows:
                print(
                    f"{row[0]} {row[1]} | "
                    f"{row[2]} | "
                    f"{row[3]} | "
                    f"Salary: {row[4]}"
                )

    finally:
        conn.close()


if __name__ == "__main__":
    show_employees()
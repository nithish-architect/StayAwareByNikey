import time
import psycopg2
from app import create_app, db

app = create_app()

def wait_for_db():
    while True:
        try:
            conn = psycopg2.connect(
                host="db",
                database="stayaware",
                user="nikey",
                password="nikey123"
            )
            conn.close()
            print("Database is ready.")
            break
        except psycopg2.OperationalError:
            print("Waiting for database...")
            time.sleep(2)

if __name__ == '__main__':
    wait_for_db()
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)

import sqlite3


class Database:
    def __init__(self, db_path="tasks.db"):
        self.db_path = db_path
        self.connection = sqlite3.connect(self.db_path)
        self.connection.row_factory = sqlite3.Row  # access columns by name: row["title"]
        self.connection.execute("PRAGMA foreign_keys = ON")
        self.create_tables()

    def create_tables(self):
        self.connection.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                task_id     INTEGER PRIMARY KEY,
                title       TEXT NOT NULL,
                description TEXT,
                status      INTEGER NOT NULL DEFAULT 1,
                created_at  TEXT NOT NULL
            )
            """
        )
        self.connection.commit()

    def execute(self, query, params=()):
        """Run a query that changes data (INSERT / UPDATE / DELETE) and commit it."""
        cursor = self.connection.execute(query, params)
        self.connection.commit()
        return cursor

    def fetch_one(self, query, params=()):
        return self.connection.execute(query, params).fetchone()

    def fetch_all(self, query, params=()):
        return self.connection.execute(query, params).fetchall()

    def close(self):
        self.connection.close()

    # Allows: with Database() as db: ...
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()


def main() -> None:
    with Database() as db:
        tables = db.fetch_all("SELECT name FROM sqlite_master WHERE type = 'table'")
        print("Tables:", [row["name"] for row in tables])


if __name__ == "__main__":
    main()

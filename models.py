import sqlite3


class Schema:
    def __init__(self):
        self.connection = sqlite3.connect('app.db')
        self.create()

    def create(self):
        query = """
            CREATE TABLE IF NOT EXISTS "Todo" (
                id INTEGER PRIMARY KEY,
                Title, TEXT, 
                Description TEXT
            );
        """

        self.connection.execute(query)


class TodoModel:

    def __init__(self):
        self.connection = sqlite3.connect("app.db")

    def create_data(self, title, description):
        query = f'insert into Todo (Title, Description) values ("{title}","{description}")'

        result = self.connection.execute(query)
        self.connection.commit()

        return f"Ok {result.lastrowid}"

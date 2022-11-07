import sqlite3
from datetime import datetime

class DBbase:

    _conn = None
    _cursor = None

    def __init__(self, db_name):
        self._db_name = db_name
        self.connect()

    def connect(self):
        self._conn = sqlite3.connect(self._db_name)
        self._cursor = self._conn.cursor()

    def execute_script(self, sql_string):
        self._cursor.executescript(sql_string)

    @property
    def get_cursor(self):
        return self._cursor

    @property
    def get_connection(self):
        return self._conn

    def reset_database(self):
        raise NotImplementedError("Must implement from the derived class")

    def close_db(self):
        self._conn.close()

class Room(DBbase):

        def __init__(self):
            super().__init__("RoomDB.sqlite")

        def update(self, room_id, availability):
            try:
                super().connect()
                super().get_cursor.execute("""UPDATE ROOM SET availability = ? WHERE room_id = ?;""", (availability, room_id,))
                super().get_connection.commit()
                super().close_db()
                print("Updated successfully.")
            except Exception as e:
                print("An error occurred.", e)

        def add(self, room_type, availability, room_price):
            try:
                super().connect()
                super().get_cursor.execute("""INSERT OR IGNORE INTO ROOM (room_type) values (?);""",
                                           (room_type, availability, room_price))
                super().get_connection.commit()
                super().close_db()
                print("added successfully.")
            except Exception as e:
                print("An error occurred.", e)

        def delete(self, room_id):
            try:
                super().connect()
                super().get_cursor.execute("""DELETE FROM ROOM WHERE room_id = ?;""", (room_id,))
                super().get_connection.commit()
                super().close_db()
                print("Deleted successfully.")
            except Exception as e:
                print("An error occurred.", e)

        def fetch(self, room_id=None):
            try:
                super().connect()
                if room_id is not None:
                    return super().get_cursor.execute("""SELECT * FROM ROOM WHERE room_id = ?; """, (room_id,)).fetchall()
                else:
                    return super().get_cursor.execute("""SELECT * FROM ROOM WHERE room_id; """).fetchall()
            except Exception as e:
                print("An error occurred.", e)
            finally:
                super().close_db()

        def reset_database(self):
            sql = """
                    DROP TABLE IF EXISTS ROOM;

                    CREATE TABLE ROOM (
                        room_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                        room_type TEXT NOT NULL UNIQUE,
                        availability INTEGER NOT NULL,
                        room_price INTEGER NOT NULL UNIQUE
                        );
                        
                    INSERT INTO ROOM (room_type, availability, room_price) VALUES 
                    ('Penthouse', 10, 220),
                    ('King Deluxe Bedroom', 20, 180),
                    ('Queen Deluxe Bedroom', 20, 150),
                    ('King Standard Bedroom', 30, 120),
                    ('Queen Standard Bedroom', 50, 100);
                    
                  """
            super().execute_script(sql)

room = Room()
room.fetch()
db = DBbase

class Window(DBbase):

    def __init__(self):
        super().__init__("RoomDB.sqlite")

    def main_window(self):

        print("---------- Welcome ----------")
        print("1. Check availability")
        print("2. Make reservation")
        main_select = int(input())
        if main_select == 1:
            print("---------- Welcome ----------")
            print("1. Penthouse")
            print("2. King Deluxe Bedroom")
            print("3. Queen Deluxe Bedroom")
            print("4. King Standard Bedroom")
            print("5. Queen Standard Bedroom")
            print("Format: ID, Type, Availability, Price")
            check_select = int(input("Please make a selection"))
            if check_select == 1:
                print(room.fetch(1))
            elif check_select == 2:
                print(room.fetch(2))
            elif check_select == 3:
                print(room.fetch(3))
            elif check_select == 4:
                print(room.fetch(4))
            elif check_select == 5:
                print(room.fetch(5))
            else:
                print("Error")
        elif main_select == 2:
            print("---------- Welcome ----------")
            print("1. Penthouse")
            print("2. King Deluxe Bedroom")
            print("3. Queen Deluxe Bedroom")
            print("4. King Standard Bedroom")
            print("5. Queen Standard Bedroom")
            reservation_select = int(input("Please select the room type"))
            if reservation_select == 1:
                super().connect()
                time_leave = input("Please enter the date you leave the hotel: ('yyyy-mm-dd')")
                par_time = datetime.strptime(time_leave, '%Y-%m-%d')
                if par_time == datetime.now():
                    super().execute_script("""
                    UPDATE ROOM SET availability = availability + 1 WHERE room_id = 1;
                    """)
                else:
                    pass
                super().execute_script("""
                    UPDATE ROOM SET availability = availability - 1 WHERE room_id = 1;
                    """)
                print("Successful")
                super().close_db()
            elif reservation_select == 2:
                super().connect()
                time_leave = input("Please enter the date you leave the hotel: ('yyyy-mm-dd')")
                par_time = datetime.strptime(time_leave, '%Y-%m-%d')
                if par_time == datetime.now():
                    super().execute_script("""
                                    UPDATE ROOM SET availability = availability + 1 WHERE room_id = 2;
                                    """)
                else:
                    pass
                super().execute_script("""
                            UPDATE ROOM SET availability = availability - 1 WHERE room_id = 2;
                            """)
                print("Successful")
                super().close_db()
            elif reservation_select == 3:
                super().connect()
                time_leave = input("Please enter the date you leave the hotel: ('yyyy-mm-dd')")
                par_time = datetime.strptime(time_leave, '%Y-%m-%d')
                if par_time == datetime.now():
                    super().execute_script("""
                                    UPDATE ROOM SET availability = availability + 1 WHERE room_id = 3;
                                    """)
                else:
                    pass
                super().execute_script("""
                            UPDATE ROOM SET availability = availability - 1 WHERE room_id = 3
                            """)
                print("Successful")
                super().close_db()
            elif reservation_select == 4:
                super().connect()
                time_leave = input("Please enter the date you leave the hotel: ('yyyy-mm-dd')")
                par_time = datetime.strptime(time_leave, '%Y-%m-%d')
                if par_time == datetime.now():
                    super().execute_script("""
                                    UPDATE ROOM SET availability = availability + 1 WHERE room_id = 4;
                                    """)
                else:
                    pass
                super().execute_script("""
                            UPDATE ROOM SET availability = availability - 1 WHERE room_id = 4
                            """)
                print("Successful")
                super().close_db()
            elif reservation_select == 5:
                super().connect()
                time_leave = input("Please enter the date you leave the hotel: ('yyyy-mm-dd')")
                par_time = datetime.strptime(time_leave, '%Y-%m-%d')
                if par_time == datetime.now():
                    super().execute_script("""
                                    UPDATE ROOM SET availability = availability + 1 WHERE room_id = 5;
                                    """)
                else:
                    pass
                super().execute_script("""
                            UPDATE ROOM SET availability = availability - 1 WHERE room_id = 5
                            """)
                print("Successful")
                super().close_db()
            else:
                print("Error")

window = Window()
window.main_window()










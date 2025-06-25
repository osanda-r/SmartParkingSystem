# SQLite database manager
import sqlite3

class DatabaseManager:
    def __init__(self, db_file="parking.db"):
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
        self._create_tables()

    def _create_tables(self):
        c = self.conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS spots (
            spot_id TEXT PRIMARY KEY,
            is_occupied INTEGER,
            vehicle_id TEXT
        )""")
        self.conn.commit()

    def occupy_spot(self, spot_id, vehicle_id):
        c = self.conn.cursor()
        c.execute("INSERT OR REPLACE INTO spots (spot_id, is_occupied, vehicle_id) VALUES (?, ?, ?)",
                  (spot_id, 1, vehicle_id))
        self.conn.commit()

    def vacate_spot(self, spot_id):
        c = self.conn.cursor()
        c.execute("UPDATE spots SET is_occupied = 0, vehicle_id = NULL WHERE spot_id = ?", (spot_id,))
        self.conn.commit()

    def get_all_spots(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM spots")
        return [dict(zip(['spot_id', 'is_occupied', 'vehicle_id'], row)) for row in c.fetchall()]

    def vacate_all_spots(self):
        c = self.conn.cursor()
        c.execute("UPDATE spots SET is_occupied = 0, vehicle_id = NULL")
        self.conn.commit()

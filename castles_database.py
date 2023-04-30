import sqlite3


class CastleDB:
    def create_table_preview(self):
        self.con = sqlite3.connect("castles.db")
        self.cur = self.con.cursor()

        self.cur.execute("""CREATE TABLE IF NOT EXISTS preview (
        id INTEGER PRIMARY KEY,
        name TEXT,
        preview_img TEXT,
        preview_info TEXT,
        page_src TEXT)""")

        self.con.commit()
        self.con.close()

    def get_castles(self):
        self.con = sqlite3.connect("castles.db")
        self.cur = self.con.cursor()

        castles = self.cur.execute("""SELECT * FROM preview""").fetchall()

        self.con.close()
        return castles

    def get_castle(self, castle_src):
        self.con = sqlite3.connect("castles.db")
        self.cur = self.con.cursor()

        page_src = "/castles/" + castle_src
        castle = self.cur.execute("""SELECT * FROM preview WHERE page_src=?""", (page_src,)).fetchone()

        self.con.close()
        return castle

    def add_castle(self, name, preview_img, preview_info, page_src):
        self.con = sqlite3.connect("castles.db")
        self.cur = self.con.cursor()

        self.cur.execute("""INSERT INTO preview (name, preview_img, preview_info, page_src) VALUES (?, ?, ?, ?)""",
                         (name, preview_img, preview_info, page_src))

        self.con.commit()
        self.con.close()

    def create_table_main(self):
        self.con = sqlite3.connect("castles.db")
        self.cur = self.con.cursor()

        self.cur.execute("""CREATE TABLE IF NOT EXISTS main (
        id INTEGER,
        name TEXT,
        paragraphs TEXT)""")

        self.con.commit()
        self.con.close()


if __name__ == "__main__":
    castle = CastleDB()
    castle.create_table_main()

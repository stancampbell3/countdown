import duckdb

class WordsDb:
    def __init__(self, db_path=':memory:'):
        self.conn = duckdb.connect(database=db_path)
        self.create_tables()

    def create_tables(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS nine_letter_words (
                word TEXT PRIMARY KEY
            )
        ''')
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS valid_words (
                word TEXT PRIMARY KEY,
                length INTEGER
            )
        ''')

    def insert_nine_letter_word(self, word):
        self.conn.execute('''
            INSERT INTO nine_letter_words (word) VALUES (?)
        ''', (word,))

    def insert_valid_word(self, word):
        self.conn.execute('''
            INSERT INTO valid_words (word, length) VALUES (?, ?)
        ''', (word, len(word)))

    def get_nine_letter_words(self):
        return self.conn.execute('SELECT word FROM nine_letter_words').fetchall()

    def get_valid_words(self, length=None):
        if length:
            return self.conn.execute('SELECT word FROM valid_words WHERE length = ?', (length,)).fetchall()
        return self.conn.execute('SELECT word FROM valid_words').fetchall()

    def seed_words_with_valid_english_words(self):
        from core.susie_dent import SusieDent
        susie = SusieDent()
        words = susie.get_valid_english_words()  # Assuming this method returns a list of valid words
        for word in words:
            if len(word) == 9:
                self.insert_nine_letter_word(word)
            else:
                self.insert_valid_word(word)

    def save_words_to_csv(self, csv_path):
        import csv
        from core.susie_dent import SusieDent
        susie = SusieDent()
        valid_words = susie.get_valid_english_words()
        nine_letter_words = [(''.join(word),) for word in valid_words if len(word) == 9]

        with open(f"{csv_path}/nine_letter_words.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['word'])
            writer.writerows(nine_letter_words)

        with open(f"{csv_path}/valid_words.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['word', 'length'])
            writer.writerows([(''.join(word), len(word)) for word in valid_words])
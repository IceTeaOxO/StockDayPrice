import sqlite3


class StockDB:
    def __init__(self,dbfile):
        self.conn = sqlite3.connect(dbfile)
        self.cursor = self.conn.cursor()
        
#ID INTEGER PRIMARY KEY AUTOINCREMENT,
    def create_day_price_table(self,table_name):
        create_query = f'''CREATE TABLE {table_name}
             (id INTEGER PRIMARY KEY,
             date TEXT NOT NULL,
             stock_id TEXT NOT NULL,
             Trading_Volume INTEGER NOT NULL,
             Trading_money INTEGER NOT NULL,
             open REAL NOT NULL,
             max REAL NOT NULL,
             min REAL NOT NULL,
             close REAL NOT NULL,
             spread REAL NOT NULL,
             Trading_turnover INTEGER NOT NULL);'''
        self.cursor.execute(create_query)
    
    def create_tick_table(self,table_name):
        create_query = f'''CREATE TABLE {table_name}
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              date TEXT,
              stock_id TEXT,
              deal_price REAL,
              volume INTEGER,
              Time TEXT,
              TickType TEXT)'''
        self.cursor.execute(create_query)
        
    def create_taiwan_stock_info_table(self,table_name):
        create_query = f'''CREATE TABLE {table_name}
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              industry_category TEXT,
              stock_id TEXT,
              stock_name TEXT,
              type TEXT,
              date TEXT)'''
        self.cursor.execute(create_query)
        
    def insert_day_price_data(self, table_name, data):
        # print("DATA=",data)
        self.cursor.execute(f"INSERT INTO {table_name} (date, stock_id, Trading_Volume, Trading_money, open, max, min, close, spread, Trading_turnover) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
        self.conn.commit()
        
    def insert_tick_data(self, table_name, data):
        # print("DATA=",data)
        self.cursor.execute(f"INSERT INTO {table_name} (date,stock_id,deal_price,volume,Time,TickType) VALUES (?, ?, ?, ?, ?, ?)", data)
        self.conn.commit()
        
    def insert_taiwan_stock_info_data(self, table_name, data):
        # print("DATA=",data)
        self.cursor.execute(f"INSERT INTO {table_name} (industry_category,stock_id,stock_name,type,date) VALUES (?, ?, ?, ?, ?)", data)
        self.conn.commit()
    
    def select_data(self,table_name,fields=None,condition=None,limit=99999,offset=0):
        if fields is None:
            fields = ['*']
        select_query = f'''SELECT DISTINCT {fields} FROM {table_name}'''
        if condition is not None:
            select_query += f' WHERE {condition} '
        select_query += f' LIMIT {limit} OFFSET {offset};'
        # print(select_query)
        self.cursor.execute(select_query)
        return self.cursor.fetchall()
    
    def __del__(self):
        self.cursor.close()
        self.conn.close()
    
    def clear_table(self,table_name):
        self.cursor.execute('''DELETE FROM {}'''.format(table_name))
        self.conn.commit()
        

# db = StockDB('Stock.db')
# db.create_day_price_table('StockDayPrice')
# db.create_taiwan_stock_info_table('TaiwanStockID')
# db.create_tick_table('StockTick')



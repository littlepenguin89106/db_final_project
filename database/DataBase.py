from configparser import ConfigParser
from pymysql import Error
import pymysql

class DataBase:
    def __init__(self):
        self._conn = self.connect()
        self._cursor = self._conn.cursor(pymysql.cursors.DictCursor)
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def read_db_config(self, filename="config.ini", section="mysql"):
        """ Read database configuration file and return a dictionary object
        :param filename: name of the configuration file
        :param section: section of database configuration
        :return: a dictionary of databases parameters
        """
        parser = ConfigParser()
        parser.read(filename)

        db = {}
        if parser.has_section(section):
            items = parser.items(section)
            for item in items:
                db[item[0]] = item[1]
        else:
            raise Exception("{0} not found in the {1} file".format(section, filename))

        return db

    def connect(self):
        """ Connect to MySQL database """
        conn = None
        try:
            print("Connecting to MySQL database...")
            conn = pymysql.connect(host="localhost",
                                    database="team8",
                                    user="root",
                                    password="Qaz40847038S")
            if conn.open:
                print("Connection established.")
            else:
                print("Connection failed.")
        except Error as e:
            print(e)
        return conn
    
    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()
    
    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()
    
    def execute(self, query, args=None):
        self.cursor.execute(query, args or ())
    
    def fetchall(self):
        return self.cursor.fetchall()
    
    def fetchone(self):
        return self.cursor.fetchone()
    
    def query(self, query, args=None):
        self.cursor.execute(query, args or ())
        return self.fetchall()
from configparser import ConfigParser
from pymysql import Error
import pymysql

class DataBase:
    def __init__(self):
        self._conn = self.connect()
        self._cursor = self._conn.cursor()
    
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
            conn = pymysql.connect(**self.read_db_config())
            if conn.open():
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
    
    def add_task(self, name, description):
        add_task =  "INSERT INTO Subtask(name, description)" \
                    "VALUES(%s, %s)"
        data_task = (name, description)

        try:
            self.cursor.execute(add_task, data_task)
        except Error as error:
            print(error)

    def add_subtask(self, task_id, name, description):
        add_task =  "INSERT INTO Subtask(task_id, name, description)" \
                    "VALUES(%s, %s, %s)"
        data_task = (task_id, name, description)

        try:
            self.cursor.execute(add_task, data_task)
        except Error as error:
            print(error)

    def add_algo(self, name, description, paper_id_list=None, ds_id_list=None):
        add_algo = "INSERT INTO Algorithm(name, description) " \
                   "VALUES(%s, %s)"
        data_algo = (name, description)

        try:
            self.cursor.execute(add_algo, data_algo)
            algo_id = self.cursor.lastrowid

            if paper_id_list is not None:
                add_algo_paper = "INSERT INTO algo_paper(algo_id, paper_id)" \
                                 "VALUES(%s, %s)"
                for paper_id in paper_id_list:
                    data_algo_paper = (algo_id, paper_id)
                    self.cursor.execute(add_algo_paper, data_algo_paper)
            
            if ds_id_list is not None:
                add_uses = "INSERT INTO uses(algo_id, ds_id)" \
                           "VALUES(%s, %s)"
                for ds_id in ds_id_list:
                    data_uses = (algo_id, ds_id)
                    self.cursor.execute(add_uses, data_uses)

            self.connection.commit()
        except Error as error:
            print(error)

    def add_paper(self, name, author, publication, published_date, algo_id_list, ds_id_list):
        add_paper = "INSERT INTO Paper(name, author, publication, published_date) " \
                    "VALUES(%s, %s, %s, %s)"
        data_paper = (name, author, publication, published_date)

        try:
            self.cursor.execute(add_paper, data_paper)
            paper_id = self.cursor.lastrowid

            if algo_id_list is not None:
                add_algo_paper = "INSERT INTO algo_paper(algo_id, paper_id)" \
                                 "VALUES(%s, %s)"
                for algo_id in algo_id_list:
                    data_algo_paper = (algo_id, paper_id)
                    self.cursor.execute(add_algo_paper, data_algo_paper)
            
            if ds_id_list is not None:
                add_ds_paper = "INSERT INTO ds_paper(ds_id, paper_id)" \
                               "VALUES(%s, %s)"
                for ds_id in ds_id_list:
                    data_ds_paper = (ds_id, paper_id)
                    self.cursor.execute(add_ds_paper, data_ds_paper)

            self.connection.commit()
        except Error as error:
            print(error)

    def add_dataset(self, name, description, size, attribute, algo_id_list, paper_id_list):
        add_ds = "INSERT INTO Dataset(name, description, size, attribute) " \
                 "VALUES(%s, %s, %s, %s)"
        data_ds = (name, description, size, attribute)

        try:
            self.cursor.execute(add_ds, data_ds)
            ds_id = self.cursor.lastrowid

            if algo_id_list is not None:
                add_uses = "INSERT INTO uses(algo_id, ds_id)" \
                           "VALUES(%s, %s)"
                for algo_id in algo_id_list:
                    data_uses = (algo_id, ds_id)
                    self.cursor.execute(add_uses, data_uses)
            
            if paper_id_list is not None:
                add_ds_paper = "INSERT INTO ds_paper(ds_id, paper_id)" \
                               "VALUES(%s, %s)"
                for paper_id in paper_id_list:
                    data_ds_paper = (ds_id, paper_id)
                    self.cursor.execute(add_ds_paper, data_ds_paper)

            self.connection.commit()
        except Error as error:
            print(error)

    def add_bulletin(self, author, publication, paper_id_list):
        add_bulletin = "INSERT INTO Bulletin(author, publication)" \
                       "VALUES(%s, %s)"
        data_bulletin = (author, publication)

        try:
            self.cursor.execute(add_bulletin, data_bulletin)
            bulletin_id = self.cursor.lastrowid
            
            if paper_id_list is not None:
                add_edit = "INSERT INTO edit(paper_id, bulletin_id)" \
                           "VALUES(%s, %s)"
                for paper_id in paper_id_list:
                    data_edit = (paper_id, bulletin_id)
                    self.cursor.execute(add_edit, data_edit)

            self.connection.commit()
        except Error as error:
            print(error)

    def get_task(self, name):
        pass

    def get_subtask(self, name):
        pass

    def get_algo(self, name):
        pass

    def get_paper(self, title):
        pass

    def get_dataset(self, name):
        pass
    
    def update_task(self):
        pass

    def update_subtask(self):
        pass

    def update_paper(self):
        pass

    def update_dataset(self):
        pass

if __name__ == "__main__":
    with DataBase() as db:
        db.add_algo("bubble_sort", "a very simple sort")
        algos = db.query('SELECT * FROM Algorithm')
        db.execute('DELETE FROM Algorithm')
        print(algos)
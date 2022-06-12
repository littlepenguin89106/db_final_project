import mysql.connector
from mysql.connector import Error
from configparser import ConfigParser
from pathlib import Path

class DataBase:
    def __init__(self):
        self._conn = self.connect()
        self._cursor = self._conn.cursor()

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
            conn = mysql.connector.connect(**self.read_db_config())
            if conn.is_connected():
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

    def add_algo(self, name, description, paper_id_list=None, ds_id_list=None):
        add_algo = "INSERT INTO Algorithm(name, description) " \
                   "VALUES(%s, %s)"
        data_algo = (name, description)

        try:
            self.cursor.execute(add_algo, data_algo)
            algo_id = self.cursor.lastrowid

            if paper_id_list is not None:
                add_algo_paper = "INSERT INTO algo_paper(algorithm_id, paper_id)" \
                                 "VALUES(%s, %s)"
                for paper_id in paper_id_list:
                    data_algo_paper = (algo_id, paper_id)
                    self.cursor.execute(add_algo_paper, data_algo_paper)
            
            if ds_id_list is not None:
                add_Uses = "INSERT INTO Uses(algorithm_id, dataset_id)" \
                           "VALUES(%s, %s)"
                for ds_id in ds_id_list:
                    data_Uses = (algo_id, ds_id)
                    self.cursor.execute(add_Uses, data_Uses)

        except Error as error:
            print(error)

    def add_paper(self, author, publication, published_date, algo_id_list, ds_id_list):
        add_paper = "INSERT INTO Algorithm(author, publication, published_date) " \
                    "VALUES(%s, %s, %s)"
        data_paper = (author, publication, published_date)

        try:
            self.cursor.execute(add_paper, data_paper)
            paper_id = self.cursor.lastrowid

            if algo_id_list is not None:
                add_algo_paper = "INSERT INTO algo_paper(algorithm_id, paper_id)" \
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

        except Error as error:
            print(error)

    def add_dataset(self, name, description, size, attribute, algo_id_list, paper_id_list):
        add_ds = "INSERT INTO Algorithm(name, description, size, attribute) " \
                 "VALUES(%s, %s, %s, %s)"
        data_ds = (name, description, size, attribute)

        try:
            self.cursor.execute(add_ds, data_ds)
            ds_id = self.cursor.lastrowid

            if algo_id_list is not None:
                add_Uses = "INSERT INTO Uses(algorithm_id, dataset_id)" \
                           "VALUES(%s, %s)"
                for algo_id in algo_id_list:
                    data_Uses = (algo_id, ds_id)
                    self.cursor.execute(add_Uses, data_Uses)
            
            if paper_id_list is not None:
                add_ds_paper = "INSERT INTO ds_paper(ds_id, paper_id)" \
                               "VALUES(%s, %s)"
                for paper_id in paper_id_list:
                    data_ds_paper = (ds_id, paper_id)
                    self.cursor.execute(add_ds_paper, data_ds_paper)
        
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
                add_Edit = "INSERT INTO Edit(paper_id, bulletin_id)" \
                           "VALUES(%s, %s)"
                for paper_id in paper_id_list:
                    data_Edit = (paper_id, bulletin_id)
                    self.cursor.execute(add_Edit, data_Edit)
        
        except Error as error:
            print(error)


if __name__ == "__main__":
    db = DataBase()
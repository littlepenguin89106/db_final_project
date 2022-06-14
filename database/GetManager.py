from .DataBase import *

class GetManager(DataBase):
    def get_algo(self):
        result = list()
        try:
            self.cursor.execute("""
                SELECT algo_id, Algorithm.name as algo_name
                FROM Algorithm
            """)
            result = self.fetchall()
        except Error as error:
            print(error)
        return result

    def show_algo(self, algo_id):
        result = dict()
        try:
            query = """
                SELECT name as algo_name, description
                FROM Algorithm
                WHERE algo_id = %s
            """
            data = (algo_id,)
            result = self.query(query, data)
            
            query = """
                SELECT paper_id, Paper.name as paper_name
                FROM (SELECT * FROM Algorithm WHERE algo_id = %s) as algo
                NATURAL JOIN algo_paper
                NATURAL JOIN Paper
            """
            self.execute(query)
            result["paper_name"] = self.fetchall()
        except Error as error:
            print(error)
        return result

    def get_algo_info(self, algo_id):
        try:
            self.cursor.execute("""
                SELECT name as algo_name, description as algo_description
                FROM Algorithm
                WHERE algo_id = %s
            """, (algo_id,))
            result = self.fetchall()
        except Error as error:
            print(error)
        return result
    
    def exist_algo(self, algo_id):
        try:
            result = self.query("SELECT algo_id FROM Algorithm WHERE algo_id = %s", (algo_id,))
            if result is None:
                deletable = False
            else:
                deletable = True
        except Error as error:
            print(error)
        return deletable

    def get_paper(self):
        try:
            self.cursor.execute("""
                SELECT *
                FROM Paper
            """)
            result = self.fetchall()
        except Error as error:
            print(error)
        return result

    def show_paper(self, paper_id):
        result = dict()
        try:
            query = """
                SELECT *
                FROM Paper
                WHERE paper_id = %s
            """
            self.execute(query, (paper_id,))
            query_result = self.fetchone()
            result.update(query_result)

            query = """
                SELECT algo_id, name as algo_name
                FROM algo_paper
                NATURAL JOIN Algorithm
                WHERE paper_id = %s
            """
            self.execute(query, (paper_id,))
            result["algo"] = self.fetchall()

            query = """
                SELECT ds_id as data_id, name as data_name
                FROM ds_paper
                NATURAL JOIN Dataset
                WHERE paper_id = %s
            """
            self.execute(query, (paper_id,))
            result["dataset"] = self.fetchall()
        except Error as error:
            print(error)
        return result

    def get_bulletin(self):
        try:
            result = self.query("SELECT * FROM Bulletin")
        except Error as error:
            print(error)
        return result
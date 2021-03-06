from .DataBase import *
from datetime import datetime

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
            raise(error)
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
            self.execute(query, data)
            result = self.fetchone()
            
            query = """
                SELECT paper_id, Paper.name as paper_name
                FROM (SELECT * FROM algo_paper WHERE algo_id = %s) as ap
                NATURAL JOIN Paper
            """
            self.execute(query, data)
            result["paper_name"] = self.fetchall()
        except Error as error:
            print(error)
            raise(error)
        return result

    def get_algo_info(self, algo_id):
        try:
            self.cursor.execute("""
                SELECT name as algo_name, description as algo_description
                FROM Algorithm
                WHERE algo_id = %s
            """, (algo_id,))
            result = self.fetchone()
        except Error as error:
            print(error)
            raise(error)
        return result
    
    def exist_algo(self, algo_id):
        result = dict({"deletable": None})
        try:
            self.execute("SELECT algo_id FROM algo_paper WHERE algo_id = %s", (algo_id,))
            query_result = self.fetchone()
            if query_result is None:
                result["deletable"] = True
            else:
                result["deletable"] = False
        except Error as error:
            print(error)
            raise error
        return result

    def get_paper(self):
        try:
            self.cursor.execute("""
                SELECT *
                FROM Paper
            """)
            result = self.fetchall()
        except Error as error:
            print(error)
            raise(error)
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

            result['published_date'] = result['published_date'].strftime('%Y-%m-%d')
#            print(result['published_date'])

            query = """
                SELECT algo_id, name as algo_name
                FROM algo_paper
                NATURAL JOIN Algorithm
                WHERE paper_id = %s
            """
            self.execute(query, (paper_id,))
            result["algo"] = self.fetchall()

            query = """
                SELECT task_id, name as task_name
                FROM paper_task
                NATURAL JOIN Task
                WHERE paper_id = %s
            """
            self.execute(query, (paper_id,))
            result["task"] = self.fetchall()
        except Error as error:
            print(error)
            raise(error)
        return result

    def get_bulletin(self):
        try:
            result = self.query("SELECT * FROM Bulletin")
        except Error as error:
            print(error)
            raise(error)
        return result
    
    def get_task(self):
        try:
            result = self.query("SELECT task_id, name as task_name FROM Task")
        except Error as error:
            print(error)
            raise(error)
        return result

    def get_dataset(self, task_id):
        try:
            result = self.query("""
                SELECT ds_id as dataset_id, Dataset.name as dataset_name
                FROM ds_task
                NATURAL JOIN Dataset
                WHERE task_id = %s
            """, (task_id,))
        except Error as error:
            print(error)
            raise(error)
        return result
    
    def exist_dataset(self, ds_id):
        result = dict({"deletable": None})
        try:
            self.execute("SELECT ds_id FROM ds_task WHERE ds_id = %s", (ds_id,))
            query_result = self.fetchone()
            if query_result is None:
                result["deletable"] = True
            else:
                result["deletable"] = False
        except Error as error:
            print(error)
            raise(error)
        return result
    
    def get_all_dataset(self):
        try:
            result = self.query("""
                SELECT ds_id as dataset_id, description as dataset_description, name as dataset_name
                FROM Dataset
            """)
        except Error as error:
            print(error)
        return result

    def get_task_info(self, task_id):
        try:
            query = """
                SELECT name as task_name
                FROM Task
                WHERE task_id = %s
            """
            self.execute(query, (task_id,))
            result = self.fetchone()

            result["dataset"] = self.query("""
                SELECT ds_id as dataset_id, Dataset.name as dataset_name
                FROM ds_task
                NATURAL JOIN Dataset
                WHERE task_id = %s
            """, (task_id,))
        except Error as error:
            print(error)
        return result


    def get_dataset_info(self, ds_id):
        try:
            self.execute("""
                SELECT name, description, attribute
                FROM Dataset
                WHERE ds_id = %s
            """, (ds_id,))
            result = self.fetchone()
        except Error as error:
            print(error)
        return result
    
    def get_bulletin_info(self, bulletin_id):
        try:
            self.execute("""
                SELECT author, description
                FROM Bulletin
                WHERE bulletin_id = %s
            """, (bulletin_id,))
            result = self.fetchone()
        except Error as error:
            print(error)
            raise(error)
        return result

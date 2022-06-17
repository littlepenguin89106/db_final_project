from .DataBase import *

class DelManager(DataBase):
    def del_algo(self, algo_id):
        try:
            self.execute("""
                DELETE FROM Algorithm
                WHERE algo_id = %s
            """, (algo_id,))
            self.commit()
        except Error as error:
            print(error)

    def del_paper(self, paper_id):
        try:
            self.execute("""
                DELETE FROM algo_paper
                WHERE paper_id = %s
            """, (paper_id,))
            self.commit()

            self.execute("""
                DELETE FROM paper_task
                WHERE paper_id = %s
            """, (paper_id,))
            self.commit()

            self.execute("""
                DELETE FROM Paper
                WHERE paper_id = %s
            """, (paper_id,))
            self.commit()
        except Error as error:
            print(error)

    
    def del_bulletin(self, bulletin_id):
        try:
            self.execute("""
                DELETE FROM Bulletin
                WHERE bulletin_id = %s
            """, (bulletin_id,))
            self.commit()
        except Error as error:
            print(error)

    def del_dataset(self, ds_id):
        try:
            self.execute("""
                DELETE FROM Dataset
                WHERE ds_id = %s
            """, (ds_id,))
            self.commit()
        except Error as error:
            print(error)
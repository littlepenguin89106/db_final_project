from DataBase import *

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
                DELETE FROM Paper
                WHERE paper_id = %s
            """, (paper_id,))
            self.commit()
        except Error as error:
            print(error)
from DataBase import *

class AddManager(DataBase):
    def add_algo(self, name, description, task_id_list=None, paper_id_list=None):
        query = "INSERT INTO Algorithm(name, description) VALUES(%s, %s)"
        data = (name, description)

        try:
            self.execute(query, data)
            algo_id = self.cursor.lastrowid

            if task_id_list is not None:
                query = "INSERT INTO algo_task(algo_id, task_id) VALUES(%s, %s)"
                for task_id in task_id_list:
                    data = (algo_id, task_id)
                    self.execute(query, data)

            self.commit()

        except Error as error:
            print(error)
        
    def add_paper(self, name, author, publication, published_date, algo_id_list, ds_id_list):
        query = "INSERT INTO Paper(name, author, publication, published_date) VALUES(%s, %s, %s, %s)"
        data = (name, author, publication, published_date)

        try:
            self.execute(query, data)
            paper_id = self.cursor.lastrowid

            if algo_id_list is not None:
                query = "INSERT INTO algo_paper(algo_id, paper_id)" \
                        "VALUES(%s, %s)"
                for algo_id in algo_id_list:
                    data = (algo_id, paper_id)
                    self.execute(query, data)
            
            if ds_id_list is not None:
                query = "INSERT INTO ds_paper(ds_id, paper_id)" \
                        "VALUES(%s, %s)"
                for ds_id in ds_id_list:
                    data = (ds_id, paper_id)
                    self.execute(query, data)

            self.commit()
        except Error as error:
            print(error)

    def add_bulletin(self, author, description):
        query = "INSERT INTO Bulletin(author, description) VALUES(%s, %s)"
        data = (author, description)
        try:
            self.execute(query, data)
            self.commit()
        except Error as error:
            print(error)

# test only
if __name__ == "__main__":
    db = AddManager()
    db.add_algo("quik sort", "a faster sort")
    result = db.query("select name as algo_name from Algorithm")
    print(result)
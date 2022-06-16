from .DataBase import *

class AddManager(DataBase):
    def add_algo(self, name, description):
        query = "INSERT INTO Algorithm(name, description) VALUES(%s, %s)"
        data = (name, description)

        try:
            self.execute(query, data)
            self.commit()

        except Error as error:
            print(error)
        
    def add_paper(self, name, description, author, publication, published_date, algo_id_list, task_id_list):
        query = "INSERT INTO Paper(name, author, publication, published_date, description) VALUES(%s, %s, %s, %s, %s)"
        data = (name, author, publication, published_date, description)

        try:
            self.execute(query, data)
            paper_id = self.cursor.lastrowid

            if algo_id_list is not None:
                query = "INSERT INTO algo_paper(algo_id, paper_id)" \
                        "VALUES(%s, %s)"
                for algo_id in algo_id_list:
                    data = (algo_id["algo_id"], paper_id)
                    self.execute(query, data)
            
            if task_id_list is not None:
                query = "INSERT INTO paper_task(paper_id, task_id)" \
                        "VALUES(%s, %s)"
                for task_id in task_id_list:
                    data = (paper_id, task_id["task_id"])
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


    def add_dataset(self, name, description, attribute):
        query = "INSERT INTO Dataset(name, description, attribute) VALUES(%s, %s, %s)"
        data = (name, description, attribute)
        try:
            self.execute(query, data)
            self.commit();
        except Error as error:
            print(error)

# test only
if __name__ == "__main__":
    db = AddManager()
    db.add_algo("quick sort", "a faster sort")
    result = db.query("select name as algo_name from Algorithm")
    print(result)
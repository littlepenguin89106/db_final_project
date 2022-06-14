from DataBase import *

class AddManager(DataBase):
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

# test only
if __name__ == "__main__":
    db = AddManager()
    db.add_algo("quik sort", "a faster sort")
    result = db.query("select name as algo_name from Algorithm")
    print(result)
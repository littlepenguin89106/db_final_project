from .DataBase import *

class UpdateManager(DataBase):
    def update_algo_info(self, algo_id, name, description):
        try:
            query = """
                UPDATE Algorithm
                SET name = %s,
                    description = %s
                WHERE algo_id = %s
            """
            data = (name, description, algo_id)
            self.execute(query, data)
            self.commit()
        except Error as error:
            print(error)

    def update_paper_info(self, paper_id, name, author, publication, published_date, algo_id_list, ds_id_list):
        query = """
            UPDATE Paper
            SET name = %s,
                author = %s,
                pulication = %s,
                published_date = %s
            WHERE paper_id = %s
        """
        data = (name, author, publication, published_date, paper_id)

        try:
            self.execute(query, data)

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

    def update_bulletin_info(self, bulletin_id, author, description):
        try:
            query = """
                UPDATE Bulletin
                Set author = %s,
                    description = %s
                WHERE bulletin_id = %s
            """
            data = (author, description, bulletin_id)
            self.execute(query, data)
            self.commit()
        except Error as error:
            print(error)
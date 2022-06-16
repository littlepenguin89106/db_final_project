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

    def update_paper_info(self, paper_id, name, description, author, publication, published_date, algo_id_list, task_id_list):
        query = """
            UPDATE Paper
            SET name = %s,
                author = %s,
                publication = %s,
                published_date = %s,
                description = %s
            WHERE paper_id = %s
        """
        data = (name, author, publication, published_date, description, paper_id)

        try:
            self.execute(query, data)

            query = """
                DELETE FROM algo_paper
                WHERE paper_id = %s
            """
            self.execute(query, (paper_id,))

            if algo_id_list is not None:
                query = "INSERT INTO algo_paper(algo_id, paper_id)" \
                        "VALUES(%s, %s)"
                for algo_id in algo_id_list:
                    data = (algo_id["algo_id"], paper_id)
                    self.execute(query, data)
            
            query = """
                DELETE FROM paper_task
                WHERE paper_id = %s
            """
            self.execute(query, (paper_id,))

            if task_id_list is not None:
                query = "INSERT INTO paper_task(paper_id, task_id)" \
                        "VALUES(%s, %s)"
                for task_id in task_id_list:
                    data = (paper_id, task_id["task_id"])
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

    def update_dataset(self, ds_id, description, name):
        try:
            query = """
                UPDATE Dataset
                Set name = %s,
                    description = %s
                WHERE ds_id = %s
            """
            data = (name, description, ds_id)
            self.execute(query, data)
            self.commit()
        except Error as error:
            print(error)
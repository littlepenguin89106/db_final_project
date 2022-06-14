from database import *
from pathlib import Path
import json

data_path = Path(r'C:\Users\admit\Downloads\paperwithcode')

def insert_algos():
    with open(data_path / 'methods.json' ,'r') as f:
        methods = json.load(f)    

    add_m = AddManager()

    for m in methods:
        add_m.add_algo(m['name'],m['description'])

    print('insert algo success')

def insert_papers():
    add_m = AddManager()

    with open(data_path / 'extract_paper_seq2seq.json','r') as f:
        papers = json.load(f)

    for p in papers:
        cmd = 'insert into Paper(name,author,publication,published_date,description) values(%s,%s,%s,%s,%s)'
        add_m.execute(cmd,(p['title'],p['authors'][0],'',p['date'],p['abstract']))

        cmd = 'select paper_id from Paper where name=%s'
        add_m.execute(cmd,p['title'])
        paper_id = add_m.fetchone()['paper_id']

        for m in p['methods']:
            cmd = 'select algo_id from Algorithm where name=%s' 
            add_m.execute(cmd,(m['name'],))
            algo_id = add_m.fetchone()
            try:
                if algo_id:
                    cmd = 'insert algo_paper(algo_id,paper_id) values(%s,%s)'
                    add_m.execute(cmd,(algo_id['algo_id'],paper_id))
                else:
                    cmd = 'insert into Algorithm(name,description) values(%s,%s)'
                    add_m.execute(cmd,(m['name'],m['description']))

                    cmd = 'select algo_id from Algorithm where name=%s'
                    add_m.execute(cmd,(m['name']))
                    algo_id = add_m.fetchone()['algo_id']
                    cmd = 'insert algo_paper(algo_id,paper_id) values(%s,%s)'
                    add_m.execute(cmd,(algo_id,paper_id))
            except:
                print(p['title'])
                break

        for t in p['tasks']:
            try:
                cmd = 'select task_id from Task where name=%s'
                add_m.execute(cmd,(t,))
                task_id = add_m.fetchone()
                if task_id:
                    cmd = 'insert into paper_task(paper_id,task_id) values(%s,%s)'
                    add_m.execute(cmd,(paper_id,task_id['task_id']))
                else:
                    cmd = 'insert into task(name) values(%s)'
                    add_m.execute(cmd,(t,))

                    cmd = "select task_id from task where name=%s"
                    add_m.execute(cmd,(t,))
                    task_id = add_m.fetchone()['task_id']
                    cmd = 'insert into paper_task(paper_id,task_id) values(%s,%s)'
                    add_m.execute(cmd,(paper_id,task_id))
            except:
                print(p['title'])
                break


def insert_dataset():
    add_m = AddManager()

    with open(data_path / 'datasets.json','r') as f:
        ds = json.load(f)

    max_num = 500
    
    for d in ds[:max_num]:
        cmd = 'INSERT INTO Dataset(name, description, attribute) VALUES(%s, %s, %s);'
        attr = d['modalities'][0] if d['modalities'] else ''
        
        add_m.execute(cmd,(d['name'],d['description'],attr))

        cmd = 'select ds_id from Dataset where name=%s'
        add_m.execute(cmd,(d['name']))
        ds_id = add_m.fetchone()['ds_id']


        for t in d['tasks']:
            try:
                cmd = "select task_id from Task where name=%s"
                add_m.execute(cmd,(t['task'],))
                result = add_m.fetchone()
                if result:
                    cmd = 'insert into ds_task(task_id,ds_id) values(%s,%s)'
                    add_m.execute(cmd,(result['task_id'],ds_id))
                else:
                    cmd = 'insert into task(name) values(%s)'
                    add_m.execute(cmd,(t['task'],))

                    cmd = "select task_id from task where name=%s"
                    add_m.execute(cmd,(t['task'],))
                    result = add_m.fetchone()
                    cmd = 'insert into ds_task(task_id,ds_id) values(%s,%s)'
                    add_m.execute(cmd,(result['task_id'],ds_id))
            except:
                print(d['name'])
                break


if __name__ == "__main__":
    insert_algos()
    print('insert algorithm success')
    insert_dataset()
    print('insert dataset success')
    insert_papers()
    print('insert paper success')

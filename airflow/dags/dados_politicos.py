from airflow import DAG
from airflow.operators.bash import BashOperator
import os


from datetime import datetime

path_temp_dir = os.path.abspath("./dados/temp")

with DAG(
    dag_id = 'dados_politicos',
    description = 'Extração de dados políticos da câmara dos deputados',
    start_date= datetime.today()
) as dag:
    
    task_1 = BashOperator(
        task_id = 'mkdir_temp',
        bash_command=  'mkdir {}'.format(path_temp_dir)
    )




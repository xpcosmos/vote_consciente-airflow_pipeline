from airflow import DAG
from airflow.operators.bash import BashOperator
import os


from datetime import datetime

deputados_url = 'https://dadosabertos.camara.leg.br/api/v2/deputados'
path_temp_dir = os.path.abspath("./dados/temp")

with DAG(
    dag_id = 'dados_politicos',
    description = 'Extração de dados políticos da câmara dos deputados',
    start_date= datetime.today()
) as dag:
    
    task_1 = BashOperator(
        task_id = 'mkdir_temp',
        bash_command=  '[[ -d {} ]] && exit 0 || mkdir {}'.format(path_temp_dir, path_temp_dir),
        skip_exit_code= 2
    )

    tasK_2 = BashOperator(
        task_id = 'download_deputados',
        bash_command = 'curl "{}" -o {}/deputados.json'.format(deputados_url, path_temp_dir)
    )
    
    task_1 >> tasK_2
    




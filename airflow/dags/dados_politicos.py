from airflow import DAG


from datetime import datetime


with DAG(
    dag_id = 'dados_politicos',
    description = 'Extração de dados políticos da câmara dos deputados',
    start_date= datetime.today()
) as dag:
    pass




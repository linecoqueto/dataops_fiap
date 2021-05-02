# Importando as bibliotecas que vamos utilizar
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
# definição de argumentos básicos
default_args = {
'owner': 'GRUPO4',
'depends_on_past': False,
'start_date': datetime(2021, 5, 2),
'retries': 0
}
# Nomeando a DAG e definindo quando ela vai ser executada - semanalmente
with DAG(
'Jobs-data-ops-semanal',
schedule_interval=:'@weekly',
catchup=False,
default_args=default_args
) as dag:
# Definindo as tarefas que a DAG vai executar, nesse caso a execução de dois programas Python, chamando sua execução por comandos bash
# O operador Bash, também pode ser utilizado para executar jobs Talend via Sh
    t1 = BashOperator(
    task_id='CamadaCurated_dataset_produtos',
    bash_command="""
    cd $AIRFLOW_HOME/dags/dataops/curated/dataset_semanal_produtos/dataset_produtos_run.sh
    """)
# Definindo o padrão de execução:
t1

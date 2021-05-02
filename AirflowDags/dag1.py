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
# Nomeando a DAG e definindo quando ela vai ser executada - diariamente
with DAG(
'Jobs-data-ops-diario',
schedule_interval=:'@daily',
catchup=False,
default_args=default_args
) as dag:
# Definindo as tarefas que a DAG vai executar, nesse caso a execução de dois programas Python, chamando sua execução por comandos bash
# O operador Bash, também pode ser utilizado para executar jobs Talend via Sh
    t1 = BashOperator(
    task_id='CamadaRawIngestao',
    bash_command="""
    cd $AIRFLOW_HOME/dags/BuildsJobTalend/Raw/ingestao/ingestao_run.sh
    """)
    t2 = BashOperator(
    task_id='CamadaHarmonizedCliente',
    bash_command="""
    cd $AIRFLOW_HOME/dags/BuildsJobTalend/Harmonized/cliente_limpo/cliente_limpo_run.sh
    """)
	t3 = BashOperator(
    task_id='CamadaHarmonizedProduto',
    bash_command="""
    cd $AIRFLOW_HOME/dags/BuildsJobTalend/Harmonized/produto_limpo/produto_limpo_run.sh
    """)
	t4 = BashOperator(
    task_id='CamadaHarmonizedVendas',
    bash_command="""
    cd $AIRFLOW_HOME/dags/BuildsJobTalend/Harmonized/vendas_limpo;vendas_limpo_run.sh
    """)
	t5 = BashOperator(
    task_id='CamadaCuratedRelatorioVendas',
    bash_command="""
    cd $AIRFLOW_HOME/dags/BuildsJobTalend/Curated/relatorio_vendas/relatorio_vendas_run.sh
    """)
# Definindo o padrão de execução:
t1 >> t2 >> t3 >> t4 >> t5

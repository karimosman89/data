from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago


my_dag = DAG(
    dag_id='my_dag_of_the_morning',
    description='My DAG to know what to do in the morning',
    tags=['tutorial', 'datascientest'],
    schedule_interval=None,
    default_args={
        'owner': 'airflow',
        'start_date': days_ago(2),
    }
)


def print_text(text):
    print(text)


texts = [
    'Put on pants',
    'Put on right sock',
    'Put on right shoe',
    'Put on left sock',
    'Put on left shoe',
    'Go out'
]

ids = [
    'pants',
    'right_sock',
    'right_shoe',
    'left_sock',
    'left_shoe',
    'go_out'
]

task1, task2, task3, task4, task5, task6 = [
    PythonOperator(
        dag=my_dag,
        task_id=i,
        python_callable=print_text,
        op_kwargs={
            'text': t
        }
    ) for t, i in zip(texts, ids)
]

task1 >> task2
task1 >> task4

task2 >> task3

task4 >> task5

task3 >> task6
task5 >> task6
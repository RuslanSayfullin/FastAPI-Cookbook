from conftest import TEST_TASKS_CSV
from models import Task, TaskWithID
from operations import (
    create_task,
    get_next_id,
    modify_task,
    read_all_tasks,
    read_task,
    remove_task,
    write_task_into_csv,
)


import pytest
from src.task_manager.manager import TaskManager

@pytest.fixture
def temp_manager(tmp_path):
    db_file = tmp_path / "tasks.json"
    return TaskManager(str(db_file))

def test_add_task(temp_manager):
    task = temp_manager.add_task("Write some tests")
    assert task.id == 1
    assert task.title == "Write some tests"
    assert task.completed is False
    assert len(temp_manager.list_tasks()) == 1

def test_add_empty_task_raises_error(temp_manager):
    with pytest.raises(ValueError):
        temp_manager.add_task("")
    with pytest.raises(ValueError):
        temp_manager.add_task("   ")

def test_complete_task(temp_manager):
    task = temp_manager.add_task("Task to complete")
    assert temp_manager.complete_task(task.id) is True
    assert temp_manager.get_task(task.id).completed is True

def test_complete_nonexistent_task(temp_manager):
    assert temp_manager.complete_task(999) is False

def test_delete_task(temp_manager):
    task = temp_manager.add_task("Task to delete")
    assert temp_manager.delete_task(task.id) is True
    assert len(temp_manager.list_tasks()) == 0

def test_delete_nonexistent_task(temp_manager):
    assert temp_manager.delete_task(999) is False

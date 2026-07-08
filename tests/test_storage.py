import os
from src.task_manager.models import Task
from src.task_manager.storage import StorageHandler

def test_storage_loads_empty_list_if_no_file(tmp_path):
    db_file = tmp_path / "test_tasks.json"
    storage = StorageHandler(str(db_file))
    assert storage.load_tasks() == []

def test_storage_save_and_load(tmp_path):
    db_file = tmp_path / "test_tasks.json"
    storage = StorageHandler(str(db_file))
    
    tasks = [
        Task(id=1, title="Test 1"),
        Task(id=2, title="Test 2", completed=True)
    ]
    
    storage.save_tasks(tasks)
    
    assert os.path.exists(db_file)
    
    loaded = storage.load_tasks()
    assert len(loaded) == 2
    assert loaded[0].id == 1
    assert loaded[0].title == "Test 1"
    assert loaded[0].completed is False
    assert loaded[1].id == 2
    assert loaded[1].title == "Test 2"
    assert loaded[1].completed is True

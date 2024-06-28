import pytest
from main import TodoList

def test_add_task():
    todo_list = TodoList()
    todo_list.add_task("Task 1")
    assert "Task 1" in todo_list.get_tasks()
    with pytest.raises(ValueError):
        todo_list.add_task("")

def test_remove_task():
    todo_list = TodoList()
    todo_list.add_task("Task 1")
    todo_list.remove_task("Task 1")
    assert "Task 1" not in todo_list.get_tasks()
    with pytest.raises(ValueError):
        todo_list.remove_task("Task 2")

def test_get_tasks():
    todo_list = TodoList()
    todo_list.add_task("Task 1")
    todo_list.add_task("Task 2")
    assert todo_list.get_tasks() == ["Task 1", "Task 2"]

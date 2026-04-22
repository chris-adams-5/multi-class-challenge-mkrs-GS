import pytest

from lib.todo import Todo

"""
On Instantiation
A task can be set
the complete property is set to False
"""
def test_todo_initially_task_set_complete_False():
    task = "Know where towel is"
    todo = Todo(task)
    assert todo.task == "Know where towel is"
    assert todo.complete == False

"""
On Instantiation
If task is not a str
throws an error
"""
def test_todo_task_not_str_error():
    with pytest.raises(Exception) as err:
        todo = Todo(None)
    assert str(err.value) == "Error Todo takes a string"

"""
A task can be
marked as complete
task property set to true
the task in unchanged
"""
def test_todo_marked_complete():
    task = "Know where towel is"
    todo = Todo(task)
    todo.mark_complete()
    assert todo.task == "Know where towel is"
    assert todo.complete == True

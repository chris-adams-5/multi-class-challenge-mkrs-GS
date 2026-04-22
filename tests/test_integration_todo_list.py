import pytest

from lib.todo import Todo
from lib.todo_list import TodoList

"""
todo_list Intially has an
empty list of todos
"""
def test_td_list_init_empty_list():
    td_list = TodoList()
    assert td_list.list == []

"""
Add a todo to 
todo_list
"""

def test_td_list_add_a_todo():
    todo = Todo("Know where towel is")
    td_list = TodoList()
    td_list.add(todo)
    assert td_list.list == [todo]

"""
Throws an Error if you try
to add anything other than
a todo
"""

def test_td_list_add_not_todo_error():
    td_list = TodoList()
    with pytest.raises(Exception) as err:
        td_list.add("I am not a Todo")
    assert str(err.value) == "Error TodoList.add receives object of type Todo"


"""
Add multiple todos to 
todo_list
"""

def test_td_list_add_multiple_todos():
    todo_1 = Todo("Know where towel is")
    todo_2 = Todo("Don't Panic!")
    td_list = TodoList()
    td_list.add(todo_1)
    td_list.add(todo_2)
    assert td_list.list == [todo_1,todo_2]

"""
Add multiple todos to 
add at the same time
"""

def test_td_list_add_multiple_todos_in_one_add():
    todo_1 = Todo("Know where towel is")
    todo_2 = Todo("Don't Panic!")
    td_list = TodoList()
    td_list.add(todo_1, todo_2)
    assert td_list.list == [todo_1,todo_2]

"""
incomplete returns a list
of incomplete tasks
"""
def test_td_list_incomplete_return_incomplete_tasks():
    todo_1 = Todo("Know where towel is")
    todo_2 = Todo("Don't Panic!")
    todo_3 = Todo("Fall at ground. Miss!")
    todo_4 = Todo("Be Happy rather than right!")
    td_list = TodoList()
    td_list.add(todo_1,todo_2, todo_3,todo_4)
    todo_2.mark_complete()
    todo_3.mark_complete()
    assert td_list.incomplete() == [todo_1,todo_4]

"""
complete returns a list
of complete tasks
"""
def test_td_list_complete_return_complete_tasks():
    todo_1 = Todo("Know where towel is")
    todo_2 = Todo("Don't Panic!")
    todo_3 = Todo("Fall at ground. Miss!")
    todo_4 = Todo("Be Happy rather than right!")
    td_list = TodoList()
    td_list.add(todo_1,todo_2, todo_3,todo_4)
    todo_2.mark_complete()
    todo_3.mark_complete()
    assert td_list.complete() == [todo_2,todo_3]

"""
Neither complete nor incomplete mutate the original list
"""

def test_td_list_complete_incomplete_not_mutate_list():
    todo_1 = Todo("Know where towel is")
    todo_2 = Todo("Don't Panic!")
    todo_3 = Todo("Fall at ground. Miss!")
    todo_4 = Todo("Be Happy rather than right!")
    td_list = TodoList()
    td_list.add(todo_1,todo_2, todo_3,todo_4)
    todo_2.mark_complete()
    todo_3.mark_complete()
    td_list.complete()
    td_list.incomplete()
    assert td_list.list == [todo_1,todo_2, todo_3,todo_4]

"""
give up marks all Todos
as complete
"""
def test_td_list_give_up_marks_all_complete():
    todo_1 = Todo("Know where towel is")
    todo_2 = Todo("Don't Panic!")
    todo_3 = Todo("Fall at ground. Miss!")
    todo_4 = Todo("Be Happy rather than right!")
    td_list = TodoList()
    td_list.add(todo_1,todo_2, todo_3,todo_4)

    assert td_list.complete() == []
    assert td_list.incomplete() == [todo_1, todo_2, todo_3, todo_4]

    td_list.give_up()

    assert td_list.complete() == [todo_1, todo_2, todo_3, todo_4]
    assert td_list.incomplete() == []

"""
give up marks all Todos
as complete
even if one is already complete
"""
def test_td_list_give_up_marks_all_complete_with_one_complete():
    todo_1 = Todo("Know where towel is")
    todo_2 = Todo("Don't Panic!")
    todo_3 = Todo("Fall at ground. Miss!")
    todo_4 = Todo("Be Happy rather than right!")
    td_list = TodoList()
    td_list.add(todo_1,todo_2, todo_3,todo_4)

    todo_1.mark_complete()

    assert td_list.complete() == [todo_1]
    assert td_list.incomplete() == [todo_2, todo_3, todo_4]

    td_list.give_up()

    assert td_list.complete() == [todo_1, todo_2, todo_3, todo_4]
    assert td_list.incomplete() == []

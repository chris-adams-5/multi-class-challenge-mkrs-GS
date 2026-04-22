from lib.todo import Todo

class TodoList:
    def __init__(self):
        self.list = []

    def add(self, *todos):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        for todo in todos:
            if not isinstance(todo, Todo):
                raise Exception("Error TodoList.add receives object of type Todo")
            
        self.list = self.list + [*todos]

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        return list(filter(lambda todo: todo.complete == False,self.list))

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        return list(filter(lambda todo: todo.complete == True,self.list))

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for todo in self.list:
            todo.mark_complete()


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if not task:
            raise ValueError("Task cannot be empty")
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            raise ValueError("Task not found")

    def get_tasks(self):
        return self.tasks


if __name__ == "__main__":
    todo_list = TodoList()
    todo_list.add_task("Buy milk")
    todo_list.add_task("Read a book")
    print("Current tasks:", todo_list.get_tasks())
    todo_list.remove_task("Buy milk")
    print("Current tasks after removal:", todo_list.get_tasks())

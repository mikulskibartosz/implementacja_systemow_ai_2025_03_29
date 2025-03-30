class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        self.tasks.append({"name": task_name, "completed": False})

    def mark_as_completed(self, task_name):
        for task in self.tasks:
            if task["name"] == task_name:
                task["completed"] = True
                break

    def remove_task(self, task_name):
        self.tasks = [task for task in self.tasks if task["name"] != task_name]

    def get_pending_tasks(self):
        return [task for task in self.tasks if not task["completed"]]

    def get_all_tasks(self):
        return self.tasks

class TodoListAssert:
    def __init__(self, todo_list):
        self.todo_list = todo_list

    def has_task_count(self, expected_count):
        actual_count = len(self.todo_list.get_all_tasks())
        assert actual_count == expected_count, \
            f"Expected {expected_count} tasks, but found {actual_count}"
        return self

    def has_pending_task_count(self, expected_count):
        actual_count = len(self.todo_list.get_pending_tasks())
        assert actual_count == expected_count, \
            f"Expected {expected_count} pending tasks, but found {actual_count}"
        return self

    def contains_task(self, task_name):
        tasks = self.todo_list.get_all_tasks()
        task_names = [task["name"] for task in tasks]
        assert task_name in task_names, \
            f"Expected task '{task_name}' to be in the list, but it wasn't found"
        return self

    def does_not_contain_task(self, task_name):
        tasks = self.todo_list.get_all_tasks()
        task_names = [task["name"] for task in tasks]
        assert task_name not in task_names, \
            f"Expected task '{task_name}' not to be in the list, but it was found"
        return self

    def has_task_with_status(self, task_name, expected_status):
        tasks = self.todo_list.get_all_tasks()
        matching_tasks = [task for task in tasks if task["name"] == task_name]

        assert matching_tasks, f"Task '{task_name}' not found in the list"

        task = matching_tasks[0]
        actual_status = task["completed"]
        assert actual_status == expected_status, \
            f"Expected task '{task_name}' to have status {expected_status}, but was {actual_status}"
        return self

def assert_that(todo_list):
    return TodoListAssert(todo_list)

class TestTodoList:
    def test_add_task(self):
        todo_list = TodoList()
        todo_list.add_task("Buy groceries")

        assert_that(todo_list) \
            .has_task_count(1) \
            .contains_task("Buy groceries") \
            .has_task_with_status("Buy groceries", False)

    def test_mark_task_as_completed(self):
        todo_list = TodoList()
        todo_list.add_task("Buy groceries")
        todo_list.mark_as_completed("Buy groceries")

        assert_that(todo_list) \
            .has_task_count(1) \
            .has_pending_task_count(0) \
            .has_task_with_status("Buy groceries", True)

    def test_remove_task(self):
        todo_list = TodoList()
        todo_list.add_task("Buy groceries")
        todo_list.add_task("Clean house")
        todo_list.remove_task("Buy groceries")

        assert_that(todo_list) \
            .has_task_count(1) \
            .does_not_contain_task("Buy groceries") \
            .contains_task("Clean house")

    def test_get_pending_tasks(self):
        todo_list = TodoList()
        todo_list.add_task("Buy groceries")
        todo_list.add_task("Clean house")
        todo_list.add_task("Do laundry")
        todo_list.mark_as_completed("Clean house")

        pending_tasks = todo_list.get_pending_tasks()

        assert len(pending_tasks) == 2
        assert any(task["name"] == "Buy groceries" for task in pending_tasks)
        assert any(task["name"] == "Do laundry" for task in pending_tasks)
        assert not any(task["name"] == "Clean house" for task in pending_tasks)

        assert_that(todo_list) \
            .has_task_count(3) \
            .has_pending_task_count(2)

    def test_get_all_tasks(self):
        todo_list = TodoList()
        todo_list.add_task("Buy groceries")
        todo_list.add_task("Clean house")
        todo_list.mark_as_completed("Clean house")

        all_tasks = todo_list.get_all_tasks()

        assert len(all_tasks) == 2
        assert any(task["name"] == "Buy groceries" and task["completed"] == False for task in all_tasks)
        assert any(task["name"] == "Clean house" and task["completed"] == True for task in all_tasks)

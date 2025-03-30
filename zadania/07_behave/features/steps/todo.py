from behave import given, when, then


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


@given('I have an empty todo list')
def step_impl(context):
    context.todo_list = TodoList()


@given('I have a todo list with the following tasks')
def step_impl(context):
    context.todo_list = TodoList()
    for row in context.table:
        task_name = row['task']
        completed = row['completed'].lower() == 'true'
        context.todo_list.add_task(task_name)
        if completed:
            context.todo_list.mark_as_completed(task_name)


@when('I add a task "{task_name}"')
def step_impl(context, task_name):
    context.todo_list.add_task(task_name)


@when('I mark the task "{task_name}" as completed')
def step_impl(context, task_name):
    context.todo_list.mark_as_completed(task_name)


@when('I remove the task "{task_name}"')
def step_impl(context, task_name):
    context.todo_list.remove_task(task_name)


@when('I get the pending tasks')
def step_impl(context):
    context.result_tasks = context.todo_list.get_pending_tasks()


@when('I get all tasks')
def step_impl(context):
    context.result_tasks = context.todo_list.get_all_tasks()


@then('the todo list should contain {count:d} task')
def step_impl(context, count):
    tasks = context.todo_list.get_all_tasks()
    assert len(tasks) == count, f"Expected {count} tasks, but found {len(tasks)}"


@then('the todo list should contain {count:d} pending tasks')
def step_impl(context, count):
    pending_tasks = context.todo_list.get_pending_tasks()
    assert len(pending_tasks) == count, f"Expected {count} pending tasks, but found {len(pending_tasks)}"


@then('the todo list should contain the task "{task_name}"')
def step_impl(context, task_name):
    tasks = context.todo_list.get_all_tasks()
    task_names = [task["name"] for task in tasks]
    assert task_name in task_names, f"Task '{task_name}' not found in the todo list"


@then('the todo list should not contain the task "{task_name}"')
def step_impl(context, task_name):
    tasks = context.todo_list.get_all_tasks()
    task_names = [task["name"] for task in tasks]
    assert task_name not in task_names, f"Task '{task_name}' should not be in the todo list"


@then('the task "{task_name}" should be marked as completed')
def step_impl(context, task_name):
    tasks = context.todo_list.get_all_tasks()
    for task in tasks:
        if task["name"] == task_name:
            assert task["completed"], f"Task '{task_name}' should be marked as completed"
            return
    assert False, f"Task '{task_name}' not found in the todo list"


@then('the task "{task_name}" should be marked as not completed')
def step_impl(context, task_name):
    tasks = context.todo_list.get_all_tasks()
    for task in tasks:
        if task["name"] == task_name:
            assert not task["completed"], f"Task '{task_name}' should be marked as not completed"
            return
    assert False, f"Task '{task_name}' not found in the todo list"


@then('I should get a list with {count:d} tasks')
def step_impl(context, count):
    assert len(context.result_tasks) == count, f"Expected {count} tasks, but found {len(context.result_tasks)}"


@then('the list should contain the task "{task_name}"')
def step_impl(context, task_name):
    task_names = [task["name"] for task in context.result_tasks]
    assert task_name in task_names, f"Task '{task_name}' not found in the result list"


@then('the list should not contain the task "{task_name}"')
def step_impl(context, task_name):
    task_names = [task["name"] for task in context.result_tasks]
    assert task_name not in task_names, f"Task '{task_name}' should not be in the result list"


@then('the list should contain the task "{task_name}" with status {status}')
def step_impl(context, task_name, status):
    expected_status = status.lower() == 'true'
    for task in context.result_tasks:
        if task["name"] == task_name:
            assert task["completed"] == expected_status, f"Task '{task_name}' has status {task['completed']}, expected {expected_status}"
            return
    assert False, f"Task '{task_name}' not found in the result list"

from behave import given, when, then

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

@given('I have a calculator')
def step_impl(context):
    context.calculator = Calculator()

@when('I add {a:d} and {b:d}')
def step_impl(context, a, b):
    context.result = context.calculator.add(a, b)

@when('I subtract {b:d} from {a:d}')
def step_impl(context, a, b):
    context.result = context.calculator.subtract(a, b)

@then('the result should be {result:d}')
def step_impl(context, result):
    assert context.result == result
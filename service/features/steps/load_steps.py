# features/steps/load_steps.py
from behave import given

@given('the following products exist')
def step_impl(context):
    context.products = [
        {"id": 1, "name": "Product A", "category": "Category 1"},
        {"id": 2, "name": "Product B", "category": "Category 2"},
        {"id": 3, "name": "Product C", "category": "Category 1"}
    ]

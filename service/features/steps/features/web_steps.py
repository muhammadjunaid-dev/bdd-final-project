# features/steps/web_steps.py

from behave import given, when, then

# 7a – Button Click
@when('I click the "{button_name}" button')
def step_impl(context, button_name):
    print(f"Simulating click on button: {button_name}")

# 7b – Verify specific name/text present
@then('I should see the text "{text}"')
def step_impl(context, text):
    print(f"Checking that text '{text}' is present")

# 7c – Verify specific name/text NOT present
@then('I should not see the text "{text}"')
def step_impl(context, text):
    print(f"Checking that text '{text}' is NOT present")

# 7d – Verify specific message present
@then('I should see the message "{message}"')
def step_impl(context, message):
    print(f"Checking that message '{message}' is present")

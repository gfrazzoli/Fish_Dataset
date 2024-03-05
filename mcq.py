from IPython.display import display, clear_output
import ipywidgets as widgets
from pathlib import Path
import json

JSON_QUESTION_PATH = Path(
    "/content/Fish_Dataset/questions.json"
)


def mcq(idx: int):
    question_dict = json.loads(JSON_QUESTION_PATH.read_text())[str(idx)]
    question = question_dict["question"]
    choice_list = question_dict["choice_list"]
    right_choice_list = question_dict["right_choice_list"]

    print(question)
    right_choice_set = set(right_choice_list)
    checkboxes = [
        widgets.Checkbox(value=False, description=choice, layout=widgets.Layout(width='90%')) for choice in choice_list
    ]
    for checkbox in checkboxes:
        display(checkbox)

    # Create an output widget to display the selected options
    output = widgets.Output()
    display(output)

    def on_validate_button_clicked(b):
        selected_options = set([
            checkbox.description for checkbox in checkboxes if checkbox.value
        ])

        with output:
            clear_output()
            if right_choice_set == selected_options:
                print("\033[1;32mCorrect!\033[0m")  # Print in red and bold
            elif len(right_choice_set) == 1:
                print("\033[1;31mWrong! The right answer is:\033[0m", *right_choice_set)  # Print in red and bold
            else:
                print("\033[1;31mWrong! The right answers are:\033[0m", *right_choice_set)  # Print in red and bold

    # Create and display the validation button
    validate_button = widgets.Button(description="Validate")
    validate_button.on_click(on_validate_button_clicked)
    display(validate_button)

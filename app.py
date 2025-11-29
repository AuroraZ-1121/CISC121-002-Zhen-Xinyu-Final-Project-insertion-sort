import gradio as gr

def parse_input(input_str: str):
    """
    Turn a comma-separated string into a list of integers.
    Example: "2, 0, 5, 4, 5, 5, 3, 2" (digits of student ID 20545532).
    """
    if input_str is None or input_str.strip() == "":
        raise ValueError("Input cannot be empty. Please enter at least one integer.")

    parts = input_str.split(",")
    numbers = []

    for part in parts:
        trimmed = part.strip()
        # ignore empty chunks such as "1, , 2"
        if trimmed == "":
            continue
        try:
            num = int(trimmed)
            numbers.append(num)
        except ValueError:
            raise ValueError(
                f"Invalid value: '{trimmed}'. Please enter only integers separated by commas."
            )

    if len(numbers) == 0:
        raise ValueError("No valid integers were found. Please enter valid integers.")

    return numbers


def insertion_sort_with_steps(arr):
    """
    Run insertion sort on a copy of the list and keep track of what happens.
    Returns:
        sorted_list: final sorted list
        steps: list of human-readable descriptions
    """
    a = arr.copy()
    steps = []

    steps.append(f"Initial array: {a}")

    # classic insertion sort
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        steps.append(
            f"\nStep {i}: Take key = {key} at index {i} and compare it with elements on the left."
        )

        # shift any larger values one slot to the right
        while j >= 0 and a[j] > key:
            steps.append(
                f"  - {a[j]} (index {j}) is greater than key {key}. "
                f"Move {a[j]} to index {j + 1}."
            )
            a[j + 1] = a[j]
            j -= 1

        # drop the key into its spot
        a[j + 1] = key
        steps.append(
            f"  - Place key {key} at index {j + 1}. Current array: {a}"
        )

    steps.append(f"\nFinal sorted array: {a}")
    return a, steps


def run_insertion_sort_app(input_str: str):
    """
    Parse the user input, run insertion sort, and format the results
    for the Gradio interface.
    """
    try:
        numbers = parse_input(input_str)
    except ValueError as e:
        return "Error", str(e)

    sorted_list, steps = insertion_sort_with_steps(numbers)
    sorted_str = ", ".join(str(x) for x in sorted_list)
    steps_text = "\n".join(steps)

    return sorted_str, steps_text


# Gradio UI
app = gr.Interface(
    fn=run_insertion_sort_app,
    inputs=gr.Textbox(
        lines=2,
        label="Enter integers separated by commas",
        placeholder="Example: 2, 0, 5, 4, 5, 5, 3, 2  (from student ID 20545532)"
    ),
    outputs=[
        gr.Textbox(label="Sorted list"),
        gr.Textbox(label="Step-by-step explanation", lines=20)
    ],
    title="Insertion Sort Visualizer",
    description=(
        "This app shows how the Insertion Sort algorithm works. "
        "Type a list of integers separated by commas and follow the steps of the sort."
    )
)

if __name__ == "__main__":
    # run locally
    app.launch()

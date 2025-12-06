# Insertion Sort Visualizer

This project is a small web app that shows how the **Insertion Sort** algorithm works on a list of integers.  
For the main example, I use the digits of my student ID **20545532**, written as:

`2, 0, 5, 4, 5, 5, 3, 2`

The app is built with Python and Gradio and is deployed on Hugging Face Spaces.


## Problem Breakdown & Computational Thinking

### 1. Decomposition

The goal is to demonstrate how the Insertion Sort algorithm works and to make the process easy to follow.

I break the problem into the following smaller pieces:

1. Read user input as a string from a text box.
2. Convert the string into a Python list of integers.
3. Apply the Insertion Sort algorithm to this list.
4. Record key steps of the algorithm:
   - which element is chosen as the key,
   - which elements are shifted,
   - where the key is finally inserted.
5. Display:
   - the final sorted list,
   - a step-by-step explanation in plain English.

### 2. Pattern Recognition

Insertion Sort has a clear and repetitive pattern:

- The array is conceptually divided into:
  - a **sorted** portion on the left, and
  - an **unsorted** portion on the right.
- For each index `i` from `1` to `n - 1`:
  - take `a[i]` as the **key**,
  - compare the key with the elements to its left,
  - shift any larger values one position to the right,
  - insert the key into the correct position in the sorted portion.

When I use the digits of student ID 20545532 (`2, 0, 5, 4, 5, 5, 3, 2`), each digit is processed by the same pattern:  
take it as the key, compare it with previous digits, shift larger digits, and insert it in order.

### 3. Abstraction

To keep the app simple for users:

- I hide low-level implementation details such as:
  - exact loop indices,
  - internal variables,
  - Python-specific syntax.
- I show only the important information:
  - the initial array (for example, `2, 0, 5, 4, 5, 5, 3, 2`),
  - which value is chosen as the key on each step,
  - which elements get moved,
  - the array after each insertion,
  - the final sorted array.
- Users only need to:
  - type integers separated by commas,
  - read the sorted result and the explanation.

### 4. Algorithm Design (Data Flow)

**Input**

- A string of integers separated by commas.  
  Example: `2, 0, 5, 4, 5, 5, 3, 2` (digits of student ID 20545532).

**Processing**

1. **Input parsing**
   - Split the string by commas.
   - Strip spaces around each piece.
   - Convert each non-empty piece into an integer.
   - Validate that:
     - at least one integer was provided,
     - all non-empty pieces are valid integers.

2. **Insertion Sort**
   - Store the integers in a list `a`.
   - For each position `i` from `1` to `len(a) - 1`:
     - set `key = a[i]` and `j = i - 1`,
     - while `j >= 0` and `a[j] > key`, move `a[j]` one step to the right,
     - place `key` at index `j + 1`,
     - record a short description of what happened at each step.

3. **Output formatting**
   - Turn the sorted list into a comma-separated string such as `0, 2, 2, 3, 4, 5, 5, 5`.
   - Join all step descriptions into one readable block of text.

**Output**

- The final sorted list (as text).
- A step-by-step explanation that describes how the list was sorted.

## Flowchart (Text Version)

Below is a text-based version of the flowchart for the overall logic of the app and the insertion sort process.  
This matches the structure used in the code and in the description above.

Start
  |
  v
User enters a comma-separated list of integers
  |
  v
Parse the input string
  |
  v
Is the input empty or invalid?
  |                 \
  | Yes              \ No
  v                   v
Show error       Store integers
message and stop   in list a
                      |
                      v
                  Set i = 1
                      |
                      v
                Is i < length(a)?
                 /             \
               No               Yes
               |                 |
               v                 v
Display final           Set key = a[i],
sorted list and steps     j = i - 1
               |                 |
               v                 v
              End      While j >= 0 and a[j] > key
                                   |
                                   v
                       Move a[j] to a[j + 1]
                       j = j - 1; record step
                                   |
                                   v
                       Place key at position j + 1
                       record current array
                                   |
                                   v
                             i = i + 1
                                   |
                                   v
                         Repeat the loop

## Steps to Run

### Run Locally

1. Make sure Python 3 is installed.

2. Install the required dependency:

   pip install -r requirements.txt

3. Run the app:

   python app.py

4. A Gradio link (usually something like `http://127.0.0.1:7860`) will appear in the terminal.
   Open this link in a browser to use the app.

### Run on Hugging Face Spaces

1. Create a new Space on Hugging Face and choose **Gradio** as the SDK.
2. Upload:

   * `app.py`
   * `requirements.txt`
3. Wait for the build to finish and open the Space.


## Testing & Verification

I tested the app with several different inputs:

1. **Student ID digits example**

   * Input: `2, 0, 5, 4, 5, 5, 3, 2` (digits of student ID 20545532)
   * Output: `0, 2, 2, 3, 4, 5, 5, 5`
   * The explanation shows how each digit is chosen as a key, which digits are shifted,
     and how the key is inserted in the correct position.

2. **Already sorted list**

   * Input: `1, 2, 3, 4`
   * Output: `1, 2, 3, 4`
   * No shifts are needed; the explanation still walks through each step.

3. **Reverse sorted list**

   * Input: `5, 4, 3, 2, 1`
   * Output: `1, 2, 3, 4, 5`
   * This is a worst case for insertion sort and produces many shifts.

4. **List with duplicates**

   * Input: `2, 2, 1, 3, 1`
   * Output: `1, 1, 2, 2, 3`

5. **Invalid input**

   * Input: `5, a, 3`
   * Output: an error message telling the user that only integers are allowed.

These tests confirm that:

* the parsing logic works,
* the insertion sort implementation is correct,
* and the app handles invalid input in a user-friendly way.

## Hugging Face Link

* Hugging Face Space: [https://aurora1121-cisc121-002-zhen-xinyu-final-project-e008fb1.hf.space/]

## Author & Acknowledgment

* Author: **Xinyu Zhen**
The project reviews the Insertion Sort algorithm from CISC 121 and uses the official Gradio documentation as a reference for building the user interface.
*AI Assistance Statement:
I used ChatGPT (OpenAI GPT-5.1) at Level 4 to help me organize the project structure, refine the wording of my README, and improve the clarity of my code comments. I implemented the insertion sort algorithm myself, tested the app with multiple inputs (including edge cases), and made all final decisions about what to include in the submission. All debugging and verification were done by me.

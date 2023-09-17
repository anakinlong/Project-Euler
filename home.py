"""
Interact with all the code in this repository.
"""

import importlib
import questions


def answer(question_number: int) -> int | None:
    """
    Return the answer to a particular question - if the answer doesn't exist, return None.

    :param question_number: the integer question number.

    :return: the `ANSWER` constant from the corresponding question module. If it doesn't exist, then None.
    """
    # Attempt to find the module containing the code for this question:
    module_name = f"Q{str(question_number)}"
    if module_name not in questions.__all__:
        raise ValueError(
            f"Could not find associated module name '{module_name}' for question '{question_number}'."
        )

    # Attempt to find the ANSWER constant in the given module:
    module = importlib.import_module("." + module_name, "questions")

    return getattr(module, "ANSWER", None)


def all_answers() -> dict[int: int]:
    """
    Return a dictionary mapping all answered questions to their answers.
    """
    return {number: answer(number) for number in sorted(questions.QUESTION_NUMBERS)}


if __name__ == "__main__":

    print(question(1))
    print(answer(1))
    print(all_answers())

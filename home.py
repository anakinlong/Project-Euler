"""
Interact with all the code in this repository.
"""

import importlib
from typing import Any

import questions


def retrieve_attribute_from_question_module(question_number: int, attribute: str) -> Any | None:
    """
    Return the value of an attribute of a particular question module.

    :param question_number: the integer question number.
    :param attribute: the name of the attribute

    :return: the value of the attribute from the corresponding question module. If it doesn't exist, then None.
    """
    # Attempt to find the module containing the code for this question:
    module_name = f"Q{str(question_number)}"
    if module_name not in questions.__all__:
        raise ValueError(
            f"Could not find associated module name '{module_name}' for question '{question_number}'."
        )

    # Attempt to find the attribute in the given module:
    module = importlib.import_module("." + module_name, "questions")

    return getattr(module, attribute, None)


def question(question_number: int) -> str | None:
    """
    Return the wording of a particular question.

    :param question_number: the integer question number.

    :return: the `__doc__` attribute from the corresponding question module. If it doesn't exist, then None.
    """
    return retrieve_attribute_from_question_module(question_number, "__doc__")


def answer(question_number: int) -> int | None:
    """
    Return the answer to a particular question - if the answer doesn't exist, return None.

    :param question_number: the integer question number.

    :return: the `ANSWER` constant from the corresponding question module. If it doesn't exist, then None.
    """
    return retrieve_attribute_from_question_module(question_number, "ANSWER")


def explanation(question_number: int) -> int | None:
    """
    Return the explanation to the answer to a particular question - if the answer doesn't exist, return None.

    :param question_number: the integer question number.

    :return: the `EXPLANATION` constant from the corresponding question module. If it doesn't exist, then None.
    """
    return retrieve_attribute_from_question_module(question_number, "EXPLANATION")


def all_answers() -> dict[int: int]:
    """
    Return a dictionary mapping all answered questions to their answers.
    """
    return {number: answer(number) for number in sorted(questions.QUESTION_NUMBERS)}


if __name__ == "__main__":

    print(question(15))
    print(answer(15))
    print(explanation(15))
    print(all_answers())

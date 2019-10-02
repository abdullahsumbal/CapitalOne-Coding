"""
Define a family of algorithms, encapsulate each one, and make them
interchangeable. Strategy lets the algorithm vary independently from
clients that use it.
"""
from PythonLanguage import PythonLanguage


class Information:
    """
    Define the interface of interest to clients.
    Maintain a reference to a Strategy object.
    """

    def __init__(self, language):
        self._language = language

    def comment_info(self):
        self._language.comment_counter()


if __name__ == "__main__":
    concrete_strategy_a = PythonLanguage()
    context = Information(concrete_strategy_a)
    context.comment_info()
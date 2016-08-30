from functools import wraps


class MissingTagError(Exception):
    """
    Custom exception to indicate a missing tag in a code smell annotation.
    """


def duplication(tag, *, comment=None):
    """

    """
    if tag == "":
        raise MissingTagError("Tag must not be empty.")

    def annotator(func):
        return func

    return annotator

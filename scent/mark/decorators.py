from functools import wraps


class MissingLabelError(Exception):
    """
    Custom exception to indicate a missing label in a code smell annotation.
    """


class duplication:
    """
    Annotator to mark code duplication
    """

    def __init__(self, label, comment=None):
        """
        Args:
            label (str):  Label to identify multiple instances of the duplicate code.
            comment (str, optional):  Optional comment (intended for other human developers).

        """
        if label == "":
            raise MissingLabelError("Label must not be empty.")

        # For now we are ignoring all arguments because the only
        # purpose of this class is to act as an annotation.

    def __call__(self, func):
        """
        This is called when the annotator is used as a decorator,
        for example as `@scent.mark.duplication(...)`. We return
        the decorated function unaltered because the only purpose
        of this class is to document that there is duplication.
        """
        return func

# Define shorter alias for easier use
dup = duplication

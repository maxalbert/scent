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
        Annotator to mark code duplication.

        Args:
            label (str):  Label to identify multiple instances of the duplicate code.
            comment (str, optional):  Optional comment. This is intended for other
                human developers and is currently ignored.

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

        @wraps(func)
        def wrapper(func):
            return func  # pragma: no cover  (as we can't be sure that a decorated function is actually called)

        return wrapper

# Define shorter alias for easier use
dup = duplication

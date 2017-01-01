"""
Annotators for common code smells.
"""

from functools import wraps

__all__ = ['dup', 'duplication', 'inconsistency', 'hardcoded_value', 'procedural_polymorphism']


class MissingLabelError(Exception):
    """
    Custom exception to indicate a missing label in a code smell annotation.
    """


class duplication:
    """
    Annotator to mark code duplication
    """

    def __init__(self, *, label, comment=None):
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


@duplication(label='inconsistency-annotator', comment='This is almost an exact copy of the "duplication" annotator.')
class inconsistency:
    """
    Annotator to mark code inconsistencies between classes/functions with a similar purpose.
    """

    def __init__(self, *, label, comment=None):
        """
        Args:
            label (str):  Label to identify all participants in this inconsistency.
            comment (str, optional):  Optional comment (intended for other human developers).

        """
        if label == "":
            raise MissingLabelError("Label must not be empty.")

        # For now we are ignoring all arguments because the only
        # purpose of this class is to act as an annotation.

    def __call__(self, func):
        """
        This is called when the annotator is used as a decorator,
        for example as `@scent.mark.inconsistency(...)`. We return
        the decorated function unaltered because the only purpose
        of this class is to document that there is duplication.
        """
        return func

@duplication(label='hardcoded-value-annotator', comment='This is almost an exact copy of the "duplication" annotator.')
class hardcoded_value:
    """
    Annotator to mark hard-coded values which should be turned into variables.
    """

    def __init__(self, *, label, comment=None):
        """
        Args:
            label (str):  Label to identify all occurrences of this hard-coded value.
            comment (str, optional):  Optional comment (intended for other human developers).

        """
        if label == "":
            raise MissingLabelError("Label must not be empty.")

        # For now we are ignoring all arguments because the only
        # purpose of this class is to act as an annotation.

    def __call__(self, func):
        """
        This is called when the annotator is used as a decorator,
        for example as `@scent.mark.hardcoded_value(...)`. We return
        the decorated function unaltered because the only purpose
        of this class is to document that there is duplication.
        """
        return func

@duplication(label='procedural-polymorphism-annotator', comment='This is almost an exact copy of the "duplication" annotator.')
class procedural_polymorphism:
    """
    Annotator to mark hard-coded values which should be turned into variables.
    """

    def __init__(self, *, label, comment=None):
        """
        Args:
            label (str):  Label to identify all occurrences of this code smell.
            comment (str, optional):  Optional comment (intended for other human developers).

        """
        if label == "":
            raise MissingLabelError("Label must not be empty.")

        # For now we are ignoring all arguments because the only
        # purpose of this class is to act as an annotation.

    def __call__(self, func):
        """
        This is called when the annotator is used as a decorator,
        for example as `@scent.mark.procedural_polymorphism(...)`.
        We return the decorated function unaltered because the only
        purpose of this class is to document that there is a code smell.
        """
        return func

# Define shorter alias for easier use
dup = duplication

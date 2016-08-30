import pytest

from .context import scent
from scent import MissingTagError


class TestCodeSmellAnnotations:
    """
    Unit tests for the code smell decorators.
    """

    @classmethod
    def setup_class(cls):
        """
        Define a simple dummy function `dummy_func` which can be re-used
        in the tests.
        """

        def dummy_func(x, y, z=42, foo="bar"):
            """Dummy function"""
            return True

        cls.dummy_func = dummy_func

    def test_annotating_a_function_does_not_change_its_attributes(self):
        """
        Annotating a function does not change its attributes.
        """
        dummy_func = scent.mark.duplication(tag='foobar')(self.dummy_func)

        assert dummy_func.__name__ == 'dummy_func'
        assert dummy_func.__doc__ == 'Dummy function'

    def test_standalone_annotation(self):
        """
        Annotations can occur "standalone", without decorating a function or class.
        """
        scent.mark.duplication(tag='foobar', comment='Standalone annotation.')

    def test_tag_must_be_specified(self):
        """
        Not specifying a tag raises an error.

        Note: Currently we don't really need this test because the decorator
              is defined as a function, so the missing 'tag' argument will
              automatically raise an error. However, if we decide to change
              the implementation in the future it's useful to have this test.
        """
        with pytest.raises(TypeError):
            scent.mark.duplication()(self.dummy_func)

    def test_cannot_be_empty(self):
        """
        Specifying an empty tag raises an error.
        """
        with pytest.raises(MissingTagError):
            scent.mark.duplication(tag="")(self.dummy_func)

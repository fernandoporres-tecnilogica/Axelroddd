Guidelines for Docstrings
=========================
Axelrod takes pride in its documentation for strategies, and Docstrings are a
big part of this implementation. In Python and especially Sphinx, docstrings
are strings which describes methods, modules and or classes and help the user
to understand the purpose and implementation of a strategy. Axelrod has
decided to follow the NumPy Docstring guidelines which are as follows:

    """ This is a Docstring

    Which can stretch over multiple lines and include a variety of content.

    """

Sections
--------

Within Axelrod, Docstrings for Strategies contain Bibliography fields as well
as brief summaries of said Strategy.

1. **Strategy Summary**
   A brief statement to summarize the workings of the Strategy.

        class HappyLittleTree(self, Player):
        """ Summarize the classes intent here.
        Could stretch multiple lines.

        """

2. **Strategy Note**
   A short note if applicable, that may serve to help future developers
   quickly understand issues or implementations within the strategy.

        class HappyLittleTree(self, Player):
        """ Summarize the classes intent here.
        Could stretch multiple lines.

        Note
        ----
        Pass on some information to future developers

        """

2. **Strategy Bibliography**
    This sections mentions the Strategy Source, or from where
    it was taken. The info written underneath ''Names'' is the source
    of the HappyLittleTree Strategy. Here, ''[Axelrod1984]_'' corresponds
    to the bibliographic item in 'docs/reference/bibliography.rst'. If
    you use a source without a reference in the RST file mentioned above,
    please take the time to add it yourself.

        class HappyLittleTree(self, Player):
        """ Summarize the classes intent here.
        Could stretch multiple lines.

        Note
        ----
        Pass on some information to future developers

        Names:
        - HappyLittleTree: [Axelrod1984]_

        """

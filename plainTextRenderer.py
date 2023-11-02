"""
A plain text renderer.
"""

from asciimatics.renderers.base import StaticRenderer


class PlainRender(StaticRenderer):
    """
    This class renders text.
    """

    def __init__(self, text):
        """
        :param text: The text string
        """
        super().__init__()
        self._images = [str(text)]

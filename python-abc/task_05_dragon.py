#!/usr/bin/env python3
"""Module demonstrating mixins."""


class SwimMixin:
    """Swimming behavior."""

    def swim(self):
        """Swim."""
        print("The creature swims!")


class FlyMixin:
    """Flying behavior."""

    def fly(self):
        """Fly."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class."""

    def roar(self):
        """Roar."""
        print("The dragon roars!")

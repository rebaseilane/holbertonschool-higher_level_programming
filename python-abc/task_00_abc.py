#!/usr/bin/env python3
"""Module that defines abstract Animal class and subclasses."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract animal class."""

    @abstractmethod
    def sound(self):
        """Return the sound made by the animal."""
        pass


class Dog(Animal):
    """Dog class."""

    def sound(self):
        """Return dog sound."""
        return "Bark"


class Cat(Animal):
    """Cat class."""

    def sound(self):
        """Return cat sound."""
        return "Meow"

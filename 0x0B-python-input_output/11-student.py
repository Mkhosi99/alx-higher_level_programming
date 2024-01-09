#!/usr/bin/python3

"""Define a class Student."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): first name of the student.
            last_name (str): last name of the student.
            age (int): age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.

        If attrs is a list of strings, 
        only attributes name contain in this list must be retrieved.
        Otherwise, all attributes must be retrieved

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) is list and
                all(type(elem) is str for elem in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance.

        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for key, val in json.items():
            setattr(self, key, val)

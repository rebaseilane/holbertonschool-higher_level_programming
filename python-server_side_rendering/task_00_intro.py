#!/usr/bin/python3
"""
Task 0 - Creating a Simple Templating Program

This module generates invitation files from a template
by replacing placeholders with attendee data.

It handles:
- Input validation
- Empty inputs
- Missing data fields
- File generation
"""


import os


def generate_invitations(template, attendees):
    """
    Generate invitation files from a template and list of attendees.

    Args:
        template (str): String containing placeholders.
        attendees (list): List of dictionaries with attendee data.

    Returns:
        None
    """

    # Validate template type
    if not isinstance(template, str):
        print(f"Error: template must be a string, got {type(template).__name__}")
        return

    # Validate attendees type
    if not isinstance(attendees, list):
        print(f"Error: attendees must be a list, got {type(attendees).__name__}")
        return

    # Check if list contains only dictionaries
    for item in attendees:
        if not isinstance(item, dict):
            print("Error: attendees must be a list of dictionaries")
            return

    # Handle empty template
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # Handle empty attendees list
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Required keys
    keys = ["name", "event_title", "event_date", "event_location"]

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        filled_template = template

        for key in keys:
            value = attendee.get(key, "N/A")

            # Handle None values
            if value is None:
                value = "N/A"

            filled_template = filled_template.replace(
                "{" + key + "}",
                str(value)
            )

        output_filename = f"output_{index}.txt"

        # Write file safely
        with open(output_filename, "w", encoding="utf-8") as file:
            file.write(filled_template)
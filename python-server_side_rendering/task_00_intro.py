#!/usr/bin/python3
"""
Generate personalized invitation files from a template and a list of attendees.
"""

def generate_invitations(template, attendees):
    """Generate invitation text files based on a template and attendee data."""

    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):

        name = attendee.get("name") or "N/A"
        event_title = attendee.get("event_title") or "N/A"
        event_date = attendee.get("event_date") or "N/A"
        event_location = attendee.get("event_location") or "N/A"

        output_text = (
            template.replace("{name}", name)
                    .replace("{event_title}", event_title)
                    .replace("{event_date}", event_date)
                    .replace("{event_location}", event_location)
        )

        filename = f"output_{index}.txt"

        try:
            with open(filename, "w") as file:
                file.write(output_text)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
            return

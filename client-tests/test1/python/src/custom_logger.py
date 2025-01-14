import json
import logging


class UniversalFormatter(logging.Formatter):
    COLORS = {
        "DEBUG": "\033[94m",  # Blue
        "INFO": "\033[92m",  # Green
        "WARNING": "\033[93m",  # Yellow
        "ERROR": "\033[91m",  # Red
        "CRITICAL": "\033[95m",  # Bright Red
        "ENDC": "\033[0m",  # End color
    }

    def format(self, record: logging.LogRecord):
        color = self.COLORS.get(record.levelname, self.COLORS["ENDC"])

        # Create a new attribute in 'record' for 'additional_info' and initialize it
        additional_info = ""

        # If user_id is present in the record, add it to 'additional_info'
        if hasattr(record, "user_id"):
            additional_info += f"user_id={record.user_id} "  # type: ignore

        # If json_payload is present in the record
        if hasattr(record, "json_payload"):
            # Pretty print the JSON
            record.json_payload = json.dumps(record.json_payload, indent=4)  # type: ignore
            additional_info += f"{record.json_payload} "  # type: ignore

        # Trim the last space from 'additional_info' and add a newline if it's not empty
        if hasattr(record, "additional_info"):
            previous_additional_info = record.additional_info.rstrip()  # type: ignore
            if previous_additional_info:
                additional_info = previous_additional_info + "\n" + additional_info

        if additional_info:
            record.additional_info = additional_info

        # Handle the case where the message itself is JSON
        if isinstance(record.msg, (dict, list)):
            record.msg = json.dumps(record.msg, indent=4)

        # Format the message with the parent class method
        formatted_message = super().format(record)

        # Apply color to the entire log message, including 'additional_info'
        colored_message = color + formatted_message + self.COLORS["ENDC"]

        return colored_message

#!/usr/bin/env python3
import json
import sys
from datetime import datetime
import html

HTML_TEMPLATE_FILE = 'report-template.html'

with open(HTML_TEMPLATE_FILE, 'r') as file:
    HTML_TEMPLATE = file.read()


def main():
    # Read JSON from stdin
    try:
        grype_data = json.load(sys.stdin)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON input: {e}", file=sys.stderr)
        sys.exit(1)

    # Generate timestamp for filename
    timestamp = datetime.now().strftime("%Y%m%dT%H%M%S")
    filename = f"grype_{timestamp}.html"

    # Create the HTML report
    report = HTML_TEMPLATE.format(
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        json_data=json.dumps(grype_data),
        grype_version=grype_data["descriptor"]["version"],
    )

    # Write the report to file
    try:
        with open(filename, "w") as f:
            f.write(report)
        print(f"Report generated: {filename}")
    except IOError as e:
        print(f"Error writing report: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

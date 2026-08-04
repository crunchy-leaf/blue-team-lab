import re


def parse_apache_log(file_path):

    events = []

    with open(file_path, 'r') as file:
        for line in file:

            pattern = (
               r'(?P<ip>\S+) .* '
               r'\[(?P<timestamp>.*?)\] '
               r'"(?P<method>\S+) (?P<endpoint>.*?) HTTP.*?" '
               r'(?P<status>\d+) (?P<size>\d+)' 
            )

            match = re.search(pattern, line)

            if match:

                event = match.groupdict()

                event['status'] = int(event['status'])
                event['size'] = int(event['size'])

                events.append(event)

        return events
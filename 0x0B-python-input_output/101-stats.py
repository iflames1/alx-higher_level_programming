#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics.
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>
"""

import sys

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        if len(parts) >= 7:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1

        if line_count % 10 == 0:
            print(f"File size: {total_size}")
            for code in sorted(status_codes):
                if status_codes[code] > 0:
                    print(f"{code}: {status_codes[code]}")

except KeyboardInterrupt:
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")
    sys.exit(0)

"""
__author__ = "Filip Ilic"
__email__ = "filip.ilic@htl.rennweg.at"
__version__ = "1.0.0"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "Development"
"""

import os
import gzip
from typing import Generator, Iterable, TextIO, List, Tuple, Dict
from collections import defaultdict, Counter
from py_generatoren.get_all_files import *


def extract_fields(lines: Iterable[str]) -> Generator[Tuple[str, str, int], None, None]:
    """
    Extract fields from log lines. Assumes Apache combined log format.
    Yields tuples of (IP address, URL, bytes transferred).

    :param lines: Iterable of log lines
    :return: Generator yielding tuples (IP, URL, bytes)

    >>> lines = ['127.0.0.1 - - [24/May/2024:14:00:00 +0000] "GET /index.html HTTP/1.1" 200 1024']
    >>> list(extract_fields(lines))
    [('127.0.0.1', '/index.html', 1024)]
    """
    for line in lines:
        parts = line.split()
        ip = parts[0]
        url = parts[6]
        bytes_transferred = int(parts[9]) if parts[9].isdigit() else 0
        yield ip, url, bytes_transferred


def count_requests(extracted_fields: Iterable[Tuple[str, str, int]]) -> Tuple[str, str, int]:
    """
    Count the number of requests per IP, per URL and sum the bytes transferred.

    :param extracted_fields: Iterable of tuples (IP, URL, bytes)
    :return: Tuple containing (most active IP, most requested URL, total bytes)

    >>> fields = [('127.0.0.1', '/index.html', 1024), ('127.0.0.1', '/index.html', 2048), ('192.168.0.1', '/about.html', 512)]
    >>> count_requests(fields)
    ('127.0.0.1', '/index.html', 3584)
    """
    ip_counter = Counter()
    url_counter = Counter()
    total_bytes = 0

    for ip, url, bytes_transferred in extracted_fields:
        ip_counter[ip] += 1
        url_counter[url] += 1
        total_bytes += bytes_transferred

    most_active_ip = ip_counter.most_common(1)[0][0]
    most_requested_url = url_counter.most_common(1)[0][0]

    return most_active_ip, most_requested_url, total_bytes


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Beispielaufruf
    directory_path = "./logs/"  # Ersetze durch das Verzeichnis mit deinen Logdateien
    fl = get_all_files(directory_path)
    of = open_files(fl)
    lines = read_lines(of)
    fields = extract_fields(lines)
    most_active_ip, most_requested_url, total_bytes = count_requests(fields)

    print(f"Most active IP: {most_active_ip}")
    print(f"Most requested URL: {most_requested_url}")
    print(f"Total bytes transferred: {total_bytes}")

#!/usr/bin/env python3

import os
import sys
import subprocess

if len(sys.argv) != 2:
    print("Usage: python3 HTTstatusPing.py https://example.com")
    sys.exit(1)

url = sys.argv[1]

def main():
    while True:
        try:
            command = f"curl -sI {url} | head -n 1 | cut -d' ' -f2"
            #print(command)
            status_code = subprocess.getoutput(command)
            print(f"HTTP status code: {status_code}")

        except KeyboardInterrupt:
            sys.exit(0)


if __name__ == "__main__":
    main()

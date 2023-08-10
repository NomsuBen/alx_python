#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays the
body of the response (decoded in utf-8).
If the HTTP status code is greater than or equal to 400, print:
Error code: followed by the value of the HTTP status code.
"""
import requests
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    try:
        response = requests.get(url)
        print("Response body:")
        print(response.text)
        
        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

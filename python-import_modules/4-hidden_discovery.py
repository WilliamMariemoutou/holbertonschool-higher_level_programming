#!/usr/bin/env python3
import marshal
import os

def discover_names():
    pyc_file_path = '/tmp/hidden_4.pyc'

    if not os.path.exists(pyc_file_path):
        print(f"Error: {pyc_file_path} does not exist.")
        return

    with open(pyc_file_path, 'rb') as file:
        file.seek(16)
        code_object = marshal.load(file)

    names = dir(code_object)
    filtered_names = [name for name in names if not name.startswith('__')]
    filtered_names.sort()

    for name in filtered_names:
        print(name)

if __name__ == "__main__":
    discover_names()

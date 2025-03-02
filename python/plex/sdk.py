import json
import os
import subprocess

from tempfile import TemporaryDirectory
from typing import Dict, List, Union

# finish run plex

def run_plex(io: Union[Dict, List[Dict]]):
    if not (isinstance(io, dict) or (isinstance(io, list) and all(isinstance(i, dict) for i in io))):
        raise ValueError('io must be a dict or a list of dicts')

    # Use a context manager for the temporary directory
    with TemporaryDirectory() as temp_dir:

        # Generate the JSON file name in the temporary directory
        json_file_path = os.path.join(temp_dir, 'io_data.json')

        # Save the io data to the JSON file
        with open(json_file_path, 'w') as json_file:
            json.dump(io, json_file, indent=4)

        cwd = os.getcwd()
        plex_dir = os.path.dirname(os.path.dirname(cwd))
        cmd = ["./plex", "-input-io", json_file_path]
        with subprocess.Popen(cmd, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True, cwd=plex_dir) as p:
            for line in p.stdout:
                print(line, end='')

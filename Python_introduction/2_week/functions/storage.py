import os
import tempfile
import json
import argparse

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

if not os.path.exists(storage_path):
    with open(storage_path, 'w') as f:
        json.dump(dict(), f)

parser = argparse.ArgumentParser()

parser.add_argument("--key", type = str, help = "method for define key in storage(necessarily)")
parser.add_argument("--value", type = str, help = "use this key if you want add new value for a key")
args = parser.parse_args()

if args.key == None:
    print("Wrong args! Exit!")
else:
    json_dict = dict()
    with open(storage_path, 'r') as f:
        json_dict = json.load(f)
    if args.value == None:
            if args.key in json_dict:
                print(", ".join(json_dict[args.key]))
            else:
                print("None")
    else:
        if args.key in json_dict:
            json_dict[args.key].append(args.value)
        else:
            json_dict[args.key] = [args.value]
        with open(storage_path, 'w') as f:
            json.dump(json_dict, f)
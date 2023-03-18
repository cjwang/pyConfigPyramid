import json
import os

# reads the "wangConfig.json" file using the json library 
# and determines the current script directory using the os library
class WangConfig:
    def __init__(self):
        script_dir = os.path.dirname(__file__)
        with open(os.path.join(script_dir, 'wangConfig.json'), 'r') as f:
            config_data = json.load(f)
        self.foo = config_data['foo']
        self.bar = config_data['bar']
        self.baz = config_data['baz']

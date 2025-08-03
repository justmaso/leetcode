import os
import sys

def rootify():
    root_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))
    if root_path not in sys.path:
        sys.path.append(root_path)

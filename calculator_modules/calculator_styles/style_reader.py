import os

def read_style(file_name):
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path,file_name)
    with open(file_path,"r") as f:
        return f.read()
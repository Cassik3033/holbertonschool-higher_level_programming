#!/usr/bin/python3
def best_scor(my_dict):
    return max(my_dict, key=my_dict.get) if my_dict else None

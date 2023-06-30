#!/bin/python3
import json

def main():
    data = {}
    with open('function_data.json', 'r') as f:
        data = json.load(f)
        
    lines = []
    var_lines = []
    
    with open(data['file'], 'r') as src:
        lines = src.readlines()

    with open(data['variant'], 'r') as var:
        var_lines = var.readlines()
            
    for i in range(len(lines)):
        lines[i] = lines[i].replace(data['name'], 'original')

    for i in range(len(var_lines)):
        var_lines[i] = var_lines[i].replace(data['name'], 'variant')
        
    l = lines[:data['line'] + data['size']] + var_lines + lines[data['line'] + data['size']:data['call_line'] + data['call_size'] - 1] + [lines[data['call_line'] - 1].replace('original', 'variant')] + lines[data['call_line'] + data['call_size'] - 1:]

    with open(data["file"], 'w') as n:
    # with open('new.c', 'w') as n:
        n.writelines(l)

if __name__ == "__main__":
    main()
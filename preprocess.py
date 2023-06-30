import json

def main():
    with open('function_data.json', 'r') as f:
        data = json.load(f)
        
        lines = []
        var_lines = []
        
        with open(data["file"], 'r') as src:
            lines = src.readlines()

        with open(data["variant"], 'r') as var:
            var_lines = var.readlines()
                
        lines = lines[:data["line"] -1 ] + var_lines + lines[data["line"] + data["size"]:]

        with open(data["file"], 'w') as n:
            n.writelines(lines)

if __name__ == "__main__":
    main()
import json
import re

def change_definition(config):
    definition = config["function"]["definition"]
    with open(definition["file"], 'r') as f:
        lines = f.readlines()
        before = lines[:definition["line"] - 1]
        after = lines[definition["line"] - 1:]

    with open(config["variant"]['file'], 'r') as f:
        variant = f.readlines()


    with open('new_def.c', 'w') as n:
        n.writelines(before + ['\n'])
        n.writelines(variant + ['\n'])
        n.writelines(after)

def change_call(config):

    call_config = config["function"]["call"]
    with open(call_config["file"], 'r') as f:
        lines = f.readlines()
        before = lines[:call_config["line"] - 1]
        call = lines[call_config["line"] - 1: call_config["line"] + call_config['call_size']]
        after = lines[call_config["line"] + call_config['call_size']:]

        copy = lines[call_config["line"] - 1: call_config["line"] + call_config['call_size']]
        copy = re.sub(r'\b' + config["function"]["name"] + r'\b', config["function"]["name"] + '_var', ''.join(copy)).split('\n')

    definitions = []
    definition_list = config["definitions"]
    for d in definition_list:
        new_name = d["name"] + '_var'
        definitions.append(f'{d["type"]} {new_name};\n')
        copy = re.sub(r'' + d["name"] + r'\b', new_name, '\n'.join(copy)).split('\n')

    comp_config = config["comparison"]
    comp_method = comp_config["method"]
    if comp_method == 'strcmp':
        with open('templates/comp_strcmp.c', 'r') as f:
            comparison = f.read()
            comparison = comparison.replace('<var1>', comp_config['var1']).replace('<var2>', comp_config['var2']).replace('<error>', comp_config['error'])
        print(comparison)
        

    with open('new_call.c', 'w') as n:
        n.writelines(before)
        n.writelines(definitions)
        n.write('\n')
        n.writelines(copy)
        n.write('\n\n')
        n.writelines(call)
        n.write('\n\n')
        n.write(comparison)
        n.write('\n')
        n.writelines(after)


def main():
    config = {}
    with open('config.json', 'r') as f:
        config = json.load(f)
    change_definition(config)
    change_call(config)

if __name__ == '__main__':
    main()





import yaml
with open('clash.yaml', 'r') as file:
    print(yaml.safe_load(file))

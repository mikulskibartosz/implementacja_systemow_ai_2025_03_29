import yaml

config_dict = {"server_name": "localhost", "server_port": 8080}

with open("test.yaml", "w") as f:
    yaml.dump(config_dict, f)


with open("test.toml", "w") as f:
    f.write(f"server_name = {config_dict['server_name']}\nserver_port = {config_dict['server_port']}")

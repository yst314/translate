import yaml

def load_config():
    with open('config.yml', 'r') as file:
        config = yaml.safe_load(file)
    return config
if __name__ == '__main__':
    config = load_config()
    print(config)
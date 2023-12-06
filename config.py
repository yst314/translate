import yaml

def load_config():
    with open('config.yml', 'r') as file:
        config = yaml.safe_load(file)
    return config

def save_yaml(data, path):
    with open(path, "w", encoding="UTF-8") as f:
        yaml.dump(data, f, allow_unicode=True)

if __name__ == '__main__':
    config = load_config()
    print(config)
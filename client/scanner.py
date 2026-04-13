from pathlib import Path

CONFIG_REGISTRY = {
    'zshrc': Path.home() / '.zshrc',
}

def find_config(config):
    if config in CONFIG_REGISTRY:
        config_obj = CONFIG_REGISTRY[config]
        if config_obj.exists():
            print(f"Config '{config}' found at {config_obj}")
            return config_obj
        else:
            raise FileNotFoundError(f"Config file '{config}' not found at {config_obj}")
    else:
        print(f"Config '{config}' not found in registry.")
    
config_obj = find_config('zshrc')

def read_config(config_obj):
    content = config_obj.read_text()
    print(f"Content of '{config_obj}':\n{content}")
    return content

if config_obj:
    text = read_config(config_obj)
    print(f"Read content from '{config_obj}':\n{text}")

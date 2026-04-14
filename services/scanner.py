from pathlib import Path

directory = Path.home() / ".config"




def find_config(app_name):

    old_dir = Path.home() / f".{app_name}rc"

    exact_file = Path.home() / f".{app_name.replace('.', '')}"
    if exact_file.is_file():
         return exact_file
    
    if old_dir.is_file():
        print(f"Config '{app_name}' found at: {old_dir}")
        return old_dir


    base_dir = directory / app_name
    config_file = base_dir / f"{app_name}.conf"

    if config_file.is_file():
        print(f"Config '{app_name}' found at: {config_file}")
        return config_file

    matches = [
        m for m in directory.rglob(f"*{app_name}*") 
        if m.is_file() and m.suffix != '.bak'
    ]
    
    if matches:
        print(f"Config '{app_name}' found via rglob at: {matches[0]}")
        return matches[0]
    else:
        print(f"Config '{app_name}' not found in {directory}.")
        return None

# def find_config(config):
#     if config in CONFIG_REGISTRY:
#         config_obj = CONFIG_REGISTRY[config]
#         if config_obj.exists():
#             print(f"Config '{config}' found at {config_obj}")
#             return config_obj
#         else:
#             raise FileNotFoundError(f"Config file '{config}' not found at {config_obj}")
#     else:
#         print(f"Config '{config}' not found in registry.")
    
def read_config(config_obj):
    content = config_obj.read_text()
    print(f"Content of '{config_obj}':\n{content[:100]}")
    return content


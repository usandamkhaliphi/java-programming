def add_setting(settings, pair):
    k, v = pair[0].lower(), pair[1].lower()
    
    if k in settings:
        return f"Setting '{k}' already exists! Cannot add a new setting with this name."
    
    settings[k] = v
    return f"Setting '{k}' added with value '{v}' successfully!"

def update_setting(settings, pair):
    k, v = pair[0].lower(), pair[1].lower()
    
    if k in settings:
        settings[k] = v
        return f"Setting '{k}' updated to '{v}' successfully!"
    
    return f"Setting '{k}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key):
    k = key.lower()
    
    if k in settings:
        del settings[k]
        return f"Setting '{k}' deleted successfully!"
    
    return "Setting not found!"

def view_settings(settings):
    if not settings:
        return "No settings available."
    
    output = "Current User Settings:\n"
    for k, v in settings.items():
        output += f"{k.capitalize()}: {v}\n"
    
    return output

test_settings = {"theme": "dark", "language": "english"}

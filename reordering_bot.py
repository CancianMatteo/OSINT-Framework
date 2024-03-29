# Reorder all tags of arf.json from: "children", "name", "type"; to: "name", "type", "children".
import json

def reorder_keys(obj):
    if isinstance(obj, dict):
        if 'children' in obj:
            children = obj.pop('children')
            new_obj = {'name': obj.pop('name'), 'type': obj.pop('type')}
            for child in children:
                new_obj.setdefault('children', []).append(reorder_keys(child))
            return new_obj
        else:
            return {k: reorder_keys(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [reorder_keys(elem) for elem in obj]
    else:
        return obj

# Read JSON from file
with open('arf.json', 'r') as f:
    json_data = json.load(f)

# Reorder keys
reordered_data = reorder_keys(json_data)

# Output reordered JSON
print(json.dumps(reordered_data, indent=2))
# Write reordered JSON to file
with open('arf2.json', 'w') as f:
    json.dump(reordered_data, f, indent=2)
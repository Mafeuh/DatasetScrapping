import json

with open('caradisiac_models.json', 'r') as file:
    brands_dict: dict = json.load(file)

print("Nombre de marques:", len(brands_dict.keys()))
print("Nombre total de modèles:", len([model for brand_models in brands_dict.values() for model in brand_models]))
import os
import json
from pathlib import Path
from horizon.CatalogedResource import *

main_model_schema = CatalogedResource.model_json_schema()
print(json.dumps(main_model_schema, indent=2))

with open("./output_formats/CatalogedResource.json", "w") as f:
    f.write(json.dumps(main_model_schema, indent=2))

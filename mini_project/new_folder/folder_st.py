import os
folder=[
    "templates/index.html"
    "static/css/style.css"
    "static/js/script.js"
]
for file in folder:
    os.makedirs(os.path.dirname(file), exist_ok=True)
    with open(file, 'w') as f:
        pass

import os 
os.rename("templates/index.html","templates/home.html")


import os
os.remove("templates/home.html")


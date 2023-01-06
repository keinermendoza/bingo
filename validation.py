import re
from wtforms import Form

def allowed_image(filename):
    return filename if re.search(r"^([^/]+\.(?:jpg|jpeg|png))$", filename) != None else None

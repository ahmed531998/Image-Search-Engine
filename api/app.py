from flask import Flask
from flask import request
from flask_cloudflared import run_with_cloudflared
import import_ipynb
import REST_Support
app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome to Golab REST API"

# route for retrieving the nearest neighbors of an image via a POST request.
# The request must contain a json parameter called "image", which is a string
# containing the base 64 representation of the query image.
# The response contains a json structure that looks like this
# data {
#   "neighbors": [
#       [<label>, <base64_image_representation>], 
#       ...
#       ...
#       [<label>, <base64_image_representation>]
#   ]    
# }
@app.route('/findKNN',methods = ['POST'])
def login():
    json_data = request.get_json(force=True) 
    image = json_data["image"]
    data = {}
    data["neighbors"] = REST_Support.get_knn_images(image.encode())
    return data, 200
    
if __name__ == '__main__':
    run_with_cloudflared(app)
    app.run()
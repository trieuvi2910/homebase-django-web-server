import requests
from flask import Flask, request, Response

app = Flask(__name__)

# Define the base URL of the Express API
EXPRESS_API_URL = "http://localhost:3000"  # Replace with the actual URL of your Express API

@app.route("/", defaults={"path": ""}, methods=["GET", "POST", "PUT", "DELETE"])
@app.route("/<path:path>", methods=["GET", "POST", "PUT", "DELETE"])
def proxy(path):
    url = "{}/{}".format(EXPRESS_API_URL, path)
    # Forward the incoming request to the Express API
    if request.method == "GET":
        response = requests.get(url, params=request.args)
    elif request.method == "POST":
        response = requests.post(url, data=request.form)
    elif request.method == "PUT":
        response = requests.put(url, data=request.form)
    elif request.method == "DELETE":
        response = requests.delete(url)
    else:
        return Response("Method not allowed", status=405)

    return Response(response.text, status=response.status_code, content_type=response.headers["content-type"])

if __name__ == "__main__":
    app.run(port=5000)
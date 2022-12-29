from flask import Flask, request, send_from_directory
from singleWordSearch import perform_search
import main

app = Flask(__name__, static_url_path='', 
            static_folder='client',)

@app.route('/search', methods=['GET'])
def search():
    # Perform the search and retrieve the results
    results = perform_search(request.args.get("q"))
    # Render the search template and pass the results to it
    return {"results": results, "queryfor": request.args.get("q")}

# @app.route('/')
# def send_report(path):
#     return send_from_directory('client', path="frontend.html")

if __name__ == '__main__':
    app.run()
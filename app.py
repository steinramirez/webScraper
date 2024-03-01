from flask import Flask, request, render_template, make_response
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/',  methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        data = request.form['data']
        soup = BeautifulSoup(requests.get(url).content, 'html.parser')
        results = soup.find_all(data)
        return render_template('index.html', results=results)
    else:
        return render_template('index.html')

@app.route('/download', methods=['GET'])
def download(results):
    # Create a string that contains the data you want to download
    data = "This is the data that will be downloaded in a text file.\n"
    for result in results:
        data += str(result) + "\n"

    # Set the Content-Type and Content-Disposition headers
    response = make_response(data)
    response.headers['Content-Type'] = 'text/plain'
    response.headers['Content-Disposition'] = 'attachment; filename=report.txt'
    return response

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, render_template, send_file, make_response
from bs4 import BeautifulSoup
import requests
import os
import json

app = Flask(__name__)

def process_url(url):
    if not url.startswith('http'):
        url = 'https://' + url
    return url

@app.route('/',  methods=['GET', 'POST'])
def index():
    results = []  # Initialize results list
    if request.method == 'POST':
        if 'clear' in request.form:
            return render_template('index.html')  # Render the template without results
        elif 'download' in request.form:
            # Generate report in a text file
            report_file = open('report.txt', 'w')
            report_file.write('Report for URL: {}\n'.format(request.form['url']))
            report_file.write('Data: {}\n'.format(request.form['data']))
            report_file.write('- {}\n'.format(request.form[results]))
            for result in results:
                report_file.write('- {}\n'.format(result.name))
            report_file.close()
            # Send the report file for download
            return send_file('report.txt', as_attachment=True)
        else:
            url = process_url(request.form['url'])
            data = request.form['data']
            soup = BeautifulSoup(requests.get(url).content, 'html.parser')
            results = soup.find_all(data)
    return render_template('index.html', results=results)

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

@app.route('/faq')
def faq():
    with open('static/faq.json', 'r') as file:
        faq_data = json.load(file)
    return render_template('faq.html', faq_data=faq_data)

if __name__ == '__main__':
    app.run(debug=True)
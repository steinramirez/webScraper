from flask import url_for, Flask, send_from_directory,  request, render_template, send_file, make_response, session
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
    return render_template('index.html', results=results, favicon_url=url_for('static', filename='favicon.ico'))

@app.route('/download', methods=['GET'])
def download():
    if 'results' in session:
        results = session['results']
        data = "This is the data that will be downloaded in a text file.\n"
        for result in results:
            data += str(result) + "\n"
        response = make_response(data)
        response.headers['Content-Type'] = 'text/plain'
        response.headers['Content-Disposition'] = 'attachment; filename=report.txt'
        return response
    else:
        return 'No results to download', 404

@app.route('/faq')
def faq():
    with open('static/faq.json', 'r') as file:
        faq_data = json.load(file)
    return render_template('faq.html', faq_data=faq_data)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
        'favicon.ico',mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
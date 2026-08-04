from flask import Flask, render_template, request
from parsers.apache_parser import parse_apache_log
from detection.engine import analyze_logs
from ai.summarize import generative_analysis
import markdown
import os


app = Flask(__name__)
ALERTS = {}

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():

    file = request.files['logfile']

    if file.filename == '':
        return 'No file selected.'

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    events = parse_apache_log(filepath)

    alerts = analyze_logs(events)

    for alert in alerts:
        ALERTS[alert['id']] = alert


    return render_template('dashboard.html', alerts=alerts)



@app.route('/alert/<alert_id>')
def alert_details(alert_id):

    alert = ALERTS.get(alert_id)

    if not alert:
        return 'Alert not found', 404

    if 'analysis' not in alert:
        alert['analysis'] = generative_analysis(alert)

    analysis_html = markdown.markdown(
        alert['analysis'],
        extensions=['fenced_code']
    )

    return render_template(
        'alert.html',
        alert=alert,
        analysis=analysis_html
    )


if __name__ == '__main__':
    app.run(debug=True)

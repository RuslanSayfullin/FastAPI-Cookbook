from flask import Flask

from converter.date_converter import DateConverter

app = Flask(__name__)
app.url_map.converters['date'] = DateConverter

@app.route('/', methods = ['GET'])
def index():
    return "This is an online ... counseling system (OPCS)"

@app.route('/home')
@app.route('/information')
@app.route('/introduction')
def home():
    return '''
        <html><head><title>Online Personal … System</title>
            </head><body>
            <h1>Online … Counseling System (OPCS)</h1>
            <p>This is a template of a web-based counseling
                application where counselors can … … …</em>
            </body></html>
        '''


if __name__ == "__main__":
    app.run(debug=True)
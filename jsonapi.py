from datetime import datetime
from flask import Flask
from flask_json import FlaskJSON, JsonError, json_response, as_json

app = Flask(__name__)
FlaskJSON(app)


@app.route('/get_time')
def get_time():
    return json_response(time=datetime.utcnow())

@app.route('', methods=['GET'])
def api_filter():
    query_parameters = request.args

    semester = query_parameters.get('semester')
    year = query_parameters.get('year')
    course_number = query_parameters.get('course_number')
    department = query_parameters.get('department')
    subject = query_parameters.get('subject')    
    course_type = query_parameters.get('course_type')
    display_closed = query_parameters.get('display_closed')

@app.route('/get_time_and_value')
@as_json
def get_time_and_value():
    return dict(time=datetime.utcnow(), value=12)


@app.route('/raise_error')
def raise_error():
    raise JsonError(description='Example text.', code=123)


if __name__ == '__main__':
    app.run()
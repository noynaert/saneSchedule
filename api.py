import flask
from flask import request, jsonify
from soup import SoupHandler

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.errorhandler(404)
def no_semester_and_year_page(e):
    return "<h1>404</h1><p>You have not specified any semester or year !</p>", 404

# A route to return all of the available entries in our catalog.
@app.route('/api/v1/courses/all', methods=['GET'])
def api_all():
    return {}

@app.route('/api/v1/courses/', methods=['GET'])
def api_filter():
    query_parameters = request.args

    semester = query_parameters.get('semester')
    year = query_parameters.get('year')
    course_number = query_parameters.get('course_number')
    department = query_parameters.get('department')
    subject = query_parameters.get('subject')    
    course_type = query_parameters.get('course_type')
    display_closed = query_parameters.get('display_closed')
    

    if not (semester or year):
        return no_semester_and_year_page(404)

    #to_filter = []
    conn = SoupHandler(semester, year)
    conn.setup_soup_handler(course_number, department, subject, display_closed, course_type)
    results = conn.proceed_scrapping()

    return jsonify(results)

app.run()
from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions

app = FlaskAPI(__name__)


notes = {
    0: 'do the shopping',
    1: 'build the codez',
    2: 'paint the door',
}


@app.route("/", methods=['GET', 'POST'])
def notes_list():
    return {"hello":"world"}

@app.route("/getData", methods=['GET', 'POST'])
def returnData():
    if request.method == 'POST':
        print(request.data)
        return request.data,status.HTTP_200_OK
    return {"hello":"world"}




if __name__ == "__main__":
    app.run(debug=True,port=8080)
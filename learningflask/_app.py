from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__, template_folder='_templates', static_folder='static', static_url_path='/')

# @app.route('/')
# def index():
    # return "<h1>Hello World</h1>"

@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}"


@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return f"{num1} + {num2} = {num1+num2}"

@app.route('/handle_url_params')
def handle_params():
    # return str(request.args)
    if 'name' in request.args.keys() and 'job' in request.args.keys():
        name = request.args["name"]
        job = request.args["job"]
        return f"Hi I am {name} and I am a {job}."
    else:
        return 'Some parameters are missing'

@app.route('/reqs', methods=['GET', 'POST'])
def mkng_requests():
    if request.method == 'POST':
        return f"You made a POST Request", 200
    elif request.method == 'GET':
        return f"You made a GET Request", 201
    else:
        return 
    
@app.route('/')
def hteeml():
    myval = 10
    result = 15
    mylist = ['Book', 'Pen', 'Ball']
    return render_template('index.html', list = mylist)

@app.route('/other')
def other():
    some_text = "Hello World"
    return render_template('other.html', text=some_text)

# @app.template_filter('reverse')
# def reverse(s):
#     text = s
#     return (text[::-1])

@app.route('/redirect_endpoint')
def redirect__():
    return redirect(url_for('other'))


@app.route('/handling', methods=['GET', 'POST'])
def handle_reqqs():
    if request.method == 'GET':
        return render_template('other.html')
    elif request.method == 'POST':    
        username = request.form.get('username')
        password  = request.form.get('password')

        if username == 'oye111' and password == '1234':
            return "success"
        else: 
            return "Failure"




if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
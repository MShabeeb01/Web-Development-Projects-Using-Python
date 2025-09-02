from flask import Flask, render_template
#Flask is used to create the app, and render_template allows you to render HTML templates (like index.html or greet.html) from a templates folder.

# Create Flask App
app = Flask(__name__)
#Creates an instance of the Flask class and assigns it to the variable app.__name__ tells Flask where to look for files and resources. If you run the file directly, __name__ will be "__main__", which Flask uses to locate things like templates and static files.

# Define a Route
@app.route('/')
def home():
    return render_template('index.html')
#@app.route('/') defines a route (URL path). Here / means the root of your website (like http://127.0.0.1:5000/).def home(): is the function that runs when someone visits /.return render_template('index.html') tells Flask to look inside the templates folder for a file called index.html and return it to the browser.

# Greeting Route
@app.route('/greet/<name>')
def greet(name):
    return render_template('greet.html', name=name)
#@app.route('/greet/<name>') defines a dynamic route.Example: If you visit http://127.0.0.1:5000/greet/Shabeeb, the value "Shabeeb" will be captured as the variable name.
# def greet(name): defines a function with that variable.
# return render_template('greet.html', name=name) passes the variable name into the template greet.html, so you can use it inside with {{ name }}.

# Run the App
if __name__ == '__main__':
    app.run(debug=True)
#This checks if the file is run directly (not imported into another Python file).
#app.run(debug=True) starts a development server: debug=True means it will automatically reload when you change the code and also show detailed error messages if something breaks.By default, it runs on http://127.0.0.1:5000/.    

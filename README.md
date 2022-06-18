# Hello Flask!

## What is Flask?

Flask is a python library, so you can install it via pip. Flask is also a web micro-framework, this means it is offering us functionality so we can build a web app on top of it. It is micro because its not super big, it just gives us the basics.
One of the functionalities we get is a local webserver so we can run our app within it and start processing requests and give out responses (typically to a web browser).

The oficial documentation for Flask can be found here:
https://flask.palletsprojects.com/en/2.1.x/

## What is in this repo?

This repo contains a finished result for different steps we will do / did in class to get familiar with Flask.
The starting point was this guide, that you were instructed to try out on your own:
https://pythonprogramminglanguage.com/flask-hello-world/

A recap of the commands to get the first 'Hello World' app running (what to put in web.py is in the linked tutorial):

```
python3 -m venv venv
. venv/bin/activate
pip3 install flask
python web.py
```
export PYTHONPATH="$PYTHONPATH:/home/mduhagon/flask-practice"


### Step 1: Convert initial web.py into a bit more complete app.py file / use flask run

- By convention, Flask expects your app creation to happen in a file named app.py or wsgi.py. 
You can name it as you wish (we created our app in web.py for example) but that requires us to pass an extra param
if we want to use the `flask run` commandm which is the standard way to run flask applications 
(we saw python app-file.py also works, but it is not so standard).

- Also, we are going to tweak a little bit the structure of the app.py to 
  make it friendlier to tests / and more similar to what we will use later for our projects.

- We created `app.py` and then we can run the app with this command:

```
flask run
```

To run our app in development mode, so when we change code we can see the change
right away without need to stop the flask app and run again, we start it with this additional param:

```
FLASK_ENV=development flask run
```

( At this point we do not need web.py anymore, we could remove it)


### Step 2: Serving static resources

When we build a web application, we often use resorces (files) that are static,
this means, there is no **server side** code to be executed in them. 
Flask makes it very easy to return these type of files to the web browser. 
We just need to put the files in a folder named `static`:

- We created folder `static` and added a couple sample files there (sample_image.jpg / styles.css)
- Then we can access them with these URLs: 
    http://127.0.0.1:5000/static/sample_image.jpg
    http://127.0.0.1:5000/static/styles.css


### Step 3: Separating code from presentation / putting HTML inside templates    

- It's clear that full html files are super complex and we cannot just construct them s strings within our route handling methods. We need to separate all this HTML / Presentation code into some other layer.
For that, Flask gives us [Jinja templates](https://jinja.palletsprojects.com/en/3.1.x/templates/)! Jinja is a templating engine used not only by Flask but many others. 

- We create templates in the `templates` folder. A layout is like a parent template with common / repeatable content, that has 'holes' or blocks, that each specific page can define content for. We created one `layout.html` and a couple templates that extend it (hello.html / hello_name.html)

- Templates can receive parameters, can have loops, conditional logic, etc. We try some of this in `hello_name.html`and `hello_name_list.html`


### Step 4: Setting up the debugger for our Flask app in VSCode:

- Switch to the 'Run and Debug' view by clicking the Arrow-and-bug icon on the left hand side
- Click on 'create a launch.json file'. On the emergent selection window, choose Flask
- Now you can use the > button on the top left column to start the Flask app in debug mode. If you place breakpoints in the code, the execution will pause and you can go step by step / check variable values, etc.

![](https://drive.google.com/file/d/192Q6JQ4cTxsXeYDoN1a-1RpSTYAe6sl_/view?usp=sharing)
![](https://drive.google.com/file/d/1xKno6Imm7hKi1NJchgmnxtBuL5lQ4opz/view?usp=sharing)
![](https://drive.google.com/file/d/1bg3m__pB3IxKn7iooSvQPYWp15OiinRy/view?usp=sharing)

### Step 5: A Form example

- Forms are very important when dealing with dat input from the user. We can use some extra library calle WTForms to implement a lot of common tasks with forms (validation, showing errors for the form / individual fields on the template, etc.)

- We install flask_wtf (which in turn also installs wtforms):

```
pip3 install flask_wtf
```

- It is the standard to have a `forms.py` file were we create one class per form we will have on our app. We create a `SampleForm`.


- To see ALL errors in a form we can use the following block:

```
    {% for field, errors in form.errors.items() %}
    <div class="alert alert-error">
        {{ form[field].label }}: {{ ', '.join(errors) }}
    </div>
    {% endfor %}
```

- We need to properly deal with [CSRF token](https://flask-wtf.readthedocs.io/en/0.15.x/csrf/)
  by making sure our form includes this:

  ```
  {{ form.csrf_token }}
  ```

  and also initializing a SECRET_KEY for the app (inside `create_app`):

  ```
    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY
  ```  
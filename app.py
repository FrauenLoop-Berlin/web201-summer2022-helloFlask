import os
from flask import Flask, render_template, request, redirect, url_for
from forms import SampleForm

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, static_folder="static")

    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY

    # Routes defined for this app / website
    @app.route('/hello')
    def hello():
        return 'Hello World from Python Flask!'

    @app.route('/')
    def helloRoot():
        return render_template(
            'hello.html'
        )   

    @app.route('/say-my-name')
    def helloName():
        nameParam = request.args.get('name')
        return render_template(
            'hello_name.html',
            personName=nameParam
        )    

    @app.route('/hello-all')
    def helloList():
        allPeople = ['July', 'Ron', 'Sandra', 'Maria']
        return render_template(
            'hello_name_list.html',
            personNamesList=allPeople
        )  

    @app.route('/form', methods=['GET', 'POST'])
    def form():
        form = SampleForm()
        if form.validate_on_submit():
            return redirect(url_for('hello'))

        return render_template(
            'sample_form.html',
            form=form
        )                        

    # End Routes

    # Return the fully initialized app
    return app


app = create_app()
if __name__ == '__main__':
    port = int(os.environ.get("PORT",5000))
    app.run(host='127.0.0.1',port=port,debug=True)
from functions.database.users import check_username_and_password, log_user_in, check_is_admin, log_user_out
from flask import Flask, request, render_template, redirect, make_response, url_for
from functions.database.database import connect
from controller.information import information
from functions.utilities import encrypt
from controller.users import users
from controller.home import home

app = Flask(__name__)

# adding blueprints
app.register_blueprint(users)
app.register_blueprint(home)
app.register_blueprint(information)

# creating the routes
@app.before_request
def before_request():
    connect()

@app.route('/')
def index():
    username = request.cookies.get('username')
    password = request.cookies.get('password')
    if any([username == None, password == None]):
        return redirect('/login')
    else:
        if check_username_and_password(username, password):
            is_admin = check_is_admin(username)[0][0]
            if is_admin:
                return redirect('/users/manage')
            else:
                return redirect('/home/manage')
        else:
            return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        error = request.args.get('error')
        if error:
            return render_template('users/login.html', error=bool(error))
        else:
            username = request.cookies.get('username')
            password = request.cookies.get('password')
            if any([username == None, password == None]):
                return render_template('users/login.html')
            else:
                if check_username_and_password(username, password):
                    return redirect('/')
                else:
                     return render_template('users/login.html', error=True)
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        password = encrypt(password)
        if log_user_in(username, password):
            resp = make_response(redirect('/'))
            resp.set_cookie('username', username, max_age=(31556926 * 10))
            resp.set_cookie('password', password, max_age=(31556926 * 10))
            return resp
        else:
            return redirect('/login?error=True')

@app.route('/logout')
def logout():
    username = request.cookies.get('username')
    password = request.cookies.get('password')
    if any([username == None, password == None]):
        return redirect('/login')
    else:
        if check_username_and_password(username, password):
            if log_user_out(username, password):
                resp = make_response(redirect('/'))
                resp.delete_cookie('username')
                resp.delete_cookie('password')
                return resp
            else:
                return redirect('/')
        else:
            return redirect('/login')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, use_reloader=True)

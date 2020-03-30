from functions.database.users import check_username_and_password, check_is_admin, delete_user as del_user, add_user, check_if_user_available
from flask import Blueprint, request, render_template, redirect, make_response, url_for
from functions.utilities import encrypt

users = Blueprint('users', __name__)

@users.route('/users/manage/<string:username>/delete')
def delete_user(username):
    current_username = request.cookies.get('username')
    current_password = request.cookies.get('password')
    if any([current_username == None, current_password == None]):
        return redirect('/login')
    else:
        if check_username_and_password(current_username, current_password):
            is_admin = check_is_admin(current_username)[0][0]
            if is_admin:
                if del_user(username):
                    return redirect(url_for('manage_users', done=True, success_msg='User deleted successfully'))
                else:
                    return redirect(url_for('manage_users', err=True, err_msg='Delete user failed'))
            else:
                return redirect('/')
        else:
            return redirect('/login')

@users.route('/users/manage/create', methods=['GET', 'POST'])
def create_user():
    current_username = request.cookies.get('username')
    current_password = request.cookies.get('password')
    if any([current_username == None, current_password == None]):
        return redirect('/login')
    else:
        if check_username_and_password(current_username, current_password):
            is_admin = check_is_admin(current_username)[0][0]
            if is_admin:
                if request.method == 'GET':
                    return render_template('create_user.html')
                else:
                    username = request.form.get('username')
                    password = request.form.get('password')
                    password = encrypt(password)
                    cpassword = request.form.get('cpassword')
                    cpassword = encrypt(cpassword)
                    is_admin = request.form.get('is_admin')
                    if is_admin == 'admin':
                        is_admin = True
                    else:
                        is_admin = False
                    if not check_if_user_available(username):
                        return render_template('create_user.html', err=True, err_msg='Username is not available')
                    if password != cpassword:
                        return render_template('create_user.html', err=True, err_msg='Password is not correct')
                    if add_user(username, password, is_admin):
                        return redirect(url_for('manage_users', done=True, success_msg='User created successfully'))
                    else:
                        return redirect(url_for('manage_users', err=True, err_msg='Create user failed'))
            else:
                return redirect('/')
        else:
            return redirect('/login')


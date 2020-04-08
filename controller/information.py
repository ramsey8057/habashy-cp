from functions.database.users import check_username_and_password, check_is_admin
from functions.database.information import get_information, update_information
from flask import Blueprint, render_template, request, redirect, url_for

information = Blueprint('information', __name__)

@information.route('/information/manage', methods=['GET', 'POST'])
def manage_information():
    username = request.cookies.get('username')
    password = request.cookies.get('password')
    if any([username == None, password == None]):
        return redirect('/login')
    else:
        if check_username_and_password(username, password):
            if request.method == 'GET':
                is_admin = check_is_admin(username)[0][0]
                err = request.args.get('err')
                err_msg = request.args.get('err_msg')
                done = request.args.get('done')
                success_msg = request.args.get('success_msg')
                return render_template(
                    'information/information.html',
                    username=username,
                    is_admin=is_admin,
                    err=err,
                    err_msg=err_msg,
                    done=done,
                    success_msg=success_msg,
                    info=get_information()[0]
                )
            else:
                old_email = request.form.get('old_email')
                email = request.form.get('email')
                main_phone = request.form.get('main_phone')
                other_phone = request.form.get('other_phone')
                address = request.form.get('address')
                city = request.form.get('city')
                footer_description = request.form.get('footer_description')
                if update_information(old_email, email, main_phone, other_phone, address, city, footer_description):
                    return redirect(url_for('information.manage_information', done=True, success_msg='information updated successfully'))
                else:
                    return redirect(url_for('information.manage_information', err=True, err_msg='update information failed'))


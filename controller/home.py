from functions.database.slider_images import get_all_slider_images, delete_slider_image as delete
from flask import Blueprint, request, render_template, redirect, make_response, url_for
from functions.database.users import check_username_and_password, check_is_admin
from functions.database.service_cards import get_all_service_cards

home = Blueprint('home', __name__)

@home.route('/home/manage', methods=['GET', 'POST'])
def manage_home():
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
                    'home_page.html',
                    username=username,
                    is_admin=is_admin,
                    err=err,
                    err_msg=err_msg,
                    done=done,
                    success_msg=success_msg,
                    all_slider_images=get_all_slider_images(),
                    all_service_cards=get_all_service_cards()
                )
            else:
                request_for = request.form.get('request_for')
                return request_for
        else:
            return redirect('/login')

@home.route('/home/manage/<int:image_slider_id>/delete')
def delete_slider_image(image_slider_id):
    username = request.cookies.get('username')
    password = request.cookies.get('password')
    if any([username == None, password == None]):
        return redirect('/login')
    else:
        if check_username_and_password(username, password):
            if delete(image_slider_id):
                return redirect(url_for('home.manage_home', done=True, success_msg='Slider image deleted successfully'))
            else:
                return redirect(url_for('home.manage_home', err=True, err_msg='Delete slider image failed'))
        else:
            return redirect('/login')

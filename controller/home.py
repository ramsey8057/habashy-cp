from functions.database.service_cards import get_all_service_cards, update_service_card, update_service_card_without_img, get_service_card_image_path
from functions.database.slider_images import get_all_slider_images, delete_slider_image as delete
from flask import Blueprint, request, render_template, redirect, make_response, url_for
from functions.database.users import check_username_and_password, check_is_admin
import pathlib
import json
import os

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
                all_service_cards = get_all_service_cards()
                return render_template(
                    'home_page.html',
                    username=username,
                    is_admin=is_admin,
                    err=err,
                    err_msg=err_msg,
                    done=done,
                    success_msg=success_msg,
                    all_slider_images=get_all_slider_images(),
                    all_service_cards=all_service_cards,
                    all_service_cards_as_json=json.dumps(all_service_cards)
                )
            else:
                request_for = request.form.get('request_for')
                if request_for == 'service_cards':
                    selected_item = int(request.form.get('selected_item'))
                    old_img_path = get_service_card_image_path(selected_item)
                    old_img_path = url_for('static', filename=old_img_path)[1:]
                    img = request.files.get('img')
                    title = request.form.get('title')
                    description = request.form.get('description')
                    link = request.form.get('link')
                    if img.filename == '':
                        if update_service_card_without_img(selected_item, title, description, link):
                            return redirect(url_for('home.manage_home', done=True, success_msg='Service card updated successfully'))
                        else:
                            return redirect(url_for('home.manage_home', err=True, err_msg='Delete slider image failed'))
                    if 'image' not in img.content_type:
                        return redirect(url_for('home.manage_home', err=True, err_msg='The image src must be an image'))
                    filename = img.filename.split('.')
                    extension = filename[len(filename) - 1]
                    img_path = f'img/uploads/service_cards/{selected_item}_img.{extension}'
                    if update_service_card(selected_item, img_path, title, description, link):
                        os.remove(old_img_path)
                        img.save(url_for('static', filename=f'{img_path}')[1:])
                        return redirect(url_for('home.manage_home', done=True, success_msg='Service card updated successfully'))
                    else:
                        return redirect(url_for('home.manage_home', err=True, err_msg='Delete slider image failed'))
                elif request_for == 'our_customers':
                    pass # TODO: CODE HERE
                else:
                    return redirect('/')
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


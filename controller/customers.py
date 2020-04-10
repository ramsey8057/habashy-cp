from functions.database.customers import get_new_customer_id, add_customer as add_customer_db, get_customer_image_path, delete_customer as del_cust
from functions.database.users import check_username_and_password, check_is_admin
from flask import Blueprint, render_template, request, redirect, url_for
import os

customers = Blueprint('customers', __name__)

@customers.route('/home/manage/customers/add', methods=['GET', 'POST'])
def add_customer():
    username = request.cookies.get('username')
    password = request.cookies.get('password')
    if any([username == None, password == None]):
        return redirect('/login')
    else:
        if check_username_and_password(username, password):
            if request.method == 'GET':
                err = request.args.get('err')
                err_msg = request.args.get('err_msg')
                return render_template(
                    'customers/add_customer.html',
                    err=err,
                    err_msg=err_msg
                )
            else:
                customer_id = get_new_customer_id()
                customer_name = request.form.get('customer_name')
                img = request.files.get('img')
                if 'image' not in img.content_type:
                    return redirect(url_for('customers.add_customer', err=True, err_msg='The image src must be an image'))
                filename = img.filename.split('.')
                extension = filename[len(filename) - 1]
                img_path = f'img/uploads/customers/{customer_id}_img.{extension}'
                if add_customer_db(customer_id, customer_name, img_path):
                    img.save(url_for('static', filename=img_path)[1:])
                    return redirect(url_for('home.manage_home', done=True, success_mg='Customer added succesfully'))
                else:
                    return redirect(url_for('customers.add_customer', err=True, err_msg='Add customer failed'))
        else:
            return redirect('/login')

@customers.route('/home/manage/customer/<string:customer_name>/delete')
def delete_customer(customer_name):
    username = request.cookies.get('username')
    password = request.cookies.get('password')
    if any([username == None, password == None]):
        return redirect('/login')
    else:
        if check_username_and_password(username, password):
            img_path = url_for('static', filename=get_customer_image_path(customer_name))[1:]
            if del_cust(customer_name):
                os.remove(img_path)
                return redirect(url_for('home.manage_home', done=True, success_msg='Customer deleted successfully'))
            else:
                return redirect(url_for('home.manage_home', err=True, err_msg='Delete customer failed'))
        else:
            return redirect('/login')


from flask import Blueprint, render_template, jsonify, request, url_for, redirect
import logging
from service.crud import add_department, get_departments, get_department, del_department, put_department
from .forms import DepartmentForm
logging.basicConfig(filename="departments_log.log", level=logging.WARNING)
logger = logging.getLogger('dep')
from  datetime import datetime

# from rest.checkers import department_check
view_departments_blueprint = Blueprint('view_departments', __name__, template_folder='templates')


@view_departments_blueprint.route('/')
def departments_list():
    """
    Show list of departments
    :return:
    """
    departments = get_departments()
    return render_template('departments.html', departments=departments)


@view_departments_blueprint.route('/<int:id_dept>')
def department_item(id_dept):
    department = get_department(id_dept)
    return render_template('department.html', department=department)


@view_departments_blueprint.route('/create', methods=['GET', 'POST'])
def create_department():
    form = DepartmentForm()
    if form.validate_on_submit():
        title = form.title.data
        id_dept = add_department(title)
        log_msg = f'dep {id_dept}, {title}, created : {datetime.now()}'
        logger.warning(log_msg)
        return redirect(url_for('view_departments.department_item', id_dept=id_dept))
    return render_template('department_create.html', form=form)


@view_departments_blueprint.route('/delete/<int:id_dept>')
def delete_department(id_dept):
    deleted = del_department(id_dept)
    if deleted:
        return redirect(url_for('view_departments.departments_list'))
    else:
        item = 'employee'
        return render_template('not_existed.html', item=item)


@view_departments_blueprint.route('/edit/<int:id_dept>', methods=["GET", "POST"])
def edit_department(id_dept):
    form = DepartmentForm()
    department = get_department(id_dept)
    if form.validate_on_submit():
        title = form.title.data
        put_department(id_dept, title)
        return redirect(url_for('view_departments.department_item', id_dept=id_dept))
    return render_template('department_edit.html', form=form, department=department)



# put_department
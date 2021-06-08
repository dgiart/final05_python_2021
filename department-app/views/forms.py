from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class DepartmentForm(FlaskForm):
    title = StringField('Enter a Title', validators=[DataRequired()])
    submit = SubmitField('Submit')


class EmployeeForm(FlaskForm):
    name = StringField('Enter a Name', validators=[DataRequired()])
    salary = FloatField('Enter a Salary', validators=[DataRequired()])
    department = IntegerField('Enter  the Department id', validators=[DataRequired()])
    year = IntegerField('Year', validators=[DataRequired()])
    month = IntegerField('Month', validators=[DataRequired()])
    day = IntegerField('Day', validators=[DataRequired()])
    submit = SubmitField('Submit')

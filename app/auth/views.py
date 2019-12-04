from flask import render_template,redirect,url_for
from . import auth
from ..models import Writer
from .forms import Registration,Login
from .. import db
from flask_login import login_user,logout_user,login_required
from flask import flash



@auth.route('/register',methods = ["GET","POST"])
def register_writer():
    form =Registration()
    if form.validate_on_submit():
        writer=Writer(email=form.email.data,username=form.username.data,password=form.password.data)
        db.session.add(writer)
        db.session.commit()
        flash('Welcome new writer')
        return redirect(url_for('auth.login'))
        title="New Account"
    return render_template('auth/register.html',registration_form = form )
@auth.route('/login', methods=['GET','POST'])
def login():
    login_form =Login()
    '''
    we create an an intsance of the login form and check if the form is validated when its submitted
    '''

    if login_form.validate_on_submit():
        writer=Writer.query.filter_by(email = login_form.email.data).first()
        if writer is not None and writer.verify_password(login_form.password.data):
            login_user(writer,login_form.remember.data)
            return  redirect(url_for('main.admin'))
        flash('Invalid username or password')
    title ="Blog login"
    return render_template('auth/login.html',login_form=login_form,title=title)
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

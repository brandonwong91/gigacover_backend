from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@customers.cwtj4hpdxres.us-east-2.rds.amazonaws.com/customers"
    #"postgresql://postgres:postgres@localhost/customers"

app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class customers(db.Model):
    id = db.Column('customer_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.Date(), nullable=False)
    updated_at = db.Column(db.DateTime(10))

    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

@app.route('/')
def show_all():
    return render_template('show_all.html', customers=customers.query.all())


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['dob']:
            flash('Please enter all the fields', 'error')
        elif customers.query.filter_by(name=request.form['name']).first():
            flash('Name entered already taken, please enter a different name (Case Sensitive)')
        else:
            customer = customers(request.form['name'], request.form['dob'])
            customer.updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            db.session.add(customer)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_all'))
    return render_template('create.html')

@app.route('/youngest', methods=['GET', 'POST'])
def youngest():
    if request.method == 'GET':
        youngest_session = db.session.execute('SELECT * FROM customers ORDER BY dob DESC')
        return render_template('youngest.html', customers=youngest_session)
        #return render_template('youngest.html', customers=customers.query.order_by(customers.dob.desc()))

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
            name = request.form['delete_name']
            customer = customers.query.filter_by(name=name).first()
            db.session.delete(customer)
            db.session.commit()
            flash('Record was successfully deleted')
            return redirect(url_for('show_all'))
    return render_template('delete.html', customers=customers.query.all())


@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
            if not request.form['update_dob']:
                flash('Please enter date field to update')
                return redirect(url_for('update'))
            else:
                dob = request.form['update_dob']
                name = request.form['update_name']
                customer = customers.query.filter_by(name=name).first()
                customer.dob = dob
                customer.updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                db.session.commit()
                flash('Record was successfully updated')
                return redirect(url_for('show_all'))
    return render_template('update.html', customers=customers.query.all())

if __name__ == '__main__':
    db.create_all()

    app.run(debug=True)
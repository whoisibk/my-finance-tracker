from flask import Flask, request, render_template, redirect, url_for, session, flash, jsonify
from extensions import db
from datetime import datetime

from dotenv import load_dotenv
import os

load_dotenv()


def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///finance.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    db.init_app(app)
    from models import User, Transaction, select

    @app.route('/')
    def home():
        return render_template('login.html')

    # credentials = {'email': 'admin@oye.com', 'password': '1234'}

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            email = request.form['login-email']
            password = request.form['login-password']

            user = User.query.filter_by(email=email, password=password).first()


            if user:
                session['email'] = user.email
            
                statement = select(User.user_id).where(User.email==email)
                user1  = db.session.execute(statement=statement).scalar_one()
                session['user_id'] = user1

                flash('Login Successful', 'success')
                return render_template('login.html', redirect_to_dashboard = True)
            else:
                flash('Invalid Username or Password', 'error')
                return render_template('login.html', redirect_to_dashboard = False)

    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        if request.method == 'POST':
            if len(request.form.keys()) == 4:
                name = request.form['signup-name']
                job = request.form['signup-job']
                email = request.form['signup-email']
                password = request.form['signup-password']

                user = User(name=name, job=job, email=email, password=password)
                db.session.add(user)
                db.session.commit()

                flash('Account Created Successfully','info')

        return render_template('login.html')


    @app.route('/dashboard', methods=['POST', 'GET'])
    def dashboard():
        global miscellaneous, housing, transportation, food, total_expenses_, total_income_

        #popup form to add transaction
        user_id = session['user_id']

        if request.method == 'POST':
            currency:str = request.form['currency']
            #1st row
            amount:int = int(request.form['amount'])
            
            # checking for type, it is a checkbox that returns on when on else None 
            check = request.form.get('transaction-type')
            if not check:
                type = 'Income'
            else: 
                type = 'Expense'

            #2nd row
            category = request.form['category']
            #3rd 
            timestamp = request.form['datetime']
            timestamp = datetime.fromisoformat(timestamp)
            # datetime = iso
            #4th row
            description = request.form['description']
            
            if '--' not in request.form.keys():
                transaction = Transaction(user_id=user_id, type=type, category=category, amount=amount, description=description, date=timestamp)

                db.session.add(transaction)
                db.session.commit()

                flash('Transaction Added Successfully', 'success')
            
        transactions = Transaction.query.filter_by(user_id=user_id).order_by(Transaction.date.desc()).all()

        # currency_ = [t.currency for t in transactions][0]
        total_income_ = sum([t.amount for t in transactions if t.type=='Income'])
        total_income = f"{total_income_:,}"

        total_expenses_ = sum([t.amount for t in transactions if t.type=='Expense'])
        total_expenses = f"{total_expenses_:,}"

        savings_ = total_income_ - total_expenses_
        savings = f"{savings_:,}"

        salary = sum([t.amount for t in transactions if t.category=='Salary'])
        housing = sum([t.amount for t in transactions if t.category=='Housing'])
        food = sum([t.amount for t in transactions if t.category=='Food'])
        transportation = sum([t.amount for t in transactions if t.category=='Transportation'])
        miscellaneous = sum([t.amount for t in transactions if t.category=='Miscellaneous'])

       

        return render_template('dashboard.html', transactions=transactions, savings=savings, total_income=total_income, total_expenses=total_expenses)
    
    @app.route('/piechart')
    def pie_chart():

        #percentage for chart
        housing_pcent = round((housing/total_expenses_) * 100)
        food_pcent = round((food/total_expenses_) * 100)
        transportation_pcent = round((transportation / total_expenses_) * 100)
        miscellaneous_pcent = round((miscellaneous/total_expenses_) * 100)

        labels = ['Food', 'Housing', 'Transportation', 'Miscellaneous']
        values = [food_pcent, housing_pcent,transportation_pcent, miscellaneous_pcent]

        chart_data= {
            'labels': labels,
            'values': values,  
        }

        return jsonify(chart_data) 
    
    @app.route('/barchart')
    def bar_chart():
        labels = ['Income', 'Expenses']
        values  = [total_income_, total_expenses_]

        barchart_data = {
            'labels': labels,
            'values': values,
        }

        return jsonify(barchart_data)

    with app.app_context():
       db.create_all()

    return app




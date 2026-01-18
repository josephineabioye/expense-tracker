from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database model
class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)

@app.route('/')
def home():
    expenses = Expense.query.all()
    return render_template('home.html', expenses=expenses)

@app.route('/add', methods=['POST'])
def add_expense():
    name = request.form['name']
    amount = request.form['amount']
    category = request.form['category']

    new_expense = Expense(
        name=name,
        amount=float(amount),
        category=category
    )

    db.session.add(new_expense)
    db.session.commit()

    return redirect('/')


@app.route('/delete/<int:id>')
def delete_expense(id):
    expense = Expense.query.get_or_404(id)
    db.session.delete(expense)
    db.session.commit()
    return redirect('/')


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_expense(id):
    expense = Expense.query.get_or_404(id)

    if request.method == 'POST':
        expense.name = request.form['name']
        expense.amount = float(request.form['amount'])
        expense.category = request.form['category']

        db.session.commit()
        return redirect('/')

    return render_template('edit.html', expense=expense)




if __name__ == "__main__":
    if not os.path.exists('expenses.db'):
        with app.app_context():
            db.create_all()

    app.run(host="0.0.0.0", port=5000, debug=True)

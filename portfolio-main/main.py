from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)

# Создаем таблицы при первом запуске
with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def process_form():
    if request.method == 'POST' and 'email' in request.form:
        email = request.form['email']
        message = request.form['text']
        
        new_feedback = Feedback(email=email, message=message)
        db.session.add(new_feedback)
        db.session.commit()
        
        return redirect('/?feedback_sent=1')

    button_python = request.form.get('button_python')
    button_telegram = request.form.get('button_telegram')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')

    return render_template(
        'index.html',
        button_python=button_python,
        button_telegram=button_telegram,
        button_html=button_html,
        button_db=button_db,
        feedback_sent=request.args.get('feedback_sent')  # Для уведомления
    )

if __name__ == "__main__":
    app.run(debug=True)
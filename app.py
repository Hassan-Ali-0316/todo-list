from flask import Flask , render_template , request , redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class todo(db.Model):
    sno = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(200),nullable = False)
    desc = db.Column(db.String(500),nullable = False)
    date = db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"           


print(type(db))


@app.route("/" , methods=['GET','POST'])
def hello():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo1 = todo(title=title,desc=desc)
        db.session.add(todo1)
        db.session.commit()

    alltodo = todo.query.all()

    return render_template('index.html',alltodo=alltodo)


@app.route("/update")
def updater():
    alltodo = todo.query.all()
    print(alltodo)
    return "this is products page"


@app.route("/delete/<int:sno>")
def deleter(sno):
    alltodo = todo.query.filter_by(sno=sno).first()
    db.session.delete(alltodo)
    db.session.commit()
    return redirect ("/")


app.run(debug=True)
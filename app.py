from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary in-memory database
users = {"student1": "12345", "admin": "admin123"}
feedback_list = []

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form['username']
        pwd = request.form['password']
        if uname in users and users[uname] == pwd:
            if uname == "admin":
                return redirect(url_for('admin'))
            else:
                return redirect(url_for('feedback'))
        else:
            return render_template('login.html', msg="Invalid Credentials!")
    return render_template('login.html')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        comment = request.form['comment']
        feedback_list.append({'name': name, 'comment': comment})
        return render_template('success.html', name=name)
    return render_template('feedback.html')

@app.route('/admin')
def admin():
    return render_template('admin.html', feedbacks=feedback_list)

if __name__ == '__main__':
    app.run(debug=True)

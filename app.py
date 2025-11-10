from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fullname = request.form['fullname']
        institute = request.form['institute']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        print(f"New registration: {fullname} | {email} | {institute} | {phone}")
        return redirect(url_for('authenticate'))
    return render_template('register.html')

@app.route('/authenticate')
def authenticate():
    return render_template('authenticate.html')

if __name__ == '__main__':
    app.run(debug=True)

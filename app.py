from flask import Flask, render_template, request, redirect, url_for
from supabase import create_client, Client

app = Flask(__name__)

# ✅ Replace with your actual Supabase project credentials
url = "https://rydypmvtwxvvcfdvrewv.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJ5ZHlwbXZ0d3h2dmNmZHZyZXd2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjI4Mzc2NDUsImV4cCI6MjA3ODQxMzY0NX0.1sYmmTsnfbtcav_fEw-IHLPDA8HI11iLwteKrjIcmXs"
supabase: Client = create_client(url, key)

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

        data = {
            "fullname": fullname,
            "institute": institute,
            "email": email,
            "phone": phone,
            "password": password
        }

        # ✅ Important: Add this print to debug
        response = supabase.table("users").insert(data).execute()
        print(response)  # See what Supabase returns

        return redirect(url_for('authenticate'))
    return render_template('register.html')

@app.route('/authenticate')
def authenticate():
    return render_template('authenticate.html')

if __name__ == '__main__':
    app.run(debug=True)

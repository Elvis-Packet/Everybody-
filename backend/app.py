from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_folder='static', template_folder='templates')

# In-memory storage for birthday date
birthday_date = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/date', methods=['GET', 'POST'])
def date():
    global birthday_date
    if request.method == 'POST':
        birthday_date = request.form.get('birthday')
        # For now, just redirect to thankyou page
        return redirect(url_for('thankyou'))
    return render_template('date.html')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

@app.route('/lastpage')
def lastpage():
    return render_template('lastpage.html')

if __name__ == '__main__':
    app.run(debug=True)

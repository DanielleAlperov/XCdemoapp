from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure random key

# Dummy user data (In production, use a database)
users = {
    "danielle": "123456"
}

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users and users[username] == password:
            session['username'] = username
            session['balance'] = 5420.75  # Initial fake balance
            session['transactions'] = [  # Initial transactions
                {"date": "2025-03-04", "description": "Deposit", "amount": "+ $1,200.00", "color": "green"},
                {"date": "2025-03-02", "description": "Online Purchase", "amount": "- $200.50", "color": "red"},
                {"date": "2025-02-28", "description": "ATM Withdrawal", "amount": "- $100.00", "color": "red"},
                {"date": "2025-02-25", "description": "Salary Credit", "amount": "+ $3,500.00", "color": "green"}
            ]
            return redirect(url_for('dashboard'))
        else:
            return "Invalid credentials. Try again!"
    
    return render_template('login.html')

@app.route('/dashboard', methods=['GET'])
def dashboard():
    if 'username' in session:
        return render_template(
            'dashboard.html', 
            username=session['username'], 
            balance=session['balance'], 
            transactions=session.get('transactions', [])
        )
    return redirect(url_for('login'))

@app.route('/make_transaction', methods=['POST'])
def make_transaction():
    if 'username' not in session:
        return jsonify({"error": "Unauthorized"}), 403

    recipient = request.form['recipient']
    amount = float(request.form['amount'])

    if amount > session['balance']:
        return jsonify({"error": "Insufficient funds!"}), 400  # Return JSON error

    # Deduct from balance
    session['balance'] -= amount

    # Fake transaction entry
    new_transaction = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "description": f"Transfer to {recipient}",
        "amount": f"- ${amount:.2f}",
        "color": "red"
    }

    # Append to session transactions
    session['transactions'].insert(0, new_transaction)

    return jsonify({
        "success": True,
        "new_balance": session['balance'],
        "transaction": new_transaction
    })

@app.route('/logout')
def logout():
    session.clear()  # Clears all session data
    return redirect(url_for('login'))

@app.route('/headers', methods=['GET'])
def headers_page():
    return render_template('headers.html')

@app.route('/headers-json', methods=['GET'])
def headers_json():
    return jsonify({key: value for key, value in request.headers.items()})

# ====== API ROUTES ====== #

def generate_fake_credit_card():
    bin_prefixes = {
        "Visa": "4",
        "MasterCard": str(random.randint(51, 55)),
        "Amex": random.choice(["34", "37"]),
        "Discover": "6011"
    }
    card_type = random.choice(list(bin_prefixes.keys()))
    prefix = bin_prefixes[card_type]
    length = 16 if card_type != "Amex" else 15

    while len(prefix) < length - 1:
        prefix += str(random.randint(0, 9))

    def luhn_checksum(card_number):
        digits = [int(d) for d in card_number]
        for i in range(len(digits) - 2, -1, -2):
            digits[i] *= 2
            if digits[i] > 9:
                digits[i] -= 9
        return (10 - sum(digits) % 10) % 10

    checksum = luhn_checksum(prefix + "0")
    return prefix + str(checksum)

def generate_fake_ssn():
    return f"{random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(1000, 9999)}"

@app.route('/api', methods=['POST'])
def api_service():
    data = request.get_json()
    if not data or 'serviceName' not in data:
        return jsonify({"error": "Missing 'serviceName' parameter"}), 400
    
    service_name = data['serviceName']
    
    if service_name == "creditcard":
        return jsonify({"message": "Credit Card Info", "credit_card": generate_fake_credit_card()})
    elif service_name == "ssn":
        return jsonify({"message": "Social Security Number", "social_security_number": generate_fake_ssn()})
    else:
        return jsonify({"error": "Invalid serviceName"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

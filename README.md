# XC Demo App

Welcome to the **XC Demo App** – a simple Flask-based web application with authentication, transactions, and API services. This app has a sleek and intuitive design with a clean UI and structured API responses.

## 🚀 Features

- **User Authentication** (Login & Logout)
- **Dashboard with Transaction History**
- **Transaction Processing** (Deducts balance, logs transactions)
- **JWT-based Header Display** (View all request headers)
- **Custom Error Pages** (`401 Unauthorized`, `404 Not Found`)
- **API Services:**
  - Generate Fake Credit Card Numbers
  - Generate Fake Social Security Numbers

---

## 🛠️ Installation & Setup

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### **2. Install Dependencies**
Ensure you have Python and Flask installed:
```bash
pip install flask
```

### **3. Run the Application**
```bash
python app.py
```
The app runs on `http://localhost:80`.

---

## 📂 Project Structure

```
/app
│-- templates/        # HTML templates (login, dashboard, headers, errors)
│-- static/           # CSS, JS, images
│-- app.py            # Main Flask application
│-- README.md         # Documentation
│-- myapp.service     # Systemd service file
```

---

## 🔑 Authentication & Dashboard
- Users login via `POST /login` with username and password.
- After login, users are redirected to `/dashboard` where they can view their balance and transaction history.

---

## 🔄 Transactions
- Users can submit transactions via `POST /make_transaction`.
- The transaction is validated and added to the session-based transaction history.
- Insufficient balance returns an error.

---

## 📡 API Endpoints
### **1. Headers Display**
- **`GET /headers`** - Displays all request headers in a styled UI.
- **`GET /headers-json`** - Returns all headers in JSON format.

### **2. API Services**
- **`POST /api`** (JSON Payload: `{ "serviceName": "creditcard" }`)
  - Returns a fake credit card number.
- **`POST /api`** (JSON Payload: `{ "serviceName": "ssn" }`)
  - Returns a fake social security number.

---



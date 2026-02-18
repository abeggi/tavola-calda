from flask import Flask, render_template, request, redirect, session, jsonify
import os, json
from datetime import datetime
from functools import wraps

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "cambia-questo-segreto")

MENU_FILE = "/data/menu.json"
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "admin123")

GIORNI = ["Lunedì","Martedì","Mercoledì","Giovedì","Venerdì","Sabato","Domenica"]
MESI = ["Gennaio","Febbraio","Marzo","Aprile","Maggio","Giugno",
        "Luglio","Agosto","Settembre","Ottobre","Novembre","Dicembre"]

def data_oggi():
    n = datetime.now()
    return f"{GIORNI[n.weekday()]} {n.day} {MESI[n.month-1]} {n.year}"

def load_menu():
    if os.path.exists(MENU_FILE):
        with open(MENU_FILE) as f:
            return json.load(f)
    return {
        "data": "",
        "sezioni": [
            {"titolo": "Primi", "piatti": []},
            {"titolo": "Secondi", "piatti": []},
            {"titolo": "Contorni", "piatti": []},
            {"titolo": "Dolci", "piatti": []}
        ],
        "nota": ""
    }

def save_menu(data):
    os.makedirs("/data", exist_ok=True)
    with open(MENU_FILE, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get("logged_in"):
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated

@app.route("/")
def index():
    menu = load_menu()
    return render_template("menu.html", menu=menu, now=data_oggi())

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form.get("password") == ADMIN_PASSWORD:
            session["logged_in"] = True
            return redirect("/admin")
        error = "Password errata"
    return render_template("login.html", error=error)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/admin", methods=["GET", "POST"])
@login_required
def admin():
    menu = load_menu()
    if request.method == "POST":
        data = request.get_json()
        save_menu(data)
        return jsonify({"ok": True})
    return render_template("admin.html", menu=menu)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

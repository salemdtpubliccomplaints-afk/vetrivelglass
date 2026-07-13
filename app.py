from flask import Flask, render_template, request, redirect, url_for, flash
import os
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "change-this-key-before-production")

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.environ.get("DATABASE_PATH", os.path.join(BASE_DIR, "vetrivelglass.db"))


def init_db():
    with sqlite3.connect(DB_PATH) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS enquiries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                email TEXT,
                vehicle TEXT,
                service TEXT NOT NULL,
                message TEXT,
                created_at TEXT NOT NULL
            )
        """)
        connection.commit()


init_db()


@app.context_processor
def inject_year():
    return {"current_year": datetime.now().year}


@app.route("/")
def home():
    return render_template("index.html", page="home")


@app.route("/about")
def about():
    return render_template("about.html", page="about")


@app.route("/services")
def services():
    return render_template("services.html", page="services")


@app.route("/contact")
def contact():
    return render_template("contact.html", page="contact")


@app.post("/enquire")
def enquire():
    name = request.form.get("name", "").strip()
    phone = request.form.get("phone", "").strip()
    email = request.form.get("email", "").strip()
    vehicle = request.form.get("vehicle", "").strip()
    service = request.form.get("service", "").strip()
    location = request.form.get("location", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not phone or not service:
        flash("Please enter your name, phone number and required service.", "error")
        return redirect(request.referrer or url_for("contact"))

    full_message = message
    if location:
        full_message = f"Service location: {location}\n{message}".strip()

    with sqlite3.connect(DB_PATH) as connection:
        connection.execute("""
            INSERT INTO enquiries
            (name, phone, email, vehicle, service, message, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            name,
            phone,
            email,
            vehicle,
            service,
            full_message,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ))
        connection.commit()

    flash("Thank you. Your enquiry has been submitted. Our team will contact you shortly.", "success")
    return redirect(url_for("contact") + "#enquiry")


@app.route("/health")
def health():
    return {"status": "ok", "website": "www.vetrivelglass.com"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)

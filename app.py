from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "supersecretkey"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# ================= USER MODEL =================
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False)

    failed_attempts = db.Column(db.Integer, default=0)
    locked = db.Column(db.Boolean, default=False)

with app.app_context():
    db.create_all()

# ================= REGISTER =================
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"].strip()
        email = request.form["email"].strip()
        password = request.form["password"].strip()
        role = request.form["role"]

        if not username or not email or not password:
            flash("All fields are required!", "error")
            return render_template("register.html")

        if User.query.filter_by(email=email).first():
            flash("Email already registered!", "error")
            return render_template("register.html")

        hashed_pw = bcrypt.generate_password_hash(password).decode("utf-8")

        user = User(
            username=username,
            email=email,
            password=hashed_pw,
            role=role
        )

        db.session.add(user)
        db.session.commit()

        flash("Registration successful! Please login.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")

# ================= LOGIN =================
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"].strip()
        password = request.form["password"].strip()

        user = User.query.filter_by(email=email).first()

        if not user:
            flash("Invalid email or password!", "error")
            return render_template("login.html")

        if user.locked:
            flash("Account locked due to multiple failed attempts!", "error")
            return render_template("login.html")

        if bcrypt.check_password_hash(user.password, password):
            user.failed_attempts = 0
            db.session.commit()

            session["user_id"] = user.id
            session["role"] = user.role

            flash("Login successful!", "success")

            if user.role == "Admin":
                return redirect(url_for("admin"))
            else:
                return redirect(url_for("dashboard"))

        else:
            user.failed_attempts += 1
            if user.failed_attempts >= 3:
                user.locked = True
            db.session.commit()

            flash("Wrong password!", "error")
            return render_template("login.html")

    return render_template("login.html")

# ================= USER DASHBOARD =================
@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("login"))

    return f"""
    <h2>User Dashboard</h2>
    <p>Welcome! You are logged in.</p>
    <p>Role: {session['role']}</p>
    <a href="/logout">Logout</a>
    """

# ================= ADMIN DASHBOARD =================
@app.route("/admin")
def admin():
    if "user_id" not in session or session.get("role") != "Admin":
        flash("Access denied!", "error")
        return redirect(url_for("login"))

    users = User.query.all()
    return render_template("admin.html", users=users)

# ================= LOGOUT =================
@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully!", "success")
    return redirect(url_for("login"))

@app.route("/")
def home():
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)

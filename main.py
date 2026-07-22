from flask import Flask, render_template, request,redirect, url_for, flash,jsonify
import sqlite3
from flask import jsonify
import requests

app = Flask(__name__)
app.secret_key = "portfolio_secret_key"

# ----------------------------
# Create Database
# ----------------------------
def create_database():

    connection = sqlite3.connect("portfolio.db")

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT,

        email TEXT,

        message TEXT

    )
    """)

    connection.commit()

    connection.close()


about = {
    "name": "Poulami Sinha",
    "role": "Python Developer",
    "college": "University of Engineering and Management",
    "cgpa": 9.23,
    "skills": [
        "Python",
        "Flask",
        "FastAPI",
        "SQL",
        "Machine Learning"
    ]
}

@app.route("/api/about")
def about_api():
    return about


# ----------------------------
#api/skills
@app.route("/api/skills")
def skills_api():

    skills = [
        {"name": "Python", "level": 95},
        {"name": "Flask", "level": 85},
        {"name": "FastAPI", "level": 75},
        {"name": "SQL", "level": 90},
        {"name": "Machine Learning", "level": 80}
    ]

    return skills


@app.route("/api/projects")
def projects_api():

    projects = [
        {
            "name": "Emotion Detection",
            "description": "A multimodal AI system."
        },
        {
            "name": "SentAI Stocks",
            "description": "AI-powered stock recommendation platform."
        },
        {
            "name": "Portfolio",
            "description": "Responsive Flask portfolio."
        }
    ]

    return projects

# ----------------------------
# Home Page
# ----------------------------
@app.route("/")
def home():
    return render_template("index.html")
#-----------------------------
#contact/api
@app.route("/api/contact", methods=["POST"])
def contact_api():

    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    connection = sqlite3.connect("portfolio.db")
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO contacts(name,email,message)
        VALUES(?,?,?)
    """, (name, email, message))

    connection.commit()
    connection.close()

    return jsonify({
        "success": True,
        "message": "Message stored successfully!"
    })
# ----------------------------
# Contact Form
# ----------------------------
@app.route("/contact", methods=["POST"])
def contact():

    # Get data from the form
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    # Open the database
    connection = sqlite3.connect("portfolio.db")

    # Create a cursor
    cursor = connection.cursor()

    # Insert the data
    cursor.execute("""
        INSERT INTO contacts(name, email, message)
        VALUES (?, ?, ?)
    """, (name, email, message))

    # Save changes
    connection.commit()

    # Close the database
    connection.close()


    flash("Thank You! Your message has been saved.", "success")
    return redirect(url_for("home"))

@app.route("/api/messages")
def get_messages():

    connection = sqlite3.connect("portfolio.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM contacts")

    rows = cursor.fetchall()

    connection.close()

    messages = []

    for row in rows:
        messages.append({
            "id": row["id"],
            "name": row["name"],
            "email": row["email"],
            "message": row["message"]
        })

    return jsonify(messages)


@app.route("/api/github")
def github():

    username = "Poulami-sinha2004"

    url = f"https://api.github.com/users/{username}/repos"

    response = requests.get(url)

    repos = response.json()

    result = []

    for repo in repos:
        result.append({
            "name": repo["name"],
            "description": repo["description"],
            "language": repo["language"],
            "url": repo["html_url"]
        })

    return jsonify(result)


@app.route("/api/github/stats")
def github_stats():

    username = "Poulami-sinha2004"

    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)

    user = response.json()

    return jsonify({
        "repositories": user["public_repos"],
        "followers": user["followers"],
        "following": user["following"],
        "profile": user["html_url"]
    })

# ----------------------------
# Run Flask
# ----------------------------
if __name__ == "__main__":

    create_database()

    app.run(debug=True)
# 🍽️ Flask Meal Planner & Recipe Finder

Simple web application built with **Flask** that allows users to:

- Generate **meal plans** based on calories and diet preferences  
- Search for **recipes** by cuisine and ingredients  
- Explore nutrition-related pages  

The app uses the **Spoonacular API** to fetch meal plans and recipes.

This project is great as a **portfolio project** for students learning Flask, APIs, and basic full-stack development (ideal for internships in IT/AI-related roles 🚀).

---

# 📌 Features

## ✅ Meal Planner
- Choose timeframe: **day / week**
- Set **target calories**
- Select diet (e.g. Vegan, Keto, Vegetarian)
- Exclude ingredients
- Fetches meal plan from Spoonacular API

## ✅ Recipe Finder
- Filter recipes by cuisine
- Include specific ingredients
- Choose number of recipes
- Displays recipe details

## ✅ Nutrition Page
- Placeholder page for future nutrition scoring or analysis

---

# 🛠️ Tech Stack

- **Backend:** Flask
- **Forms:** Flask-WTF + WTForms
- **Frontend:** Flask-Bootstrap
- **API:** Spoonacular API
- **Environment variables:** python-dotenv
- **HTTP Requests:** requests

---

# 📂 Project Structure


project/
│
├── app.py
├── templates/
│ ├── index.html
│ ├── meal_plan.html
│ ├── recipes.html
│ └── nutrition.html
│
├── static/
│ └── css/js/images
│
├── .env
└── README.md


---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/flask-meal-planner.git
cd flask-meal-planner
2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows
3️⃣ Install Dependencies
pip install flask flask-wtf flask-bootstrap requests python-dotenv
🔑 Environment Variables

Create .env file in project root:

API_KEY=your_spoonacular_api_key
SECRET=your_secret_key

You can get Spoonacular API key here:
👉 https://spoonacular.com/food-api

▶️ Run Application
python app.py

Open browser:

http://127.0.0.1:5000
📚 How It Works (Simple Explanation)

User fills form in browser

Flask receives form data

App sends request to Spoonacular API

API returns JSON with recipes/meal plans

Flask renders results in HTML templates

This is a classic example of:
👉 Frontend form → Backend Flask → External API → Render results

🧠 Possible Improvements (Good for Your CV)

Since you’re studying Informatics & Econometrics and aiming for ML roles, try adding:

🔹 Backend Improvements

Input validation & error handling

Logging instead of print()

Caching API responses

Clean Architecture (services + repositories)

🔹 Frontend Improvements

Better UI with Bootstrap cards

Loading spinners

Pagination

🔹 Data Science / AI Ideas

Recommend meals using ML model

Personal calorie prediction

Nutrition score prediction

User history & personalization

🐛 Known Issues

Missing error handling for API failures

No database (data not saved)

Nutrition page not implemented

📜 License

MIT License

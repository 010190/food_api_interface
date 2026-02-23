# 🍽️ Meal Planner & Recipe Finder

A Flask-based web application that helps users generate personalized meal plans and discover recipes based on their dietary preferences and available ingredients. This project integrates with the Spoonacular API to provide real-time recipe data and nutritional information.

---

## 🚀 Features

- **Meal Plan Generator**: Create daily or weekly meal plans based on target calories and dietary restrictions
- **Recipe Search**: Find recipes by cuisine type and available ingredients
- **Dietary Support**: Supports 12+ diet types including Vegan, Keto, Paleo, Gluten-Free, and more
- **Responsive UI**: Built with Flask-Bootstrap for mobile-friendly design
- **Secure API Handling**: Environment variables for API key management

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|-------------|
| **Backend** | Python, Flask |
| **Frontend** | HTML, Bootstrap 4, Jinja2 Templates |
| **Forms** | Flask-WTF, WTForms |
| **API** | Spoonacular API |
| **Security** | Werkzeug, python-dotenv |

---

## 📋 Prerequisites

- Python 3.7+
- Spoonacular API Key ([Get one free here](https://spoonacular.com/food-api))
- pip package manager

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/meal-planner.git
   cd meal-planner

Create a virtual environment
bash
Copy
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
Install dependencies
bash
Copy
pip install flask flask-wtf flask-bootstrap requests python-dotenv werkzeug
Set up environment variables
Create a .env file in the root directory:
env
Copy
SECRET=your_flask_secret_key_here
API_KEY=your_spoonacular_api_key_here
# 🎯 Usage
Run the application
bash
Copy
python app.py
Access the application
Open your browser and navigate to http://localhost:5000
#Explore the features
Home: Landing page with navigation
Meal Plan: Generate custom meal plans (daily/weekly)
Recipes: Search for recipes by cuisine and ingredients
NutriScore: Nutritional information page
# 📁 Project Structure
plain
Copy
meal-planner/
├── app.py                 # Main application file
├── .env                   # Environment variables (not in git)
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
└── templates/
    ├── index.html        # Home page
    ├── meal_plan.html    # Meal plan generator page
    ├── recipes.html      # Recipe search page
    ├── nutrition.html    # Nutritional info page
    └── base.html         # Base template with Bootstrap
# 🔧 Configuration
Environment Variables
Table
Copy
Variable	Description	Required
SECRET	Flask secret key for session management	Yes
API_KEY	Spoonacular API key for recipe data	Yes
Supported Diet Types
Gluten Free
Ketogenic
Vegetarian
Lacto-Vegetarian
Ovo-Vegetarian
Vegan
Pescetarian
Paleo
Primal
Low FODMAP
Whole30
Omnivore
Supported Cuisines
African
Asian
Greek
Indian
Italian
Mexican
Mediterranean
Korean
# 📝 API Endpoints
Table
Copy
Route	Method	Description
/	GET	Home page
/meal_plan	GET, POST	Generate meal plans
/recipes	GET, POST	Search recipes
/nutriscore	GET	Nutritional information
# 🔒 Security Features
✅ Environment variable management for sensitive data
✅ CSRF protection via Flask-WTF
✅ Secure password hashing with Werkzeug
✅ Input validation on all forms
🚧 Future Improvements
[ ] User authentication and saved meal plans
[ ] Shopping list generator
[ ] Nutritional breakdown charts
[ ] Recipe favorites/bookmarks
[ ] Meal prep scheduling
[ ] Grocery price estimation
#📄 License
This project is created for educational purposes as a student portfolio project.
#👨‍💻 Author
Michał Olczak
GitHub: @01019191

# 🙏 Acknowledgments
Spoonacular API for comprehensive recipe data
Flask for the lightweight web framework
Bootstrap for responsive UI components

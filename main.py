from flask import Flask, render_template
import requests
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms import DecimalField, RadioField, SelectField, TextAreaField, FileField
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import SubmitField
from wtforms.validators import InputRequired, DataRequired
from werkzeug.security import generate_password_hash
from flask_bootstrap import Bootstrap4
import os
from dotenv import load_dotenv, dotenv_values



app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET")
bootstrap = Bootstrap4(app)

load_dotenv()
API_KEY = os.getenv("API_KEY")


class MealPlan(FlaskForm):
    time_frame = SelectField('Time Frame', validators=[DataRequired()], choices=["day", "week"])
    target_calories = IntegerField("Target Calories", validators=[DataRequired()], default=0)
    diet = SelectField('Diet', validators=[DataRequired()], choices=["Gluten Free", "Ketogenic", "Vegetarian",
                                                                     "Lacto-Vegetarian", "Ovo-Vegetarian", "Vegan",
                                                                     "Pescetarian", "Paleo", "Primal", "Low FODMAP",
                                                                     "Whole30", "Omnivore"])
    exclude = StringField("Exclude ingredients", validators=[DataRequired()], default="e.g. nuts, eggs")
    submit = SubmitField('Submit')


class RecipeCasual(FlaskForm):
    cuisine = SelectField("Cuisine", validators=[DataRequired()], default="e.g. italian",
                          choices=["African", "Asian", "Greek", "Indian", "Italian", "Mexican", "Mediterranean",
                                   "Korean"])
    includeIngredients = StringField("Include ingredients", validators=[DataRequired()], default="e.g. eggs, nuts")
    number = IntegerField("How many recipes do you want?", default=1)
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route('/meal_plan', methods=['GET', 'POST'])
def meal_plan():
    form = MealPlan()
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    url = "https://api.spoonacular.com/mealplanner/generate"
    time_frame = ""
    results = 0
    if form.validate_on_submit():
        time_frame = form.data["time_frame"]

        target_calories = form.data["target_calories"]
        exclude = form.data["exclude"]
        diet = form.data["diet"]

        params = {
            "timeFrame": time_frame,

            "targetCalories": target_calories,
            # "exclude": exclude,
            "diet": diet,

        }
        data = {
            "api-key": API_KEY,
        }

        headers = {
            "x-api-key": API_KEY,
            "Content-Type": "application/json",
        }
        response = requests.get(url, headers=headers, params=params)
        print(response.raise_for_status())
        print(response.json())
        results = response.json()

    return render_template("meal_plan.html", meal_form=form, results=results, days=days, day=time_frame)


@app.route('/nutriscore', methods=['GET', 'POST'])
def nutrition():
    return render_template("nutrition.html")


@app.route('/recipes', methods=['GET', 'POST'])
def recipes():
    url = "https://api.spoonacular.com/recipes/complexSearch"
    form = RecipeCasual()
    results = 0
    if form.validate_on_submit():
        cuisine = form.data["cuisine"]
        includeIngredients = form.data["includeIngredients"]
        number = form.data["number"]

        params = {
            "cuisine": cuisine,
            "instructionsRequired": True,
            "addRecipeInformation": True,
            "includeIngredients": includeIngredients,
            "number": number,

        }

        headers = {
            "x-api-key": API_KEY,
            "Content-Type": "application/json",
        }
        response = requests.get(url, headers=headers, params=params)
        print(response.raise_for_status())
        print(response.json())
        results = response.json()['results']
        print(results)

    return render_template("recipes.html", form=form, results=results)


if __name__ == "__main__":
    app.run(debug=True)

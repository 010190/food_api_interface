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

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET")
bootstrap = Bootstrap4(app)
#
# API_KEY = "6d7fd30a19a14e5c8c822e3ffe734c05"
API_KEY = os.getenv("API_KEY")

# choices = (n for n in range(1, 10))


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

    # excludeCuisine = SelectField("Exclude cusine", validators=[DataRequired()], default="e.g. italian",  choices=["African","Asian","Greek","Indian", "Italian", "Mexican", "Mediterranean", "Korean"])
    # diet = SelectField('Diet', validators=[DataRequired()], choices=["Gluten Free", "Ketogenic", "Vegetarian",
    #                                                                  "Lacto-Vegetarian", "Ovo-Vegetarian", "Vegan",
    #                                                                  "Pescetarian", "Paleo", "Primal", "Low FODMAP",
    #                                                                  "Whole30"])
    # intolerance = SelectField(default="e.g. gluten, lactose ", choices=["None", "Dairy","Egg","Gluten","Grain", "Peanut", "Seafood", "Sesame", "Korean", "Shellfish", "Soy", "Tree Nut"])
    includeIngredients = StringField("Include ingredients", validators=[DataRequired()], default="e.g. eggs, nuts")
    # maxReadyTime = IntegerField("Maximal time for preparing in min", validators=[DataRequired()], default=30)
    number = IntegerField("How many recipes do you want?", default=1)
    # exclude = StringField("Exclude", validators=[DataRequired()], default="e.g. nuts, eggs")
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
        # response = requests.get(url, headers=headers, params=params)
        # print(response.raise_for_status())
        # print(response.json())
        # results = response.json()
        results = {
  'meals': [
    {
      'id': 636026,
      'image': 'Breakfast-Biscuits-and-Gravy-636026.jpg',
      'imageType': 'jpg',
      'title': 'Breakfast Biscuits and Gravy',
      'readyInMinutes': 45,
      'servings': 4,
      'sourceUrl': 'http://www.foodista.com/recipe/S8F5B5H4/breakfast-biscuits-and-gravy'
    },
    {
      'id': 650378,
      'image': 'Low-Carb-Curry-Chicken-Salad-650378.jpg',
      'imageType': 'jpg',
      'title': 'Curry Chicken Salad',
      'readyInMinutes': 25,
      'servings': 2,
      'sourceUrl': 'https://www.foodista.com/recipe/RSNP5GR2/low-carb-curry-chicken-salad'
    },
    {
      'id': 1697673,
      'image': 'sheet-pan-dinner-hanger-steak-with-mushrooms-and-carrots-1697673.jpg',
      'imageType': 'jpg',
      'title': 'Sheet Pan Dinner: Hanger Steak with Mushrooms and Carrots',
      'readyInMinutes': 35,
      'servings': 2,
      'sourceUrl': 'https://maplewoodroad.com/sheet-pan-dinner-hanger-steak/'
    }
  ],
  'nutrients': {
    'calories': 2932.21,
    'protein': 128.07,
    'fat': 228.5,
    'carbohydrates': 94.84
  }
}
        # results = response.json()
        # data = {'week': {'monday': {'meals': [{'id': 636026, 'image': 'Breakfast-Biscuits-and-Gravy-636026.jpg', 'imageType': 'jpg', 'title': 'Breakfast Biscuits and Gravy', 'readyInMinutes': 45, 'servings': 4, 'sourceUrl': 'http://www.foodista.com/recipe/S8F5B5H4/breakfast-biscuits-and-gravy'}, {'id': 650127, 'image': 'Linguine-in-Cream-Sauce-with-Poached-Eggs-and-Bacon-650127.jpg', 'imageType': 'jpg', 'title': 'Linguine in Cream Sauce with Poached Eggs and Bacon', 'readyInMinutes': 25, 'servings': 2, 'sourceUrl': 'https://www.foodista.com/recipe/YQQZ6X46/linguine-in-cream-sauce-with-poached-eggs-and-bacon'}, {'id': 659042, 'image': 'salmon-and-prawn-croquettes-with-lemony-jalapeno-mayonnaise-659042.jpg', 'imageType': 'jpg', 'title': 'Salmon and Prawn Croquettes With Lemony Jalapeno Mayonnaise', 'readyInMinutes': 45, 'servings': 6, 'sourceUrl': 'https://www.foodista.com/recipe/RQ3GGFD5/salmon-and-prawn-croquettes-with-lemony-jalapeno-mayonnaise'}], 'nutrients': {'calories': 2992.54, 'protein': 148.6, 'fat': 195.95, 'carbohydrates': 152.63}}, 'tuesday': {'meals': [{'id': 634882, 'image': 'Best-Breakfast-Burrito-634882.jpg', 'imageType': 'jpg', 'title': 'Best Breakfast Burrito', 'readyInMinutes': 45, 'servings': 4, 'sourceUrl': 'https://www.foodista.com/recipe/WLQNMQ5B/best-breakfast-burrito'}, {'id': 650377, 'image': 'Low-Carb-Brunch-Burger-650377.jpg', 'imageType': 'jpg', 'title': 'Low Carb Brunch Burger', 'readyInMinutes': 30, 'servings': 2, 'sourceUrl': 'https://www.foodista.com/recipe/5SPTY657/low-carb-brunch-burger'}, {'id': 663050, 'image': 'Tex-Mex-Burger-663050.jpg', 'imageType': 'jpg', 'title': 'Tex-Mex Burger', 'readyInMinutes': 15, 'servings': 4, 'sourceUrl': 'https://www.foodista.com/recipe/NSYCCHLT/tex-mex-burger'}], 'nutrients': {'calories': 2868.72, 'protein': 135.8, 'fat': 193.52, 'carbohydrates': 147.86}}, 'wednesday': {'meals': [{'id': 636026, 'image': 'Breakfast-Biscuits-and-Gravy-636026.jpg', 'imageType': 'jpg', 'title': 'Breakfast Biscuits and Gravy', 'readyInMinutes': 45, 'servings': 4, 'sourceUrl': 'http://www.foodista.com/recipe/S8F5B5H4/breakfast-biscuits-and-gravy'}, {'id': 1681413, 'image': 'macaroni-and-cheese-1681413.jpg', 'imageType': 'jpg', 'title': 'Macaroni and Cheese', 'readyInMinutes': 20, 'servings': 2, 'sourceUrl': 'http://thecuisine.blogspot.com/2016/07/macaroni-and-cheese.html'}, {'id': 661055, 'image': 'Spicy-Chili-w-Boneless-Beef-Short-Ribs-661055.jpg', 'imageType': 'jpg', 'title': 'Spicy Chili w Boneless Beef Short Ribs', 'readyInMinutes': 45, 'servings': 6, 'sourceUrl': 'http://www.foodista.com/recipe/Y4HNTZ6S/spicy-chili-w-boneless-beef-short-ribs'}], 'nutrients': {'calories': 2807.33, 'protein': 162.09, 'fat': 170.52, 'carbohydrates': 151.72}}, 'thursday': {'meals': [{'id': 635446, 'image': 'Blueberry-Cinnamon-Porridge-635446.jpg', 'imageType': 'jpg', 'title': 'Blueberry Cinnamon Porridge', 'readyInMinutes': 45, 'servings': 1, 'sourceUrl': 'https://www.foodista.com/recipe/2HVQB6LT/blueberry-cinnamon-porridge'}, {'id': 1095806, 'image': 'spanish-style-salmon-fillets-1095806.jpg', 'imageType': 'jpg', 'title': 'Spanish style salmon fillets', 'readyInMinutes': 30, 'servings': 2, 'sourceUrl': 'https://www.foodista.com/recipe/JS5W8D53/spanish-style-salmon-fillets'}, {'id': 1697599, 'image': 'baked-ziti-with-ricotta-and-italian-sausage-1697599.jpg', 'imageType': 'jpg', 'title': 'Baked Ziti with Ricotta and Italian Sausage', 'readyInMinutes': 75, 'servings': 6, 'sourceUrl': 'https://maplewoodroad.com/baked-ziti-with-ricotta-and-italian-sausage/'}], 'nutrients': {'calories': 2877.31, 'protein': 111.58, 'fat': 200.79, 'carbohydrates': 173.27}}, 'friday': {'meals': [{'id': 634882, 'image': 'Best-Breakfast-Burrito-634882.jpg', 'imageType': 'jpg', 'title': 'Best Breakfast Burrito', 'readyInMinutes': 45, 'servings': 4, 'sourceUrl': 'https://www.foodista.com/recipe/WLQNMQ5B/best-breakfast-burrito'}, {'id': 642593, 'image': 'Farfalle-With-Sun-Dried-Tomato-Pesto--Sausage-and-Fennel-642593.jpg', 'imageType': 'jpg', 'title': 'Farfalle With Sun-Dried Tomato Pesto, Sausage and Fennel', 'readyInMinutes': 20, 'servings': 4, 'sourceUrl': 'https://www.foodista.com/recipe/CSLBDWBS/farfalle-with-sun-dried-tomato-pesto-sausage-and-fennel'}, {'id': 646870, 'image': 'Home-Made-Dry-Aged-Sirloin-Steak-with-Cheesy-Roast-Fingerling-Potatoes-646870.jpg', 'imageType': 'jpg', 'title': 'Home Made Dry-Aged Sirloin Steak with Cheesy Roast Fingerling Potatoes', 'readyInMinutes': 45, 'servings': 2, 'sourceUrl': 'https://www.foodista.com/recipe/BSHVSN36/home-made-dry-aged-sirloin-steak-with-cheesy-roast-fingerling-potatoes'}], 'nutrients': {'calories': 2849.48, 'protein': 148.65, 'fat': 146.17, 'carbohydrates': 231.97}}, 'saturday': {'meals': [{'id': 636026, 'image': 'Breakfast-Biscuits-and-Gravy-636026.jpg', 'imageType': 'jpg', 'title': 'Breakfast Biscuits and Gravy', 'readyInMinutes': 45, 'servings': 4, 'sourceUrl': 'http://www.foodista.com/recipe/S8F5B5H4/breakfast-biscuits-and-gravy'}, {'id': 1095827, 'image': 'ginger-garlic-and-lime-chicken-thighs-with-escarole-salad-1095827.jpg', 'imageType': 'jpg', 'title': 'Ginger-Garlic and Lime Chicken Thighs with Escarole Salad', 'readyInMinutes': 30, 'servings': 6, 'sourceUrl': 'https://www.foodista.com/recipe/84ZD6N5S/ginger-garlic-and-lime-chicken-thighs-with-escarole-salad'}, {'id': 638248, 'image': 'Chicken-Piccata-With-Angel-Hair-Pasta-638248.jpg', 'imageType': 'jpg', 'title': 'Chicken Piccata With Angel Hair Pasta', 'readyInMinutes': 45, 'servings': 2, 'sourceUrl': 'https://www.foodista.com/recipe/7F7DBP8R/chicken-piccata-with-angel-hair-pasta'}], 'nutrients': {'calories': 2917.15, 'protein': 134.81, 'fat': 188.73, 'carbohydrates': 172.5}}, 'sunday': {'meals': [{'id': 636026, 'image': 'Breakfast-Biscuits-and-Gravy-636026.jpg', 'imageType': 'jpg', 'title': 'Breakfast Biscuits and Gravy', 'readyInMinutes': 45, 'servings': 4, 'sourceUrl': 'http://www.foodista.com/recipe/S8F5B5H4/breakfast-biscuits-and-gravy'}, {'id': 1095827, 'image': 'ginger-garlic-and-lime-chicken-thighs-with-escarole-salad-1095827.jpg', 'imageType': 'jpg', 'title': 'Ginger-Garlic and Lime Chicken Thighs with Escarole Salad', 'readyInMinutes': 30, 'servings': 6, 'sourceUrl': 'https://www.foodista.com/recipe/84ZD6N5S/ginger-garlic-and-lime-chicken-thighs-with-escarole-salad'}, {'id': 646870, 'image': 'Home-Made-Dry-Aged-Sirloin-Steak-with-Cheesy-Roast-Fingerling-Potatoes-646870.jpg', 'imageType': 'jpg', 'title': 'Home Made Dry-Aged Sirloin Steak with Cheesy Roast Fingerling Potatoes', 'readyInMinutes': 45, 'servings': 2, 'sourceUrl': 'https://www.foodista.com/recipe/BSHVSN36/home-made-dry-aged-sirloin-steak-with-cheesy-roast-fingerling-potatoes'}], 'nutrients': {'calories': 3162.4, 'protein': 175.89, 'fat': 222.47, 'carbohydrates': 110.71}}}}
        # results = data["week"]
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

        # excludeCuisine  = form.data["excludeCuisine"]
        # diet = form.data["diet"]
        # intolerance = form.data["intolerance"]
        includeIngredients = form.data["includeIngredients"]
        # maxReadyTime = form.data["maxReadyTime"]
        number = form.data["number"]
        # exclude = form.data["exclude"]

        params = {
            "cuisine": cuisine,
            "instructionsRequired": True,
            "addRecipeInformation": True,

            # "excludeCuisine": excludeCuisine,
            # "diet": diet,
            # "intolerance": intolerance,
            "includeIngredients": includeIngredients,
            # "maxReadyTime": maxReadyTime,
            "number": number,
            # "exclude": exclude,

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
        results = response.json()['results']
        print(results)
        # data = {'results': [
        #     {'id': 644826, 'image': 'https://img.spoonacular.com/recipes/644826-312x231.jpg', 'imageType': 'jpg',
        #      'title': 'Gluten Free Dairy Free Sugar Free Chinese Chicken Salad', 'readyInMinutes': 45, 'servings': 6,
        #      'sourceUrl': 'https://www.foodista.com/recipe/ZSNGMXBF/gluten-free-dairy-free-sugar-free-chinese-chicken-salad',
        #      'vegetarian': False, 'vegan': False, 'glutenFree': True, 'dairyFree': True, 'veryHealthy': True,
        #      'cheap': False, 'veryPopular': False, 'sustainable': False, 'lowFodmap': False,
        #      'weightWatcherSmartPoints': 6, 'gaps': 'no', 'preparationMinutes': None, 'cookingMinutes': None,
        #      'aggregateLikes': 3, 'healthScore': 98.0,
        #      'creditsText': 'Foodista.com – The Cooking Encyclopedia Everyone Can Edit', 'license': 'CC BY 3.0',
        #      'sourceName': 'Foodista', 'pricePerServing': 305.98,
        #      'summary': 'Gluten Free Dairy Free Sugar Free Chinese Chicken Salad is a <b>gluten free and dairy free</b> main course. This recipe serves 6 and costs $3.06 per serving. One serving contains <b>364 calories</b>, <b>31g of protein</b>, and <b>15g of fat</b>. If you have scallions, pepper, kosher salt, and a few other ingredients on hand, you can make it. This recipe from Foodista has 3 fans. Not a lot of people really liked this Chinese dish. From preparation to the plate, this recipe takes about <b>45 minutes</b>. With a spoonacular <b>score of 94%</b>, this dish is great. If you like this recipe, take a look at these similar recipes: <a href="https://spoonacular.com/recipes/gluten-free-dairy-free-sugar-free-chinese-chicken-salad-1364955">Gluten Free Dairy Free Sugar Free Chinese Chicken Salad</a>, <a href="https://spoonacular.com/recipes/thousand-island-dressing-gluten-free-corn-free-dairy-free-soy-free-nut-free-gum-free-and-refined-sugar-free-512186">Thousand Island Dressing (Gluten-Free, Corn-Free, Dairy-Free, Soy-Free, Nut-Free, Gum-Free and Refined Sugar-Free)</a>, and <a href="https://spoonacular.com/recipes/skinny-double-chocolate-muffins-vegan-gluten-free-dairy-free-egg-free-and-refined-sugar-free-1149614">Skinny Double Chocolate Muffins-Vegan, Gluten Free, Dairy Free, Egg Free and Refined Sugar Free</a>.',
        #      'cuisines': ['Chinese', 'Asian'],
        #      'dishTypes': ['side dish', 'lunch', 'salad', 'main course', 'main dish', 'dinner'],
        #      'diets': ['gluten free', 'dairy free'], 'occasions': [], 'analyzedInstructions': [{'name': '', 'steps': [
        #         {'number': 1, 'step': 'For the salad:Finely slice the red, and green cabbage.', 'ingredients': [
        #             {'id': 11109, 'name': 'green cabbage', 'localizedName': 'green cabbage', 'image': 'cabbage.jpg'}],
        #          'equipment': []}, {'number': 2,
        #                             'step': 'Remove ends and finely slice romaine lettuce.Trim ends of scallions (white and green side) and finely slice.Peel and grate carrots, or put into a mini food processor to finely chop.Peel clementines then remove pith from slices.',
        #                             'ingredients': [{'id': 10111251, 'name': 'romaine', 'localizedName': 'romaine',
        #                                              'image': 'romaine'},
        #                                             {'id': 9433, 'name': 'clementine', 'localizedName': 'clementine',
        #                                              'image': 'mandarin-or-tangerines-or-clementines.jpg'},
        #                                             {'id': 11291, 'name': 'green onions',
        #                                              'localizedName': 'green onions', 'image': 'spring-onions.jpg'},
        #                                             {'id': 11124, 'name': 'carrot', 'localizedName': 'carrot',
        #                                              'image': 'sliced-carrot.png'}], 'equipment': [
        #                 {'id': 404771, 'name': 'food processor', 'localizedName': 'food processor',
        #                  'image': 'https://spoonacular.com/cdn/equipment_100x100/food-processor.png'}]}]}, {
        #                                                                                            'name': 'Add all the ingredients into a large serving bowl.For the dressing',
        #                                                                                            'steps': [
        #                                                                                                {'number': 1,
        #                                                                                                 'step': 'Add all the ingredients into a glass jar and shake until well blended, or whisk all the ingredients in a mixing bowl.',
        #                                                                                                 'ingredients': [
        #                                                                                                     {'id': 0,
        #                                                                                                      'name': 'shake',
        #                                                                                                      'localizedName': 'shake',
        #                                                                                                      'image': ''}],
        #                                                                                                 'equipment': [{
        #                                                                                                                   'id': 405907,
        #                                                                                                                   'name': 'mixing bowl',
        #                                                                                                                   'localizedName': 'mixing bowl',
        #                                                                                                                   'image': 'https://spoonacular.com/cdn/equipment_100x100/mixing-bowl.jpg'},
        #                                                                                                               {
        #                                                                                                                   'id': 404661,
        #                                                                                                                   'name': 'whisk',
        #                                                                                                                   'localizedName': 'whisk',
        #                                                                                                                   'image': 'https://spoonacular.com/cdn/equipment_100x100/whisk.png'}]},
        #                                                                                                {'number': 2,
        #                                                                                                 'step': 'Pour dressing over salad, toss to combine well.If making ahead, dress the salad just before serving.',
        #                                                                                                 'ingredients': [],
        #                                                                                                 'equipment': []}]}],
        #      'spoonacularScore': 95.1800308227539,
        #      'spoonacularSourceUrl': 'https://spoonacular.com/gluten-free-dairy-free-sugar-free-chinese-chicken-salad-644826'},
        #     {'id': 633088, 'image': 'https://img.spoonacular.com/recipes/633088-312x231.jpg', 'imageType': 'jpg',
        #      'title': 'Authentic Jamaican Curry Chicken', 'readyInMinutes': 45, 'servings': 4,
        #      'sourceUrl': 'https://www.foodista.com/recipe/VVMBG4PD/authentic-jamaican-curry-chicken',
        #      'vegetarian': False, 'vegan': False, 'glutenFree': True, 'dairyFree': True, 'veryHealthy': False,
        #      'cheap': False, 'veryPopular': False, 'sustainable': False, 'lowFodmap': False,
        #      'weightWatcherSmartPoints': 9, 'gaps': 'no', 'preparationMinutes': None, 'cookingMinutes': None,
        #      'aggregateLikes': 4, 'healthScore': 54.0,
        #      'creditsText': 'Foodista.com – The Cooking Encyclopedia Everyone Can Edit', 'license': 'CC BY 3.0',
        #      'sourceName': 'Foodista', 'pricePerServing': 401.56,
        #      'summary': 'If you want to add more <b>gluten free, dairy free, paleolithic, and primal</b> recipes to your recipe box, Authentic Jamaican Curry Chicken might be a recipe you should try. This recipe serves 4. For <b>$4.02 per serving</b>, this recipe <b>covers 46%</b> of your daily requirements of vitamins and minerals. This main course has <b>587 calories</b>, <b>70g of protein</b>, and <b>19g of fat</b> per serving. 4 people have made this recipe and would make it again. Not a lot of people really liked this Indian dish. This recipe from Foodista requires thyme, scallions, scotch bonnet pepper, and sweet potatoes. From preparation to the plate, this recipe takes about <b>45 minutes</b>. All things considered, we decided this recipe <b>deserves a spoonacular score of 87%</b>. This score is great. Try <a href="https://spoonacular.com/recipes/authentic-jamaican-curry-chicken-1261085">Authentic Jamaican Curry Chicken</a>, <a href="https://spoonacular.com/recipes/authentic-jamaican-curry-chicken-1258495">Authentic Jamaican Curry Chicken</a>, and <a href="https://spoonacular.com/recipes/authentic-jamaican-brown-stew-chicken-107028">Authentic Jamaican Brown Stew Chicken</a> for similar recipes.',
        #      'cuisines': ['Indian', 'Asian'], 'dishTypes': ['lunch', 'main course', 'main dish', 'dinner'],
        #      'diets': ['gluten free', 'dairy free', 'paleolithic', 'primal', 'whole 30'], 'occasions': [],
        #      'analyzedInstructions': [{'name': '', 'steps': [{'number': 1,
        #                                                       'step': 'Season the chicken with all of the ingredients except for the potatoes and water and marinate up to 2 hours or overnight in the fridge.',
        #                                                       'ingredients': [{'id': 11352, 'name': 'potato',
        #                                                                        'localizedName': 'potato',
        #                                                                        'image': 'potatoes-yukon-gold.png'},
        #                                                                       {'id': 0, 'name': 'chicken',
        #                                                                        'localizedName': 'chicken',
        #                                                                        'image': 'https://spoonacular.com/cdn/ingredients_100x100/whole-chicken.jpg'},
        #                                                                       {'id': 14412, 'name': 'water',
        #                                                                        'localizedName': 'water',
        #                                                                        'image': 'water.png'}], 'equipment': [],
        #                                                       'length': {'number': 120, 'unit': 'minutes'}},
        #                                                      {'number': 2,
        #                                                       'step': 'Add the oil to a Dutch oven and on high heat, fry the only the chicken pieces until it is brown and seared on each side for about 10 minutes.After the meat is nice and brown on both sides, add the remaining vegetable marinade, scotch bonnet pepper and water to the pot, cover and bring to a boil.',
        #                                                       'ingredients': [
        #                                                           {'id': 10011819, 'name': 'scotch bonnet chili',
        #                                                            'localizedName': 'scotch bonnet chili',
        #                                                            'image': 'scotch-bonnet-chile.jpg'},
        #                                                           {'id': 1005006, 'name': 'chicken pieces',
        #                                                            'localizedName': 'chicken pieces',
        #                                                            'image': 'chicken-parts.jpg'},
        #                                                           {'id': 11583, 'name': 'vegetable',
        #                                                            'localizedName': 'vegetable',
        #                                                            'image': 'https://spoonacular.com/cdn/ingredients_100x100/mixed-vegetables.png'},
        #                                                           {'id': 0, 'name': 'marinade',
        #                                                            'localizedName': 'marinade',
        #                                                            'image': 'seasoning.png'},
        #                                                           {'id': 14412, 'name': 'water',
        #                                                            'localizedName': 'water', 'image': 'water.png'},
        #                                                           {'id': 1065062, 'name': 'meat',
        #                                                            'localizedName': 'meat',
        #                                                            'image': 'whole-chicken.jpg'},
        #                                                           {'id': 4582, 'name': 'cooking oil',
        #                                                            'localizedName': 'cooking oil',
        #                                                            'image': 'vegetable-oil.jpg'}], 'equipment': [
        #                                                          {'id': 404667, 'name': 'dutch oven',
        #                                                           'localizedName': 'dutch oven',
        #                                                           'image': 'https://spoonacular.com/cdn/equipment_100x100/dutch-oven.jpg'}],
        #                                                       'length': {'number': 10, 'unit': 'minutes'}},
        #                                                      {'number': 3,
        #                                                       'step': 'Add the potatoes and lower to a simmer and stew it for about 1 hour until it has a thick consistency.',
        #                                                       'ingredients': [{'id': 11352, 'name': 'potato',
        #                                                                        'localizedName': 'potato',
        #                                                                        'image': 'potatoes-yukon-gold.png'},
        #                                                                       {'id': 0, 'name': 'stew',
        #                                                                        'localizedName': 'stew', 'image': ''}],
        #                                                       'equipment': [],
        #                                                       'length': {'number': 60, 'unit': 'minutes'}}]}],
        #      'spoonacularScore': 89.30965423583984,
        #      'spoonacularSourceUrl': 'https://spoonacular.com/authentic-jamaican-curry-chicken-633088'},
        #     {'id': 638642, 'image': 'https://img.spoonacular.com/recipes/638642-312x231.jpg', 'imageType': 'jpg',
        #      'title': 'Chinese Chicken Salad With Chipotle Dressing', 'readyInMinutes': 45, 'servings': 4,
        #      'sourceUrl': 'https://www.foodista.com/recipe/JHBGMT48/bobby-flays-chinese-chicken-salad-with-chile-pea-mond-dressing',
        #      'vegetarian': False, 'vegan': False, 'glutenFree': True, 'dairyFree': True, 'veryHealthy': False,
        #      'cheap': False, 'veryPopular': False, 'sustainable': False, 'lowFodmap': False,
        #      'weightWatcherSmartPoints': 20, 'gaps': 'no', 'preparationMinutes': None, 'cookingMinutes': None,
        #      'aggregateLikes': 7, 'healthScore': 45.0,
        #      'creditsText': 'Foodista.com – The Cooking Encyclopedia Everyone Can Edit', 'license': 'CC BY 3.0',
        #      'sourceName': 'Foodista', 'pricePerServing': 390.43,
        #      'summary': 'The recipe Chinese Chicken Salad With Chipotle Dressing is ready <b>in roughly 45 minutes</b> and is definitely a tremendous <b>gluten free and dairy free</b> option for lovers of Chinese food. For <b>$3.9 per serving</b>, this recipe <b>covers 39%</b> of your daily requirements of vitamins and minerals. This main course has <b>780 calories</b>, <b>51g of protein</b>, and <b>46g of fat</b> per serving. This recipe serves 4. 7 people were impressed by this recipe. Head to the store and pick up romaine lettuce, carrots, mint leaves, and a few other things to make it today. It is brought to you by Foodista. All things considered, we decided this recipe <b>deserves a spoonacular score of 86%</b>. This score is spectacular. If you like this recipe, you might also like recipes such as <a href="https://spoonacular.com/recipes/chinese-chicken-salad-with-sesame-dressing-1226459">Chinese Chicken Salad with Sesame Dressing</a>, <a href="https://spoonacular.com/recipes/chinese-chicken-salad-with-sesame-dressing-510753">Chinese Chicken Salad with Sesame Dressing</a>, and <a href="https://spoonacular.com/recipes/doms-chinese-chicken-salad-dressing-143924">Dom\'s Chinese Chicken Salad Dressing</a>.',
        #      'cuisines': ['Chinese', 'Asian'],
        #      'dishTypes': ['side dish', 'lunch', 'salad', 'main course', 'main dish', 'dinner'],
        #      'diets': ['gluten free', 'dairy free'], 'occasions': [], 'analyzedInstructions': [{'name': 'Dressing',
        #                                                                                         'steps': [{'number': 1,
        #                                                                                                    'step': 'Whisk together the vinegar, peanut & almond butters, ginger, chipotle pepper puree, soy sauce, honey, sesame oil, and canola oil in a medium bowl. Season with salt and pepper, to taste.',
        #                                                                                                    'ingredients': [
        #                                                                                                        {
        #                                                                                                            'id': 98839,
        #                                                                                                            'name': 'chipotle chiles',
        #                                                                                                            'localizedName': 'chipotle chiles',
        #                                                                                                            'image': 'chile-chipotle.jpg'},
        #                                                                                                        {
        #                                                                                                            'id': 1102047,
        #                                                                                                            'name': 'salt and pepper',
        #                                                                                                            'localizedName': 'salt and pepper',
        #                                                                                                            'image': 'salt-and-pepper.jpg'},
        #                                                                                                        {
        #                                                                                                            'id': 1014582,
        #                                                                                                            'name': 'canola oil',
        #                                                                                                            'localizedName': 'canola oil',
        #                                                                                                            'image': 'vegetable-oil.jpg'},
        #                                                                                                        {
        #                                                                                                            'id': 4058,
        #                                                                                                            'name': 'sesame oil',
        #                                                                                                            'localizedName': 'sesame oil',
        #                                                                                                            'image': 'sesame-oil.png'},
        #                                                                                                        {
        #                                                                                                            'id': 16124,
        #                                                                                                            'name': 'soy sauce',
        #                                                                                                            'localizedName': 'soy sauce',
        #                                                                                                            'image': 'soy-sauce.jpg'},
        #                                                                                                        {
        #                                                                                                            'id': 2053,
        #                                                                                                            'name': 'vinegar',
        #                                                                                                            'localizedName': 'vinegar',
        #                                                                                                            'image': 'vinegar-(white).jpg'},
        #                                                                                                        {
        #                                                                                                            'id': 12061,
        #                                                                                                            'name': 'almonds',
        #                                                                                                            'localizedName': 'almonds',
        #                                                                                                            'image': 'almonds.jpg'},
        #                                                                                                        {
        #                                                                                                            'id': 11216,
        #                                                                                                            'name': 'ginger',
        #                                                                                                            'localizedName': 'ginger',
        #                                                                                                            'image': 'ginger.png'},
        #                                                                                                        {
        #                                                                                                            'id': 16091,
        #                                                                                                            'name': 'peanuts',
        #                                                                                                            'localizedName': 'peanuts',
        #                                                                                                            'image': 'peanuts.png'},
        #                                                                                                        {
        #                                                                                                            'id': 19296,
        #                                                                                                            'name': 'honey',
        #                                                                                                            'localizedName': 'honey',
        #                                                                                                            'image': 'honey.png'}],
        #                                                                                                    'equipment': [
        #                                                                                                        {
        #                                                                                                            'id': 404661,
        #                                                                                                            'name': 'whisk',
        #                                                                                                            'localizedName': 'whisk',
        #                                                                                                            'image': 'https://spoonacular.com/cdn/equipment_100x100/whisk.png'},
        #                                                                                                        {
        #                                                                                                            'id': 404783,
        #                                                                                                            'name': 'bowl',
        #                                                                                                            'localizedName': 'bowl',
        #                                                                                                            'image': 'https://spoonacular.com/cdn/equipment_100x100/bowl.jpg'}]}]},
        #                                                                                        {'name': 'Salad',
        #                                                                                         'steps': [{'number': 1,
        #                                                                                                    'step': 'Combine cabbage, lettuce, carrots, snow peas, cilantro, and green onion in a large bowl.',
        #                                                                                                    'ingredients': [
        #                                                                                                        {
        #                                                                                                            'id': 11291,
        #                                                                                                            'name': 'green onions',
        #                                                                                                            'localizedName': 'green onions',
        #                                                                                                            'image': 'spring-onions.jpg'},
        #                                                                                                        {
        #                                                                                                            'id': 11300,
        #                                                                                                            'name': 'snow peas',
        #                                                                                                            'localizedName': 'snow peas',
        #                                                                                                            'image': 'snow-peas.jpg'},
        #                                                                                                        {
        #                                                                                                            'id': 11165,
        #                                                                                                            'name': 'cilantro',
        #                                                                                                            'localizedName': 'cilantro',
        #                                                                                                            'image': 'cilantro.png'},
        #                                                                                                        {
        #                                                                                                            'id': 11109,
        #                                                                                                            'name': 'cabbage',
        #                                                                                                            'localizedName': 'cabbage',
        #                                                                                                            'image': 'cabbage.jpg'},
        #                                                                                                        {
        #                                                                                                            'id': 11124,
        #                                                                                                            'name': 'carrot',
        #                                                                                                            'localizedName': 'carrot',
        #                                                                                                            'image': 'sliced-carrot.png'},
        #                                                                                                        {
        #                                                                                                            'id': 11252,
        #                                                                                                            'name': 'lettuce',
        #                                                                                                            'localizedName': 'lettuce',
        #                                                                                                            'image': 'iceberg-lettuce.jpg'}],
        #                                                                                                    'equipment': [
        #                                                                                                        {
        #                                                                                                            'id': 404783,
        #                                                                                                            'name': 'bowl',
        #                                                                                                            'localizedName': 'bowl',
        #                                                                                                            'image': 'https://spoonacular.com/cdn/equipment_100x100/bowl.jpg'}]},
        #                                                                                                   {'number': 2,
        #                                                                                                    'step': 'Add the dressing and toss to combine.',
        #                                                                                                    'ingredients': [],
        #                                                                                                    'equipment': []},
        #                                                                                                   {'number': 3,
        #                                                                                                    'step': 'Transfer to a serving platter and top with the shredded chicken, chopped peanuts, and mint.',
        #                                                                                                    'ingredients': [
        #                                                                                                        {
        #                                                                                                            'id': 1005114,
        #                                                                                                            'name': 'shredded chicken',
        #                                                                                                            'localizedName': 'shredded chicken',
        #                                                                                                            'image': 'rotisserie-chicken.png'},
        #                                                                                                        {
        #                                                                                                            'id': 16091,
        #                                                                                                            'name': 'peanuts',
        #                                                                                                            'localizedName': 'peanuts',
        #                                                                                                            'image': 'peanuts.png'},
        #                                                                                                        {
        #                                                                                                            'id': 2064,
        #                                                                                                            'name': 'mint',
        #                                                                                                            'localizedName': 'mint',
        #                                                                                                            'image': 'mint.jpg'}],
        #                                                                                                    'equipment': []},
        #                                                                                                   {'number': 4,
        #                                                                                                    'step': 'Drizzle with chili oil, if desired.',
        #                                                                                                    'ingredients': [
        #                                                                                                        {
        #                                                                                                            'id': 1014053,
        #                                                                                                            'name': 'chili oil',
        #                                                                                                            'localizedName': 'chili oil',
        #                                                                                                            'image': 'chili-oil.jpg'}],
        #                                                                                                    'equipment': []},
        #                                                                                                   {'number': 5,
        #                                                                                                    'step': 'Garnish with lime halves.',
        #                                                                                                    'ingredients': [
        #                                                                                                        {
        #                                                                                                            'id': 9159,
        #                                                                                                            'name': 'lime',
        #                                                                                                            'localizedName': 'lime',
        #                                                                                                            'image': 'lime.jpg'}],
        #                                                                                                    'equipment': []}]}],
        #      'spoonacularScore': 88.9572525024414,
        #      'spoonacularSourceUrl': 'https://spoonacular.com/chinese-chicken-salad-with-chipotle-dressing-638642'},
        #     {'id': 641908, 'image': 'https://img.spoonacular.com/recipes/641908-312x231.jpg', 'imageType': 'jpg',
        #      'title': 'Easy Chicken Tikka Masala', 'readyInMinutes': 45, 'servings': 4,
        #      'sourceUrl': 'https://www.foodista.com/recipe/7Q3RC88N/easy-chicken-tikka-masala', 'vegetarian': False,
        #      'vegan': False, 'glutenFree': True, 'dairyFree': False, 'veryHealthy': False, 'cheap': False,
        #      'veryPopular': False, 'sustainable': False, 'lowFodmap': False, 'weightWatcherSmartPoints': 8,
        #      'gaps': 'no', 'preparationMinutes': None, 'cookingMinutes': None, 'aggregateLikes': 54,
        #      'healthScore': 25.0, 'creditsText': 'Foodista.com – The Cooking Encyclopedia Everyone Can Edit',
        #      'license': 'CC BY 3.0', 'sourceName': 'Foodista', 'pricePerServing': 219.1,
        #      'summary': 'Easy Chicken Tikka Masala might be a good recipe to expand your main course recipe box. One serving contains <b>371 calories</b>, <b>38g of protein</b>, and <b>20g of fat</b>. This gluten free recipe serves 4 and costs <b>$2.19 per serving</b>. 54 people were glad they tried this recipe. If you have salt, water, onion, and a few other ingredients on hand, you can make it. From preparation to the plate, this recipe takes about <b>45 minutes</b>. This recipe is typical of Indian cuisine. It is brought to you by Foodista. All things considered, we decided this recipe <b>deserves a spoonacular score of 84%</b>. This score is excellent. If you like this recipe, take a look at these similar recipes: <a href="https://spoonacular.com/recipes/easy-chicken-tikka-masala-1073355">Easy Chicken Tikka Masala</a>, <a href="https://spoonacular.com/recipes/easy-chicken-tikka-masala-671187">Easy Chicken Tikka Masala</a>, and <a href="https://spoonacular.com/recipes/easy-chicken-tikka-masala-1554183">Easy Chicken Tikka Masala</a>.',
        #      'cuisines': ['Indian', 'Asian'], 'dishTypes': ['lunch', 'main course', 'main dish', 'dinner'],
        #      'diets': ['gluten free'], 'occasions': [], 'analyzedInstructions': [{'name': '', 'steps': [
        #         {'number': 1, 'step': 'In a small bowl mix all the spices including the ginger. Set aside.',
        #          'ingredients': [{'id': 11216, 'name': 'ginger', 'localizedName': 'ginger', 'image': 'ginger.png'},
        #                          {'id': 2035, 'name': 'spices', 'localizedName': 'spices', 'image': 'spices.png'}],
        #          'equipment': [{'id': 404783, 'name': 'bowl', 'localizedName': 'bowl',
        #                         'image': 'https://spoonacular.com/cdn/equipment_100x100/bowl.jpg'}]},
        #         {'number': 2, 'step': 'In a large saucepan, heat the oil .', 'ingredients': [
        #             {'id': 4582, 'name': 'cooking oil', 'localizedName': 'cooking oil', 'image': 'vegetable-oil.jpg'}],
        #          'equipment': [{'id': 404669, 'name': 'sauce pan', 'localizedName': 'sauce pan',
        #                         'image': 'https://spoonacular.com/cdn/equipment_100x100/sauce-pan.jpg'}]},
        #         {'number': 3, 'step': 'Add the onions and cook until golden brown.',
        #          'ingredients': [{'id': 11282, 'name': 'onion', 'localizedName': 'onion', 'image': 'brown-onion.png'}],
        #          'equipment': []}, {'number': 4, 'step': 'Add the garlic and continue to cook for a minute.',
        #                             'ingredients': [{'id': 11215, 'name': 'garlic', 'localizedName': 'garlic',
        #                                              'image': 'garlic.png'}], 'equipment': []},
        #         {'number': 5, 'step': 'Stir in the spices and allow the flavours to infuse.',
        #          'ingredients': [{'id': 2035, 'name': 'spices', 'localizedName': 'spices', 'image': 'spices.png'}],
        #          'equipment': []}, {'number': 6, 'step': 'Stir in the tomato paste.', 'ingredients': [
        #             {'id': 11887, 'name': 'tomato paste', 'localizedName': 'tomato paste',
        #              'image': 'tomato-paste.jpg'}], 'equipment': []}, {'number': 7,
        #                                                                'step': 'Add the chopped tomato and pour in the water. Simmer and season with salt to taste.',
        #                                                                'ingredients': [{'id': 11529, 'name': 'tomato',
        #                                                                                 'localizedName': 'tomato',
        #                                                                                 'image': 'tomato.png'},
        #                                                                                {'id': 14412, 'name': 'water',
        #                                                                                 'localizedName': 'water',
        #                                                                                 'image': 'water.png'},
        #                                                                                {'id': 2047, 'name': 'salt',
        #                                                                                 'localizedName': 'salt',
        #                                                                                 'image': 'salt.jpg'}],
        #                                                                'equipment': []}, {'number': 8,
        #                                                                                   'step': 'Add the chicken pieces stirring well to coat the meat with the sauce. Continue to simmer until the chicken is cooked and the sauce has thickened, about 12 minutes.',
        #                                                                                   'ingredients': [
        #                                                                                       {'id': 1005006,
        #                                                                                        'name': 'chicken pieces',
        #                                                                                        'localizedName': 'chicken pieces',
        #                                                                                        'image': 'chicken-parts.jpg'},
        #                                                                                       {'id': 0,
        #                                                                                        'name': 'chicken',
        #                                                                                        'localizedName': 'chicken',
        #                                                                                        'image': 'https://spoonacular.com/cdn/ingredients_100x100/whole-chicken.jpg'},
        #                                                                                       {'id': 0, 'name': 'sauce',
        #                                                                                        'localizedName': 'sauce',
        #                                                                                        'image': ''},
        #                                                                                       {'id': 1065062,
        #                                                                                        'name': 'meat',
        #                                                                                        'localizedName': 'meat',
        #                                                                                        'image': 'whole-chicken.jpg'}],
        #                                                                                   'equipment': [],
        #                                                                                   'length': {'number': 12,
        #                                                                                              'unit': 'minutes'}},
        #         {'number': 9, 'step': 'Stir in the yogurt and continue to simmer 5 minutes.', 'ingredients': [
        #             {'id': 1116, 'name': 'yogurt', 'localizedName': 'yogurt', 'image': 'plain-yogurt.jpg'}],
        #          'equipment': [], 'length': {'number': 5, 'unit': 'minutes'}},
        #         {'number': 10, 'step': 'Garnish with chopped fresh cilantro', 'ingredients': [
        #             {'id': 11165, 'name': 'fresh cilantro', 'localizedName': 'fresh cilantro',
        #              'image': 'cilantro.png'}], 'equipment': []}, {'number': 11, 'step': 'Serve with bismati rice.',
        #                                                            'ingredients': [{'id': 20444, 'name': 'rice',
        #                                                                             'localizedName': 'rice',
        #                                                                             'image': 'uncooked-white-rice.png'}],
        #                                                            'equipment': []}]}],
        #      'spoonacularScore': 87.6030044555664,
        #      'spoonacularSourceUrl': 'https://spoonacular.com/easy-chicken-tikka-masala-641908'},
        #     {'id': 638649, 'image': 'https://img.spoonacular.com/recipes/638649-312x231.jpg', 'imageType': 'jpg',
        #      'title': 'Chinese Chicken Salad With Creamy Soy Dressing', 'readyInMinutes': 30, 'servings': 2,
        #      'sourceUrl': 'https://www.foodista.com/recipe/BPHS2ZXF/chinese-chicken-salad-with-creamy-soy-dressing',
        #      'vegetarian': False, 'vegan': False, 'glutenFree': True, 'dairyFree': False, 'veryHealthy': True,
        #      'cheap': False, 'veryPopular': False, 'sustainable': False, 'lowFodmap': False,
        #      'weightWatcherSmartPoints': 4, 'gaps': 'no', 'preparationMinutes': None, 'cookingMinutes': None,
        #      'aggregateLikes': 1, 'healthScore': 59.0,
        #      'creditsText': 'Foodista.com – The Cooking Encyclopedia Everyone Can Edit', 'license': 'CC BY 3.0',
        #      'sourceName': 'Foodista', 'pricePerServing': 325.28,
        #      'summary': 'Chinese Chicken Salad With Creamy Soy Dressing takes roughly <b>30 minutes</b> from beginning to end. This recipe makes 2 servings with <b>316 calories</b>, <b>50g of protein</b>, and <b>7g of fat</b> each. For <b>$3.25 per serving</b>, this recipe <b>covers 38%</b> of your daily requirements of vitamins and minerals. If you have chicken breast, snow peas, ginger root, and a few other ingredients on hand, you can make it. This recipe is typical of Chinese cuisine. It is brought to you by Foodista. 1 person has made this recipe and would make it again. It is a good option if you\'re following a <b>gluten free</b> diet. It works well as a main course. With a spoonacular <b>score of 85%</b>, this dish is super. Similar recipes are <a href="https://spoonacular.com/recipes/chinese-chicken-salad-with-soy-ginger-dressing-712588">Chinese Chicken Salad with Soy Ginger Dressing</a>, <a href="https://spoonacular.com/recipes/hearts-of-romaine-salad-with-creamy-soy-dressing-16772">Hearts of Romaine Salad with Creamy Soy Dressing</a>, and <a href="https://spoonacular.com/recipes/marinated-tofu-avocado-and-spinach-salad-with-creamy-toasted-sesame-soy-dressing-905643">Marinated Tofu, Avocado, and Spinach Salad with Creamy Toasted Sesame & Soy Dressing</a>.',
        #      'cuisines': ['Chinese', 'Asian'],
        #      'dishTypes': ['side dish', 'lunch', 'salad', 'main course', 'main dish', 'dinner'],
        #      'diets': ['gluten free'], 'occasions': [], 'analyzedInstructions': [{'name': '', 'steps': [
        #         {'number': 1, 'step': 'Whisk mayonnaise, soy sauce and ginger together in a large bowl until blended.',
        #          'ingredients': [
        #              {'id': 4025, 'name': 'mayonnaise', 'localizedName': 'mayonnaise', 'image': 'mayonnaise.png'},
        #              {'id': 16124, 'name': 'soy sauce', 'localizedName': 'soy sauce', 'image': 'soy-sauce.jpg'},
        #              {'id': 11216, 'name': 'ginger', 'localizedName': 'ginger', 'image': 'ginger.png'}], 'equipment': [
        #             {'id': 404661, 'name': 'whisk', 'localizedName': 'whisk',
        #              'image': 'https://spoonacular.com/cdn/equipment_100x100/whisk.png'},
        #             {'id': 404783, 'name': 'bowl', 'localizedName': 'bowl',
        #              'image': 'https://spoonacular.com/cdn/equipment_100x100/bowl.jpg'}]},
        #         {'number': 2, 'step': 'Add chicken, snow peas, peppers, carrots and green onion; toss to mix and coat.',
        #          'ingredients': [{'id': 11291, 'name': 'green onions', 'localizedName': 'green onions',
        #                           'image': 'spring-onions.jpg'},
        #                          {'id': 11300, 'name': 'snow peas', 'localizedName': 'snow peas',
        #                           'image': 'snow-peas.jpg'}, {'id': 11124, 'name': 'carrot', 'localizedName': 'carrot',
        #                                                       'image': 'sliced-carrot.png'},
        #                          {'id': 0, 'name': 'chicken', 'localizedName': 'chicken',
        #                           'image': 'https://spoonacular.com/cdn/ingredients_100x100/whole-chicken.jpg'},
        #                          {'id': 10111333, 'name': 'peppers', 'localizedName': 'peppers',
        #                           'image': 'green-pepper.jpg'}], 'equipment': []},
        #         {'number': 3, 'step': 'Serve over torn spinach leaves.', 'ingredients': [
        #             {'id': 10011457, 'name': 'spinach', 'localizedName': 'spinach', 'image': 'spinach.jpg'}],
        #          'equipment': []}]}], 'spoonacularScore': 86.82758331298828,
        #      'spoonacularSourceUrl': 'https://spoonacular.com/chinese-chicken-salad-with-creamy-soy-dressing-638649'}],
        #         'offset': 0, 'number': 5, 'totalResults': 65}
        #
        # results = data["results"]
    return render_template("recipes.html", form=form, results=results)


if __name__ == "__main__":
    app.run(debug=True)

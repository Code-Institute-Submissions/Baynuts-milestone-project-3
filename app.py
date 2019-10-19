import os
import json
from flask import Flask, render_template, redirect, request, url_for, flash, jsonify, session, abort
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'online_cookbook'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

mongo = PyMongo(app)
login_manager = LoginManager(app)
login_manager.login_view = 'user_login'

class User:
    def __init__(self, username):
        self.username = username

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username

    @staticmethod
    def check_password(password_hash, password):
        return check_password_hash(password_hash, password)

    @login_manager.user_loader
    def load_user(username):
        site_user = mongo.db.users.find_one({"username": username})
        if not site_user:
            return None
        return User(site_user)

class form_user_sign_up(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    
class form_user_login(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

class form_update_user(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
    
@app.route('/login_page', methods=['GET', 'POST'])
def login_page():
    form = form_user_login()
    return render_template("login.html", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = form_user_login()
    users = mongo.db.users
    if request.method == 'GET' and current_user.is_authenticated:
        return render_template("index.html")
    if request.method == 'POST':
        the_user = users.find_one({"username": form.username.data.lower()})
        if the_user and User.check_password(the_user["password"], form.password.data):
            user_obj = User(the_user["username"])
            login_user(user_obj)
            return render_template("index.html", users=users, user=the_user)
    error = "You have entered the wrong username / password"
    return render_template("login.html", form=form)

@app.route('/sign_up_page', methods=['GET', 'POST'])
def sign_up_page():
    sign_up_form = form_user_sign_up()
    return render_template("signup.html", form=sign_up_form)

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    users = mongo.db.users
    form = form_user_sign_up()
    registered_user = users.find_one({'username': form.username.data})
    if registered_user is None:
        passwordhash = generate_password_hash(form.password.data, method="sha256")
        new_user = {
            'username': form.username.data.lower(),
            'password': passwordhash,
        }
        users.insert_one(new_user)
        return redirect(url_for('login_page'))
        
    return render_template("signup.html", form=form)

@app.route('/logout')
def logout():
    logout_user()
    return render_template("index.html")

@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())
        
@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("viewrecipe.html", recipe=the_recipe)    
        
@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html", nationality=mongo.db.nationality.find(), rating=mongo.db.rating.find(), serves=mongo.db.serves.find(), category=mongo.db.category.find())
    
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipe = mongo.db.recipes
    recipe.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))
    
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_nationality =  mongo.db.nationality.find()
    all_ratings = mongo.db.rating.find()
    all_serves = mongo.db.serves.find()
    all_category = mongo.db.category.find()
    return render_template('editrecipe.html', recipe=the_recipe, nationality=all_nationality, rating=all_ratings, serves=all_serves, category=all_category)        
        
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name':request.form.get('recipe_name'),
        'overview':request.form.get('overview'),
        'url': request.form.get('url'),
        'rating': request.form.get('rating'),
        'serves':request.form.get('serves'),
        'cook_time':request.form.get('cook_time'),
        'prep_time':request.form.get('prep_time'),
        'ingredient_1':request.form.get('ingredient_1'),      
        'ingredient_2':request.form.get('ingredient_2'),   
        'ingredient_3':request.form.get('ingredient_3'),   
        'ingredient_4':request.form.get('ingredient_4'),   
        'ingredient_5':request.form.get('ingredient_5'),   
        'ingredient_6':request.form.get('ingredient_6'),   
        'ingredient_7':request.form.get('ingredient_7'),   
        'ingredient_8':request.form.get('ingredient_8'),   
        'ingredient_9':request.form.get('ingredient_9'),   
        'ingredient_10':request.form.get('ingredient_10'),   
        'ingredient_11':request.form.get('ingredient_11'), 
        'ingredient_12':request.form.get('ingredient_12'),         
        'method_1':request.form.get('method_1'),   
        'method_2':request.form.get('method_2'), 
        'method_3':request.form.get('method_3'), 
        'method_4':request.form.get('method_4'), 
        'method_5':request.form.get('method_5'), 
        'method_6':request.form.get('method_6'), 
        'method_7':request.form.get('method_7'),     
        'method_8':request.form.get('method_8'),  
        'category':request.form.get('category'),            
        'nationality':request.form.get('nationality')          
    })
    return redirect(url_for('get_recipes'))

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipe.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
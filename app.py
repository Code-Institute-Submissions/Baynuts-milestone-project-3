import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'online_cookbook'
app.config["MONGO_URI"] = 'mongodb+srv://MongoUser9:yEO9UgPTpAfbcTH4@mongocluster-k8ube.mongodb.net/online_cookbook?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')

@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())
    
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
            
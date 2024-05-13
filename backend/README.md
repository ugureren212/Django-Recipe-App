# Recipe App Back End

This is a the backend for the recipe application.

This application needs to be ran in a seperate terminal along side the front end application.

Tech stach: Django , Python, Postgress

### Install requirements, Run server

```
pip install -r requirements.txt

python manage.py runserver
```

### Migrate database

```
python manage.py migrate

python manage.py makemigrations
```

### Database

This application uses postgress. The data models used to store the data can be found in recipesAPI/models.py

A recipe is broken into 2 parts. Recipe and Ingrediant.

The combination of both is stored in a join table called RecipeIngredient

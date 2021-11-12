This project is a complete end to end implementation of Store Sales Prediction using Machine Learning with DVC and MLFlow for Data Versioning and Model profiling to track the performance of the ML model.

The Steps involved in building and deploying this project is as below:

Activate conda environment

```bash
source /Users/harishkumar/opt/anaconda3/bin/activate
```

Create env

```bash
conda create -n salespred python=3.7 -y
```

Activate env

```bash
conda activate salespred
```

Create Requirement File and install it

```bash
touch requirements.txt
```

```bash
pip install -r requirements.txt
```

Create Template for the project for how you want to build it

```bash
touch template.py
```

After Creating the required template of your project, run the template file to create directories and files

```bash
python template.py
```

Now Create a directory 'data_given' to keep our initial data and import Train and Test data to this directory

```bash
mkdir data_given
```

Let's push all the files to GIT remote repository and also start versioning our data using DVC

First, we have to initialize GIT and DVC

```bash
git init
```

```bash
dvc init
```

Add data files to DVC for tracking

```bash
dvc add data_given/Train.csv

dvc add data_given/Test.csv
```
Let's Add all the files to GIT Staging area to push it to remote repository

```bash
git add .
```

Commit the code

```bash
git commit -m "first commit"
```

Create a Repository in GitHub where we can push all these files

After that we can push all our files to the github remote repository

Since I made few changes to this README file, I'll add these to Staging and commit once again

```bash
git add . && git commit -m "updated Readme.md"
```

Now let's push the local files to remote repository

```bash
git remote add origin https://github.com/Harish2f/StoreSalesPrediction.git

git branch -M main

git push -u origin main
```
Now, Let's create a file to read our data to the app

```bash
touch src/get_data.py
```

Now after coding, running to check get_data.py

```bash
python src/get_data.py
```

Let's keep pushing files to remote repository for each individual file completed

```bash
git add . && git commit -m "updated get_data.py"

git push origin main
```
Create load data file to copy the file and dump it in raw data folder to keep a copy of raw unprocessed data

```bash
touch src/load_data.py
```
Now after coding, running to check load_data.py

```bash
python src/load_data.py
```
Now, Lets track the data change occuring from get_data and load_data files

Update dvc.yaml file with data tracing stage

Execute data tracing
```bash
dvc repro
```

Create file to treat missing values

```bash
touch src/missing_values.py
```
Now after coding, running to check missing_values.py

```bash
python src/missing_values.py
```

Create file to generate new features from existing features

```bash
touch src/new_features.py
```
Now after coding, running to check new_features.py

```bash
python src/new_features.py
```

Create feature encoding file

```bash
touch src/feature_encoding.py
```
Now after coding, running to check feature_encoding.py

```bash
python src/feature_encoding.py
```

Create split data for splitting train data for cross validation on our ML Model

```bash
touch src/split_data.py
```

Also, configure dvc.yaml  to track the split data
```bash
dvc repro
```

Push files to remote
```bash
git add . && git commit -m "stage 2 complete"

git push origin main
```

Time to create Train and Evaluate file to build our model

```bash
touch src/train_and_evaluate.py
```

Push files to remote
```bash
git add . && git commit -m "updated train&evaluate file"

git push origin main
```


Also, configure dvc.yaml  to track the train and evaluate data
```bash
dvc repro
```

Push files to remote
```bash
git add . && git commit -m "stage 3 complete"

git push origin main
```

Let's track and record changes in our params and metrics from ML Model to identify model derpreciation and possible retraining approach

```bash
mkdir report

touch report/params.json
touch report/scores.json
```

Now, Lets create Test files and Test environment

```bash
touch tox.ini
```

Create Test cases with test files

```bash

mkdir tests

touch tests/conftest.py tests/test_config.py

touch tests/__init__.py

```

Push files to remote
```bash
git add . && git commit -m "created test files"

git push origin main
```

Create Setup file to make the app as a package

```bash
touch setup.py
```

tox command -
```bash
tox
```

for rebuilding -

```bash
tox -r 
```

pytest command

```bash
pytest -v
```

Check if the package is installing

```bash
pip install -e .

pip freeze
```

Build the package

```bash
python setup.py sdist bdist_wheel
```
Create Prediction files to  predict and keep updated model 

```bash
mkdir -p prediction_service/model

mkdir webapp

touch app.py

touch prediction_service/__init__.py

touch prediction_service/prediction.py

```

Crete CSS and HTML files for app UI

```bash
mkdir -p webapp/static/css

mkdir -p webapp/static/script

touch webapp/static/css/main.css

touch webapp/static/script/index.js

mkdir webapp/templates

touch webapp/templates/index.html

touch webapp/templates/404.html

touch webapp/templates/base.html
```
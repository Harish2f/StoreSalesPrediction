This project is a complete end to end implementation of Store Sales Prediction using Machine Learning with DVC and MLFlow for Data Versioning and Model profiling to track the performance of the ML model.

The Steps involved in building and deploying this project is as below:

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

As a Good practice, let's push all the files to GIT and also start versioning our data using DVC

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
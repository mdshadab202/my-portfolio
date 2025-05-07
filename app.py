
from flask import Flask, render_template, request, redirect, flash
import csv
import os

app = Flask(__name__)

app.secret_key = 'your_secret_key'

# Dummy data
projects = [
    {'title': 'Insurance Prediction', 
     'description': 'I built a machine learning model using Scikit-learn to predict insurance premiums based on factors like age, BMI, and smoking habits. I included EDA, feature engineering,and hyperparameter tuning in my workflow..',
     'link': 'https://github.com/mdshadab202/insurance-premium-predictor',
     'Progress' : 100 },
    
     {'title': 'Titanic survival prediction ',
      'description': 'A machine learning model built on the Titanic dataset to predict survival outcomes using logistic regression, decision trees, and feature engineering techniques..',
      'link': 'https://www.kaggle.com/code/shadab91/fork-of-titanic',
      'Progress' : 100},
     
    
    {'title': 'resume macher',
     'description': 'A smart resume matcher that evaluates resumes against job descriptions using NLP',
     'link': 'https://github.com/mdshadab202/resume-matcher',
     'Progress' : 100
     },
    {'title': 'Jira AI Anomaly Detection',
     'description': 'LLM + clustering for doc irregularity detection.',
     'link': 'https://github.com/mdshadaba202/kb-model',
     'Progress' : 40
    }
    
    
]

blogs = [
    {'title': 'How I Built My Portfolio', 'content': 'Step-by-step breakdown...'},
    {'title': 'Using Flask with Conda', 'content': 'Managing environments for web dev...'}
]

# @app.route('/')
# def home():
#     return render_template('index.html', blogs=blogs, projects=projects)
from math import ceil

@app.route('/')
def home():
    page = request.args.get('page', 1, type=int)
    per_page = 2  # Number of blogs per page

    total = len(blogs)
    start = (page - 1) * per_page
    end = start + per_page
    paginated_blogs = blogs[start:end]

    total_pages = ceil(total / per_page)

    return render_template(
        'index.html',
        blogs=paginated_blogs,
        projects=projects,
        page=page,
        total_pages=total_pages
    )

# ✅ This route should be after app = Flask(...)
@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Save contact to CSV
    file_exists = os.path.isfile('contacts.csv')
    with open('contacts.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Name', 'Email', 'Message'])
        writer.writerow([name, email, message])

    flash('Thank you for contacting me!', 'success')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

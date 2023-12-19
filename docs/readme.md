# flask_e2e_project

For this final project, I am using external data from data.gov (https://catalog.data.gov/dataset/ischemic-stroke-30-day-mortality-and-30-day-readmission-rates-and-quality-ratings-for-ca-h-b8d33) which  is cleaned in a google colab environment, which is included in db/ folder. The data is then brought to a MySQL workbench database (finalproject), and used in the flask app to display the value information about the Ischemic Stroke 30-Day Mortality and 30-Day Readmission Rates and Quality Ratings for CA Hospitals. 

## Technologies used for final assignment:  
      - Github (Version Control)
      - Flask (Python; Frotend & Backend)
      - MySQL (Database)
      - SQLAlchemy (ORM)
      - .ENV (Environment Variables)
      - Tailwind (Frontend Styling)
      - Authorization (Google OAuth)
      - API Service (Flask Backend)
      - Logger and or Sentry.io (Debugging & Logging)
      - Docker (Containerization)
      - GCP (Deployment)

## How to run the app locally

1. Clone this repository
      git clone https://github.com/jjomathew98/flask_e2e_project
      cd flask_e2e_project

2. Install python virtual env (if not installed) and activate
      pip install virtualenv
      python -m venv env
      source env/bin/activate

3. Install python requirements
      pip install -r requirements.txt

4. Run the app locally
      cd app
      python app.py
        The app should be then started at `127.0.0.1:5000`

## Using docker
1. Pull the image from docker
      docker-compose build
      docker-compose up
   
3. Run the image container
      docker run -p 5000:5000 stroke

   Followed this link for deployment instructions: https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service 

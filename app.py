from flask import Flask, render_template, redirect, url_for, session, request
from flask_sqlalchemy import SQLAlchemy
from authlib.integrations.flask_client import OAuth
from authlib.integrations.base_client.errors import OAuthError
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Create Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['DEBUG'] = os.environ.get('DEBUG', False)

# Update your database connection details
db_ip = os.environ.get('DB_IP', '35.202.151.235')
db_port = os.environ.get('DB_PORT', '3306')
db_username = os.environ.get('DB_USERNAME', 'root')
db_password = os.environ.get('DB_PASSWORD', 'tholvi98jm')
db_name = os.environ.get('DB_NAME', 'finalproject')

# Set the database URI for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db_username}:{db_password}@{db_ip}:{db_port}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Google OAuth configuration with Authlib
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id=os.environ.get('GOOGLE_CLIENT_ID'),
    client_secret=os.environ.get('GOOGLE_CLIENT_SECRET'),
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params={'scope': 'email'},
    access_token_url='https://accounts.google.com/o/oauth2/token',
)

# Routes
@app.route('/')
def index():
    return render_template('base.html')

# /login route for Google OAuth
@app.route('/login')
def login():
    # Use url_for within the context of a request
    redirect_uri = url_for('authorized', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route('/logout')
def logout():
    session.pop('google_token', None)
    session.pop('google_user_info', None)
    return redirect(url_for('index'))

@app.route('/login/authorized')
def authorized():
    try:
        token = google.authorize_access_token()
        user_info = google.parse_id_token(token)
        session['google_token'] = token
        session['google_user_info'] = user_info

        return redirect(url_for('index'))
    except OAuthError as e:
        return f'Authentication failed: {e.description}'
    except Exception as e:
        return f'An unexpected error occurred: {e}'

@app.route('/data')
def data():
    try:
        query = 'SELECT * FROM finalproject.california_ischemic_stroke_data'
        result = db.session.execute(query)
        data = [dict(row) for row in result]
        return render_template('data.html', data=data)
    except Exception as e:
        return f"Error fetching data: {e}"


@app.route('/api/data')
def api_data():
    try:
        # Query the database to get the data if needed for API routes
        # Example: data_frame = pd.read_sql('SELECT * FROM your_table_name', db.engine)
        input_county = request.args.get('input_county')
        # Process the data if needed
        # Example: data = data_frame[data_frame['County'] == input_county].head(10)
        return "API endpoint without data retrieval"
    except Exception as e:
        return f'Error: {e}'

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000
    )

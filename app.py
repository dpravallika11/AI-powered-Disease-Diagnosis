from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
from mysql.connector import Error
import jwt
from datetime import datetime, timedelta
from functools import wraps
import pickle
import numpy as np
import pandas as pd
from disease_info import get_disease_info
import re
import os
import json

app = Flask(__name__)
CORS(app)

# !! SECRET KEY FOR JWT - MUST BE SET !!
app.config['SECRET_KEY'] = 'pravallika@1110'  # <-- CHANGE THIS TO A STRONG SECRET

# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'port': '3306',
    'database': 'disease_diagnosis',
    'user': 'root',
    'password': '@1110'
}

# Load ML model
try:
    with open('disease_model.pkl', 'rb') as f:
        model = pickle.load(f)
    print("Model loaded successfully")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

SYMPTOMS = ["itching", "skin_rash", "nodal_skin_eruptions", "continuous_sneezing", "shivering", "chills",
    "joint_pain", "stomach_pain", "acidity", "ulcers_on_tongue", "muscle_wasting", "vomiting",
    "burning_micturition", "spotting_urination", "fatigue", "weight_gain", "anxiety", 
    "cold_hands_and_feets", "mood_swings", "weight_loss", "restlessness", "lethargy",
    "patches_in_throat", "irregular_sugar_level", "cough", "high_fever", "sunken_eyes", 
    "breathlessness", "sweating", "dehydration", "indigestion", "headache", "yellowish_skin",
    "dark_urine", "nausea", "loss_of_appetite", "pain_behind_the_eyes", "back_pain",
    "constipation", "abdominal_pain", "diarrhoea", "mild_fever", "yellow_urine", 
    "yellowing_of_eyes", "acute_liver_failure", "fluid_overload", "swelling_of_stomach",
    "swelled_lymph_nodes", "malaise", "blurred_and_distorted_vision", "phlegm", 
    "throat_irritation", "redness_of_eyes", "sinus_pressure", "runny_nose", "congestion",
    "chest_pain", "weakness_in_limbs", "fast_heart_rate", "pain_during_bowel_movements",
    "pain_in_anal_region", "bloody_stool", "irritation_in_anus", "neck_pain", "dizziness",
    "cramps", "bruising", "obesity", "swollen_legs", "swollen_blood_vessels",
    "puffy_face_and_eyes", "enlarged_thyroid", "brittle_nails", "swollen_extremeties",
    "excessive_hunger", "extra_marital_contacts", "drying_and_tingling_lips",
    "slurred_speech", "knee_pain", "hip_joint_pain", "muscle_weakness", "stiff_neck",
    "swelling_joints", "movement_stiffness", "spinning_movements", "loss_of_balance",
    "unsteadiness", "weakness_of_one_body_side", "loss_of_smell", "bladder_discomfort",
    "foul_smell_of_urine", "continuous_feel_of_urine", "passage_of_gases", 
    "internal_itching", "toxic_look_(typhos)", "depression", "irritability", 
    "muscle_pain", "altered_sensorium", "red_spots_over_body", "belly_pain", 
    "abnormal_menstruation", "dischromic_patches", "watering_from_eyes",
    "increased_appetite", "polyuria", "family_history", "mucoid_sputum", "rusty_sputum",
    "lack_of_concentration", "visual_disturbances", "receiving_blood_transfusion",
    "receiving_unsterile_injections", "coma", "stomach_bleeding", "distention_of_abdomen",
    "history_of_alcohol_consumption", "fluid_overload", "blood_in_sputum",
    "prominent_veins_on_calf", "palpitations", "painful_walking", "pus_filled_pimples",
    "blackheads", "scurring", "skin_peeling", "silver_like_dusting", "small_dents_in_nails",
    "inflammatory_nails", "blister", "red_sore_around_nose", "yellow_crust_ooze"
]

def init_database():
    conn = None
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS users ("
            "id INT AUTO_INCREMENT PRIMARY KEY, "
            "name VARCHAR(255) NOT NULL, "
            "email VARCHAR(255) UNIQUE NOT NULL, "
            "password_hash VARCHAR(255) NOT NULL, "
            "created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"
        )
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS diagnosis_history ("
            "id INT AUTO_INCREMENT PRIMARY KEY, "
            "user_id INT, "
            "disease VARCHAR(255) NOT NULL, "
            "symptoms TEXT, "  # <-- Store as TEXT for compatibility
            "dob DATE, "
            "weight FLOAT, "
            "height FLOAT, "
            "created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "
            "FOREIGN KEY (user_id) REFERENCES users(id))"
        )
        conn.commit()
        print("Database initialized successfully")
    except Error as e:
        print(f"Database initialization error: {e}")
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

def get_db_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        print(f"Database connection error: {e}")
        return None

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'success': False, 'message': 'Token is missing'}), 401
        try:
            token = token.split(' ')[1]
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = data['user_id']
        except jwt.ExpiredSignatureError:
            return jsonify({'success': False, 'message': 'Token expired'}), 401
        except Exception as e:
            print(f"JWT decode error: {e}")
            return jsonify({'success': False, 'message': 'Token is invalid'}), 401
        return f(current_user, *args, **kwargs)
    return decorated

def calculate_age(dob):
    today = datetime.now().date()
    dob = datetime.strptime(dob, '%Y-%m-%d').date()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age

def get_age_category(age):
    if age < 18:
        return 'Children'
    elif age < 60:
        return 'Adults'
    else:
        return 'Seniors'

def generate_wikipedia_link(disease_name):
    clean_name = re.sub(r'[^\w\s]', '', disease_name)
    clean_name = clean_name.replace(' ', '_')
    return f"https://en.wikipedia.org/wiki/{clean_name}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/register', methods=['POST'])
def register():
    conn = None
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        if not all([name, email, password]):
            return jsonify({'success': False, 'message': 'All fields are required'})
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            return jsonify({'success': False, 'message': 'Invalid email format'})
        password_hash = generate_password_hash(password)
        conn = get_db_connection()
        if not conn:
            return jsonify({'success': False, 'message': 'Database connection failed'})
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO users (name, email, password_hash) VALUES (%s, %s, %s)",
                (name, email, password_hash)
            )
            conn.commit()
            return jsonify({'success': True, 'message': 'Registration successful'})
        except mysql.connector.IntegrityError:
            return jsonify({'success': False, 'message': 'Email already exists'})
    except Exception as e:
        print(f"Registration error: {e}")
        return jsonify({'success': False, 'message': 'Registration failed'})
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

@app.route('/api/login', methods=['POST'])
def login():
    conn = None
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        if not all([email, password]):
            return jsonify({'success': False, 'message': 'Email and password are required'})
        conn = get_db_connection()
        if not conn:
            return jsonify({'success': False, 'message': 'Database connection failed'})
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        if user and check_password_hash(user['password_hash'], password):
            token = jwt.encode({
                'user_id': user['id'],
                'exp': datetime.utcnow() + timedelta(days=7)
            }, app.config['SECRET_KEY'], algorithm='HS256')
            # Ensure token is a string for JSON serialization
            if isinstance(token, bytes):
                token = token.decode('utf-8')
            return jsonify({
                'success': True,
                'token': token,
                'user': {
                    'id': user['id'],
                    'name': user['name'],
                    'email': user['email']
                }
            })
        else:
            return jsonify({'success': False, 'message': 'Invalid credentials'})
    except Exception as e:
        print(f"Login error: {e}")
        return jsonify({'success': False, 'message': 'Login failed'})
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

@app.route('/api/verify_token', methods=['POST'])
def verify_token():
    conn = None
    try:
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'success': False, 'message': 'Token missing'})
        token = token.split(' ')[1]
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, name, email FROM users WHERE id = %s", (data['user_id'],))
        user = cursor.fetchone()
        if user:
            return jsonify({'success': True, 'user': user})
        else:
            return jsonify({'success': False, 'message': 'User not found'})
    except jwt.ExpiredSignatureError:
        return jsonify({'success': False, 'message': 'Token expired'})
    except jwt.InvalidTokenError:
        return jsonify({'success': False, 'message': 'Invalid token'})
    except Exception as e:
        print(f"Token verification error: {e}")
        return jsonify({'success': False, 'message': 'Token verification failed'})
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

@app.route('/api/diagnose', methods=['POST'])
@token_required
def diagnose(current_user):
    conn = None
    try:
        if not model:
            return jsonify({'success': False, 'message': 'ML model not available'})
        data = request.get_json()
        dob = data.get('dob')
        weight = data.get('weight')
        height = data.get('height')
        symptoms = data.get('symptoms', [])
        if not all([dob, weight, height]) or len(symptoms)==0:
            return jsonify({'success': False, 'message': 'All fields are required'})
        age = calculate_age(dob)
        age_category = get_age_category(age)
        symptoms_vector = [1 if symptom in symptoms else 0 for symptom in SYMPTOMS]
        prediction = model.predict([symptoms_vector])[0]
        disease_info = get_disease_info(prediction)
        # Use correct age_category key for exercise
        exercise = None
        if disease_info:
            # If disease_info['exercise'] is a dict, fetch by age_category (Children/Adults/Seniors)
            if isinstance(disease_info['exercise'], dict):
                exercise = disease_info['exercise'].get(age_category, list(disease_info['exercise'].values())[0])
            else:
                exercise = disease_info['exercise']
            result = {
                'disease': prediction,
                'specialist': disease_info['specialist'],
                'precautions': disease_info['precautions'],
                'diet': disease_info['diet'],
                'exercise': [exercise] if isinstance(exercise, str) else exercise,
                'wikipedia_link': generate_wikipedia_link(prediction)
            }
        else:
            result = {
                'disease': 'Not able to diagnose',
                'specialist': 'General Physician',
                'precautions': ['Consult a doctor for proper diagnosis'],
                'diet': ['Maintain a balanced diet'],
                'exercise': ['Light exercise as tolerated'],
                'wikipedia_link': 'https://en.wikipedia.org/wiki/Disease'
            }
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO diagnosis_history (user_id, disease, symptoms, dob, weight, height)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (current_user, result['disease'], json.dumps(symptoms), dob, weight, height))
        conn.commit()
        return jsonify({'success': True, 'result': result})
    except Exception as e:
        print(f"Diagnosis error: {e}")
        return jsonify({'success': False, 'message': 'Diagnosis failed'})
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

@app.route('/api/diseases', methods=['GET'])
def get_diseases():
    try:
        from disease_info import disease_data
        diseases = []
        for disease_name, info in disease_data.items():
            diseases.append({
                'name': disease_name,
                'specialist': info['specialist'],
                'precautions': info['precautions'],
                'diet': info['diet'],
                'exercise': info['exercise'],
                'symptoms': []
            })
        return jsonify({'success': True, 'diseases': diseases})
    except Exception as e:
        print(f"Disease library error: {e}")
        return jsonify({'success': False, 'message': 'Failed to load disease library'})

@app.route('/api/profile', methods=['GET'])
@token_required
def get_profile(current_user):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, name, email, created_at FROM users WHERE id = %s", (current_user,))
        profile = cursor.fetchone()
        cursor.execute("""
            SELECT disease, symptoms, created_at 
            FROM diagnosis_history 
            WHERE user_id = %s 
            ORDER BY created_at DESC
        """, (current_user,))
        history = cursor.fetchall()
        for item in history:
            if isinstance(item['symptoms'], str):
                import ast
                try:
                    item['symptoms'] = ast.literal_eval(item['symptoms'])
                except:
                    item['symptoms'] = []
        return jsonify({'success': True, 'profile': profile, 'history': history})
    except Exception as e:
        print(f"Profile error: {e}")
        return jsonify({'success': False, 'message': 'Failed to load profile'})
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

@app.errorhandler(404)
def not_found(error):
    return jsonify({'success': False, 'message': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'success': False, 'message': 'Internal server error'}), 500

if __name__ == '__main__':
    init_database()
    app.run(debug=True, host='0.0.0.0', port=5000)
age_groups = {
    "Children": {"range": (0, 12), "description": "0–12 years"},
    "Adolescents": {"range": (13, 18), "description": "13–18 years"},
    "Adults": {"range": (19, 59), "description": "19–59 years"},
    "Seniors": {"range": (60, 200), "description": "60+ years"}
}

disease_data = {
    "Fungal Infection": {
        "specialist": "Dermatologist",
        "precautions": [
            "Maintain hygiene",
            "Avoid damp clothes",
            "Avoid sharing personal items"
        ],
        "diet": [
            "Include probiotics (yogurt)",
            "Garlic",
            "Leafy greens",
            "Avoid sugar and refined carbs"
        ],
        "exercise": {
            "Children": "Light stretching",
            "Adolescents": "Yoga",
            "Adults": "Walking",
            "Seniors": "Joint-friendly stretches"
        }
    },
    "Allergy": {
        "specialist": "Allergist",
        "precautions": [
            "Avoid allergens",
            "Keep epinephrine auto-injector if prescribed"
        ],
        "diet": [
            "Balanced diet rich in Vitamin C (citrus fruits, bell peppers)",
            "Avoid known allergens"
        ],
        "exercise": {
            "Children": "Playful activities",
            "Adolescents": "Swimming",
            "Adults": "Light jogging",
            "Seniors": "Tai Chi"
        }
    },
    "GERD": {
        "specialist": "Gastroenterologist",
        "precautions": [
            "Avoid lying down after meals",
            "Avoid spicy and fatty foods"
        ],
        "diet": [
            "High-fiber foods (whole grains, vegetables)",
            "Avoid citrus, caffeine, and carbonated drinks"
        ],
        "exercise": {
            "Children": "Light stretches",
            "Adolescents": "Moderate walking",
            "Adults": "Yoga",
            "Seniors": "Gentle walking"
        }
    },
    "Chronic Cholestasis": {
        "specialist": "Hepatologist",
        "precautions": [
            "Avoid alcohol",
            "Maintain a healthy weight"
        ],
        "diet": [
            "Low-fat diet",
            "Increase intake of fruits, vegetables, and lean proteins",
            "Avoid fried and greasy foods"
        ],
        "exercise": {
            "Children": "Light activities",
            "Adolescents": "Walking",
            "Adults": "Yoga",
            "Seniors": "Gentle stretching"
        }
    },
    "Drug Reaction": {
        "specialist": "Pharmacologist",
        "precautions": [
            "Avoid self-medication",
            "Inform doctor of allergies to medicines"
        ],
        "diet": [
            "Hydrate well",
            "Include anti-inflammatory foods (turmeric, ginger, leafy greens)"
        ],
        "exercise": {
            "Children": "Rest",
            "Adolescents": "Relaxation exercises",
            "Adults": "Light walks",
            "Seniors": "Gentle yoga"
        }
    },
    "Peptic Ulcer Disease": {
        "specialist": "Gastroenterologist",
        "precautions": [
            "Avoid NSAIDs",
            "Reduce stress",
            "Avoid spicy foods"
        ],
        "diet": [
            "High-fiber foods",
            "Non-acidic fruits",
            "Lean proteins",
            "Avoid alcohol, caffeine, and spicy foods"
        ],
        "exercise": {
            "Children": "Light walking",
            "Adolescents": "Yoga",
            "Adults": "Aerobics",
            "Seniors": "Gentle yoga"
        }
    },
    "AIDS": {
        "specialist": "Infectious Disease Specialist",
        "precautions": [
            "Practice safe sex",
            "Avoid shared needles",
            "Adhere to medications"
        ],
        "diet": [
            "Nutrient-rich diet with fruits, vegetables, lean proteins, whole grains",
            "Avoid raw or undercooked foods"
        ],
        "exercise": {
            "Children": "Light play",
            "Adolescents": "Walking",
            "Adults": "Yoga",
            "Seniors": "Gentle stretching"
        }
    },
    "Diabetes": {
        "specialist": "Endocrinologist",
        "precautions": [
            "Monitor blood sugar",
            "Avoid skipping meals",
            "Stay hydrated"
        ],
        "diet": [
            "Low-glycemic index foods",
            "Whole grains",
            "Lean proteins",
            "Non-starchy vegetables",
            "Avoid sugary items"
        ],
        "exercise": {
            "Children": "Active play",
            "Adolescents": "Cycling",
            "Adults": "Brisk walking",
            "Seniors": "Low-impact aerobics"
        }
    },
    "Gastroenteritis": {
        "specialist": "Gastroenterologist",
        "precautions": [
            "Stay hydrated",
            "Avoid contaminated food or water"
        ],
        "diet": [
            "Hydrating foods (soups, clear fluids)",
            "Bananas",
            "Rice",
            "Applesauce",
            "Toast (BRAT diet)",
            "Avoid dairy and fried foods"
        ],
        "exercise": {
            "Children": "Rest",
            "Adolescents": "Walking post-recovery",
            "Adults": "Light exercises post-recovery",
            "Seniors": "Breathing exercises"
        }
    },
    "Bronchial Asthma": {
        "specialist": "Pulmonologist",
        "precautions": [
            "Avoid allergens",
            "Use inhalers as prescribed"
        ],
        "diet": [
            "Anti-inflammatory foods (fish, nuts, turmeric)",
            "Avoid dairy and processed foods"
        ],
        "exercise": {
            "Children": "Playful activities",
            "Adolescents": "Swimming",
            "Adults": "Breathing exercises",
            "Seniors": "Gentle yoga"
        }
    },
    "Hypertension": {
        "specialist": "Cardiologist",
        "precautions": [
            "Limit salt intake",
            "Manage stress"
        ],
        "diet": [
            "DASH diet: fruits, vegetables, whole grains, lean proteins",
            "Avoid processed and salty foods"
        ],
        "exercise": {
            "Children": "Fun outdoor activities",
            "Adolescents": "Team sports",
            "Adults": "Brisk walking",
            "Seniors": "Chair exercises"
        }
    },
    "Migraine": {
        "specialist": "Neurologist",
        "precautions": [
            "Stay hydrated",
            "Avoid triggers (e.g., strong lights, caffeine)"
        ],
        "diet": [
            "Magnesium-rich foods (nuts, seeds)",
            "Leafy greens",
            "Fish",
            "Avoid alcohol and processed foods"
        ],
        "exercise": {
            "Children": "Relaxation exercises",
            "Adolescents": "Yoga",
            "Adults": "Aerobics",
            "Seniors": "Gentle yoga"
        }
    },
    "Cervical Spondylosis": {
        "specialist": "Orthopedist",
        "precautions": [
            "Maintain correct posture",
            "Avoid heavy lifting"
        ],
        "diet": [
            "Calcium-rich foods",
            "Vitamin D (dairy, fish, eggs)",
            "Avoid excess caffeine"
        ],
        "exercise": {
            "Children": "Posture exercises",
            "Adolescents": "Neck stretches",
            "Adults": "Strengthening exercises",
            "Seniors": "Gentle yoga"
        }
    },
    "Paralysis (Brain Hemorrhage)": {
        "specialist": "Neurologist",
        "precautions": [
            "Regular physiotherapy",
            "Adhere to medications"
        ],
        "diet": [
            "Soft and nutrient-dense foods (smoothies, soups)",
            "High in protein and fiber"
        ],
        "exercise": {
            "Children": "Physiotherapy",
            "Adolescents": "Guided physiotherapy",
            "Adults": "Guided therapy",
            "Seniors": "Gentle assisted exercises"
        }
    },
    "Jaundice": {
        "specialist": "Hepatologist",
        "precautions": [
            "Avoid alcohol",
            "Get adequate rest"
        ],
        "diet": [
            "High-carb diet (rice, bananas, boiled potatoes)",
            "Avoid fatty and oily foods"
        ],
        "exercise": {
            "Children": "Rest",
            "Adolescents": "Gentle walking",
            "Adults": "Gradual walking",
            "Seniors": "Light stretches"
        }
    },
    "Malaria": {
        "specialist": "Infectious Disease Specialist",
        "precautions": [
            "Use mosquito nets",
            "Avoid mosquito-prone areas"
        ],
        "diet": [
            "Hydrating foods (coconut water, soups)",
            "Iron-rich foods for anemia",
            "Avoid heavy or oily meals"
        ],
        "exercise": {
            "Children": "Rest during the acute stage",
            "Adolescents": "Light walking after recovery",
            "Adults": "Gradual aerobic exercises",
            "Seniors": "Gentle walking"
        }
    },
    "Chicken Pox": {
        "specialist": "Dermatologist",
        "precautions": [
            "Avoid scratching",
            "Maintain hygiene"
        ],
        "diet": [
            "Hydrating and soothing foods (soups, boiled vegetables)",
            "Avoid oily and spicy foods"
        ],
        "exercise": {
            "Children": "Rest",
            "Adolescents": "Light activities after recovery",
            "Adults": "Gradual walking",
            "Seniors": "Gentle exercise"
        }
    },
    "Dengue": {
        "specialist": "Infectious Disease Specialist",
        "precautions": [
            "Use mosquito repellents",
            "Stay hydrated"
        ],
        "diet": [
            "Hydration-rich foods (coconut water, papaya)",
            "Vitamin C-rich fruits",
            "Avoid oily and spicy foods"
        ],
        "exercise": {
            "Children": "Rest during the acute stage",
            "Adolescents": "Light walking after recovery",
            "Adults": "Gradual walking",
            "Seniors": "Gentle yoga"
        }
    },
    "Typhoid": {
        "specialist": "Infectious Disease Specialist",
        "precautions": [
            "Avoid contaminated food and water",
            "Complete medication course"
        ],
        "diet": [
            "High-calorie, soft foods (rice, bananas, boiled eggs)",
            "Avoid raw and spicy foods"
        ],
        "exercise": {
            "Children": "Rest",
            "Adolescents": "Light activities after recovery",
            "Adults": "Gradual walking",
            "Seniors": "Gentle stretches"
        }
    },
    "Hepatitis A": {
        "specialist": "Hepatologist",
        "precautions": [
            "Avoid alcohol",
            "Get vaccinated"
        ],
        "diet": [
            "High-carb diet (rice, bread)",
            "Fresh fruits and vegetables",
            "Avoid fatty and fried foods"
        ],
        "exercise": {
            "Children": "Rest",
            "Adolescents": "Light walking",
            "Adults": "Gradual walking",
            "Seniors": "Gentle yoga"
        }
    },
    "Hepatitis B": {
        "specialist": "Hepatologist",
        "precautions": [
            "Avoid alcohol",
            "Get vaccinated"
        ],
        "diet": [
            "Balanced diet rich in vitamins and proteins",
            "Avoid processed foods"
        ],
        "exercise": {
            "Children": "Rest",
            "Adolescents": "Light walking",
            "Adults": "Gradual aerobic exercises",
            "Seniors": "Gentle stretches"
        }
    },
    "Hepatitis C": {
        "specialist": "Hepatologist",
        "precautions": [
            "Avoid alcohol",
            "Regular liver tests"
        ],
        "diet": [
            "Nutrient-rich diet (whole grains, lean proteins)",
            "Avoid fried and processed foods"
        ],
        "exercise": {
            "Children": "Rest",
            "Adolescents": "Light walking",
            "Adults": "Gradual aerobic exercises",
            "Seniors": "Gentle walking"
        }
    },
    "Hepatitis D": {
        "specialist": "Hepatologist",
        "precautions": [
            "Avoid alcohol",
            "Adhere to medications"
        ],
        "diet": [
            "High-protein diet (eggs, lean meat)",
            "Fresh fruits and vegetables",
            "Avoid junk food"
        ],
        "exercise": {
            "Children": "Rest",
            "Adolescents": "Light walking",
            "Adults": "Gradual exercises",
            "Seniors": "Gentle stretches"
        }
    },
    "Hepatitis E": {
        "specialist": "Hepatologist",
        "precautions": [
            "Avoid contaminated water",
            "Maintain hygiene"
        ],
        "diet": [
            "Hydrating foods (soups, fruits)",
            "Vitamin E-rich foods",
            "Avoid oily and fried foods"
        ],
        "exercise": {
            "Children": "Rest",
            "Adolescents": "Light walking",
            "Adults": "Gradual walking",
            "Seniors": "Gentle yoga"
        }
    },
    "Alcoholic Hepatitis": {
        "specialist": "Hepatologist",
        "precautions": [
            "Stop alcohol consumption",
            "Maintain healthy weight"
        ],
        "diet": [
            "Vitamin-rich foods (fruits, vegetables)",
            "Lean proteins",
            "Avoid fatty and processed foods"
        ],
        "exercise": {
            "Children": "Not applicable",
            "Adolescents": "Not applicable",
            "Adults": "Walking after recovery",
            "Seniors": "Gentle walking"
        }
    },
    "Tuberculosis": {
        "specialist": "Pulmonologist",
        "precautions": [
            "Complete the medication course",
            "Avoid close contact with others during active infection"
        ],
        "diet": [
            "Protein-rich foods (eggs, chicken)",
            "Whole grains",
            "Vegetables",
            "Avoid alcohol and smoking"
        ],
        "exercise": {
            "Children": "Rest during acute stage",
            "Adolescents": "Gradual walking post-recovery",
            "Adults": "Aerobic exercises",
            "Seniors": "Breathing exercises"
        }
    },
    "Common Cold": {
        "specialist": "General Physician",
        "precautions": [
            "Stay hydrated",
            "Avoid cold exposure"
        ],
        "diet": [
            "Warm fluids (soups, herbal teas)",
            "Vitamin C-rich foods",
            "Avoid cold and greasy foods"
        ],
        "exercise": {
            "Children": "Rest",
            "Adolescents": "Light activities",
            "Adults": "Gentle yoga",
            "Seniors": "Breathing exercises"
        }
    },
    "Pneumonia": {
        "specialist": "Pulmonologist",
        "precautions": [
            "Avoid cold exposure",
            "Maintain hygiene"
        ],
        "diet": [
            "Warm soups",
            "Hydrating foods",
            "Lean proteins",
            "Avoid cold or greasy foods"
        ],
        "exercise": {
            "Children": "Rest during acute stage",
            "Adolescents": "Light walking after recovery",
            "Adults": "Gradual aerobic exercises",
            "Seniors": "Breathing exercises"
        }
    },
    "Dimorphic Hemorrhoids (Piles)": {
        "specialist": "Proctologist",
        "precautions": [
            "Avoid constipation",
            "Maintain hygiene"
        ],
        "diet": [
            "High-fiber foods (whole grains, fruits, vegetables)",
            "Avoid spicy and fatty foods"
        ],
        "exercise": {
            "Children": "Not applicable",
            "Adolescents": "Light yoga",
            "Adults": "Walking",
            "Seniors": "Gentle pelvic exercises"
        }
    },
    "Heart Attack": {
        "specialist": "Cardiologist",
        "precautions": [
            "Avoid stress",
            "Adhere to medications",
            "Monitor cholesterol levels"
        ],
        "diet": [
            "Heart-healthy diet: fruits, vegetables, whole grains, lean proteins",
            "Avoid fried and high-fat foods"
        ],
        "exercise": {
            "Children": "Not applicable",
            "Adolescents": "Not applicable",
            "Adults": "Post-recovery supervised exercises",
            "Seniors": "Gentle stretches under supervision"
        }
    },
    "Varicose Veins": {
        "specialist": "Vascular Surgeon",
        "precautions": [
            "Avoid prolonged standing",
            "Elevate legs when resting"
        ],
        "diet": [
            "High-fiber foods",
            "Hydration",
            "Avoid salty foods"
        ],
        "exercise": {
            "Children": "Fun outdoor activities",
            "Adolescents": "Swimming",
            "Adults": "Walking",
            "Seniors": "Gentle leg exercises"
        }
    },
    "Hypothyroidism": {
        "specialist": "Endocrinologist",
        "precautions": [
            "Take medications regularly",
            "Avoid stress"
        ],
        "diet": [
            "Iodine-rich foods (fish, eggs)",
            "Selenium-rich foods (nuts)",
            "Avoid soy and processed foods"
        ],
        "exercise": {
            "Children": "Fun activities",
            "Adolescents": "Yoga",
            "Adults": "Brisk walking",
            "Seniors": "Gentle stretching"
        }
    },
    "Hypoglycemia": {
        "specialist": "Endocrinologist",
        "precautions": [
            "Eat small meals frequently",
            "Monitor blood sugar levels"
        ],
        "diet": [
            "Easily digestible carbs (bananas, crackers)",
            "Lean proteins",
            "Avoid high-sugar processed foods"
        ],
        "exercise": {
            "Children": "Playful activities",
            "Adolescents": "Cycling",
            "Adults": "Walking",
            "Seniors": "Gentle yoga"
        }
    },
    "Osteoarthritis": {
        "specialist": "Rheumatologist",
        "precautions": [
            "Avoid prolonged standing",
            "Manage weight"
        ],
        "diet": [
            "Anti-inflammatory foods (fatty fish, turmeric, leafy greens)",
            "Avoid sugar and processed foods"
        ],
        "exercise": {
            "Children": "Gentle stretches",
            "Adolescents": "Swimming",
            "Adults": "Low-impact exercises",
            "Seniors": "Chair yoga"
        }
    },
    "Arthritis": {
        "specialist": "Rheumatologist",
        "precautions": [
            "Manage weight",
            "Avoid overexertion"
        ],
        "diet": [
            "Anti-inflammatory foods (berries, nuts, fish)",
            "Avoid processed foods"
        ],
        "exercise": {
            "Children": "Fun stretching",
            "Adolescents": "Swimming",
            "Adults": "Yoga",
            "Seniors": "Gentle chair yoga"
        }
    },
    "(Vertigo) Paroxysmal Positional Vertigo": {
        "specialist": "Neurologist",
        "precautions": [
            "Avoid sudden head movements",
            "Practice balance exercises"
        ],
        "diet": [
            "Hydration",
            "Vitamin D-rich foods (dairy, fish)",
            "Avoid caffeine and alcohol"
        ],
        "exercise": {
            "Children": "Balance exercises",
            "Adolescents": "Gentle yoga",
            "Adults": "Balance training",
            "Seniors": "Assisted balance exercises"
        }
    },
    "Acne": {
        "specialist": "Dermatologist",
        "precautions": [
            "Maintain skin hygiene",
            "Avoid touching the face frequently"
        ],
        "diet": [
            "Low-glycemic foods",
            "Include zinc-rich foods (pumpkin seeds, lentils)",
            "Avoid dairy and sugary items"
        ],
        "exercise": {
            "Children": "Light outdoor play",
            "Adolescents": "Yoga",
            "Adults": "Aerobics",
            "Seniors": "Gentle yoga"
        }
    },
    "Urinary Tract Infection": {
        "specialist": "Urologist",
        "precautions": [
            "Stay hydrated",
            "Avoid holding urine for long periods"
        ],
        "diet": [
            "Cranberry juice",
            "Water-rich fruits (watermelon)",
            "Probiotics",
            "Avoid caffeine and spicy foods"
        ],
        "exercise": {
            "Children": "Hydration walks",
            "Adolescents": "Light yoga",
            "Adults": "Walking",
            "Seniors": "Pelvic floor exercises"
        }
    },
    "Psoriasis": {
        "specialist": "Dermatologist",
        "precautions": [
            "Keep skin moisturized",
            "Avoid triggers like stress or smoking"
        ],
        "diet": [
            "Anti-inflammatory diet: nuts, seeds, fatty fish, and leafy greens",
            "Avoid alcohol and processed foods"
        ],
        "exercise": {
            "Children": "Gentle yoga",
            "Adolescents": "Swimming",
            "Adults": "Moderate yoga",
            "Seniors": "Chair yoga"
        }
    },
    "Impetigo": {
        "specialist": "Dermatologist",
        "precautions": [
            "Maintain hygiene",
            "Avoid scratching or touching lesions"
        ],
        "diet": [
            "Balanced diet with Vitamin C-rich foods (oranges, strawberries)",
            "Avoid greasy foods"
        ],
        "exercise": {
            "Children": "Rest",
            "Adolescents": "Relaxation exercises",
            "Adults": "Light walking",
            "Seniors": "Gentle yoga"
        }
    },
    "Covid 19": {
        "specialist": "Pulmonologist",
        "precautions": [
            "Wear a mask in crowded areas",
            "Regular hand washing",
            "Maintain physical distance"
            ],
        "diet": [
            "Immune-boosting foods (citrus fruits, garlic, ginger)",
            "Hydrating fluids",
            "Avoid processed foods"
            ],
        "exercise": {
            "Children": "Light stretching indoors",
            "Adolescents": "Mild aerobic exercises at home",
            "Adults": "Walking or light yoga",
            "Seniors": "Breathing exercises and gentle yoga"
        }
    },
    "Chronic Obstructive Pulmonary Disease (COPD)": {
        "specialist": "Pulmonologist",
        "precautions": [
            "Avoid smoking and air pollutants",
            "Use inhalers as prescribed",
            "Monitor breathing difficulty"
        ],
        "diet": [
            "High-fiber and antioxidant-rich foods",
            "Small frequent meals",
            "Avoid gas-producing foods"
        ],
        "exercise": {
            "Children": "N/A",
            "Adolescents": "N/A",
            "Adults": "Pulmonary rehab and walking",
            "Seniors": "Breathing exercises and light yoga"
        }
    },
    "Sinusitis": {
        "specialist": "ENT Specialist (Otolaryngologist)",
        "precautions": [
            "Use steam inhalation",
            "Avoid allergens and pollutants",
            "Stay hydrated"
        ],
        "diet": [
            "Warm fluids and soups",
            "Spicy foods to clear sinuses",
            "Avoid dairy and cold drinks"
        ],
        "exercise": {
            "Children": "Play indoors",
            "Adolescents": "Walking or light jogging",
            "Adults": "Breathing exercises",
            "Seniors": "Gentle stretching"
        }
    },
    "Tonsillitis": {
        "specialist": "ENT Specialist (Otolaryngologist)",
        "precautions": [
            "Avoid cold drinks",
            "Maintain oral hygiene",
            "Isolate if bacterial"
        ],
        "diet": [
            "Soft, warm foods (soups, porridge)",
            "Avoid spicy and acidic foods",
            "Stay hydrated"
        ],
        "exercise": {
            "Children": "Rest",
            "Adolescents": "Mild activity indoors",
            "Adults": "Rest and hydration",
            "Seniors": "Gentle walks after recovery"
        }
    },
    "Eczema (Atopic Dermatitis)": {
        "specialist": "Dermatologist",
        "precautions": [
            "Moisturize frequently",
            "Avoid harsh soaps and triggers",
            "Keep nails short to prevent scratching"
        ],
        "diet": [
            "Anti-inflammatory foods (turmeric, berries)",
            "Omega-3-rich foods",
            "Avoid dairy or gluten if allergic"
        ],
        "exercise": {
            "Children": "Indoor play avoiding sweat triggers",
            "Adolescents": "Short walks",
            "Adults": "Low-sweat exercises",
            "Seniors": "Stretching and mild walking"
        }
    },
    "Vitiligo": {
        "specialist": "Dermatologist",
        "precautions": [
            "Avoid sun exposure without sunscreen",
            "Use prescribed topical treatments",
            "Manage emotional stress"
        ],
        "diet": [
            "Copper-rich foods (nuts, seeds)",
            "Fruits and vegetables with antioxidants",
            "Avoid processed and junk foods"
        ],
        "exercise": {
            "Children": "Outdoor play with protection",
            "Adolescents": "Any preferred activity",
            "Adults": "Cardio or yoga",
            "Seniors": "Walking and flexibility exercises"
        }
    },
    "Scabies": {
        "specialist": "Dermatologist",
        "precautions": [
            "Wash clothes and bedding in hot water",
            "Avoid skin contact with infected persons",
            "Use prescribed creams"
        ],
        "diet": [
            "Immune-boosting foods (citrus, garlic)",
            "Stay hydrated",
            "Avoid inflammatory foods"
        ],
        "exercise": {
            "Children": "Rest until treated",
            "Adolescents": "Light activity post-treatment",
            "Adults": "Normal routine post-recovery",
            "Seniors": "Minimal exertion until itching subsides"
        }
    },
    "Coronary Artery Disease (CAD)": {
        "specialist": "Cardiologist",
        "precautions": [
            "Manage blood pressure and cholesterol",
            "Avoid smoking",
            "Limit stress"
        ],
        "diet": [
            "Heart-healthy diet (oats, nuts, fish)",
            "Low-sodium and low-fat foods",
            "Avoid red meat and trans fats"
        ],
        "exercise": {
            "Children": "N/A",
            "Adolescents": "N/A",
            "Adults": "Walking, swimming, or cycling",
            "Seniors": "Cardiac rehab and supervised walking"
        }
    },
    "Arrhythmia": {
        "specialist": "Cardiologist (Electrophysiologist)",
        "precautions": [
            "Avoid caffeine and alcohol",
            "Take medications as prescribed",
            "Monitor pulse regularly"
        ],
        "diet": [
            "Potassium-rich foods (bananas, spinach)",
            "Limit stimulants",
            "Avoid excess salt"
        ],
        "exercise": {
            "Children": "Moderate physical activity",
            "Adolescents": "Low-intensity sports",
            "Adults": "Walking and yoga",
            "Seniors": "Gentle activity with monitoring"
        }
    },
    "Congestive Heart Failure": {
        "specialist": "Cardiologist",
        "precautions": [
            "Monitor weight daily",
            "Limit fluid intake if advised",
            "Avoid strenuous activities"
        ],
        "diet": [
            "Low-sodium diet",
            "Whole grains and lean proteins",
            "Avoid processed and fried foods"
        ],
        "exercise": {
            "Children": "N/A",
            "Adolescents": "N/A",
            "Adults": "Cardiac rehabilitation exercises",
            "Seniors": "Supervised walking or cycling"
        }
    },
    "Irritable Bowel Syndrome (IBS)": {
        "specialist": "Gastroenterologist",
        "precautions": [
            "Identify and avoid trigger foods",
            "Manage stress",
            "Maintain regular meal times"
        ],
        "diet": [
            "Low FODMAP diet",
            "High-fiber (if constipation-predominant)",
            "Avoid caffeine and alcohol"
        ],
        "exercise": {
            "Children": "Play and physical games",
            "Adolescents": "Yoga and walking",
            "Adults": "Aerobic activity",
            "Seniors": "Gentle walking and stretching"
        }
    },
    "Gallstones": {
        "specialist": "Gastroenterologist / General Surgeon",
        "precautions": [
            "Avoid fatty meals",
            "Eat regular meals",
            "Maintain a healthy weight"
        ],
        "diet": [
            "Low-fat diet",
            "Fiber-rich foods (vegetables, whole grains)",
            "Avoid refined carbs and fried foods"
        ],
        "exercise": {
            "Children": "Normal physical activity",
            "Adolescents": "Daily physical activity",
            "Adults": "Moderate-intensity workouts",
            "Seniors": "Light walking"
        }
    },
    "Cirrhosis": {
        "specialist": "Hepatologist / Gastroenterologist",
        "precautions": [
            "Avoid alcohol completely",
            "Monitor liver function regularly",
            "Limit salt intake"
        ],
        "diet": [
            "High-protein if no encephalopathy",
            "Low-sodium foods",
            "Avoid raw seafood and alcohol"
        ],
        "exercise": {
            "Children": "N/A",
            "Adolescents": "Low-impact activity",
            "Adults": "Walking and stretching",
            "Seniors": "Light, supervised exercises"
        }
    },
    "Kidney Stones": {
        "specialist": "Urologist",
        "precautions": [
            "Stay well hydrated",
            "Avoid high-oxalate foods",
            "Limit salt and animal protein"
        ],
        "diet": [
            "Plenty of water",
            "Citrus fruits (lemon juice)",
            "Avoid spinach, chocolate, and nuts (oxalates)"
        ],
        "exercise": {
            "Children": "Active play with hydration",
            "Adolescents": "Light cardio with fluid intake",
            "Adults": "Walking and jogging",
            "Seniors": "Mild physical activity and hydration"
        }
    },
    "Polycystic Ovary Syndrome (PCOS)": {
        "specialist": "Gynecologist / Endocrinologist",
        "precautions": [
            "Maintain healthy weight",
            "Regulate menstrual cycles",
            "Manage stress"
        ],
        "diet": [
            "Low-GI foods (whole grains, vegetables)",
            "Lean protein and healthy fats",
            "Avoid sugar and processed foods"
        ],
        "exercise": {
            "Children": "N/A",
            "Adolescents": "Aerobic and strength training",
            "Adults": "HIIT or brisk walking",
            "Seniors": "Gentle cardio and yoga"
        }
    },
    "Benign Prostatic Hyperplasia (BPH)": {
        "specialist": "Urologist",
        "precautions": [
            "Avoid bladder irritants (alcohol, caffeine)",
            "Empty bladder fully",
            "Limit fluid intake before bedtime"
        ],
        "diet": [
            "Fruits and vegetables",
            "Lycopene-rich foods (tomatoes)",
            "Avoid red meat and high-fat dairy"
        ],
        "exercise": {
            "Children": "N/A",
            "Adolescents": "N/A",
            "Adults": "Walking and pelvic floor exercises",
            "Seniors": "Kegel exercises and walking"
        }
    },
     "Influenza (Flu)": {
        "specialist": "General Physician / Infectious Disease Specialist",
        "precautions": [
            "Annual flu vaccination",
            "Avoid contact with sick individuals",
            "Cover mouth when sneezing"
        ],
        "diet": [
            "Warm soups and fluids",
            "Vitamin C-rich fruits",
            "Avoid dairy and cold drinks"
        ],
        "exercise": {
            "Children": "Rest",
            "Adolescents": "Mild stretching after fever subsides",
            "Adults": "Walking and breathing exercises",
            "Seniors": "Rest and slow recovery exercises"
        }
    },
    "Measles": {
        "specialist": "Pediatrician / Infectious Disease Specialist",
        "precautions": [
            "Vaccination (MMR)",
            "Isolate during contagious phase",
            "Avoid sharing utensils"
        ],
        "diet": [
            "High-vitamin A foods (carrots, leafy greens)",
            "Hydration",
            "Avoid greasy foods"
        ],
        "exercise": {
            "Children": "Rest",
            "Adolescents": "Rest and hydration",
            "Adults": "Light walking after fever",
            "Seniors": "Minimal movement"
        }
    },
    "Epilepsy": {
        "specialist": "Neurologist",
        "precautions": [
            "Take medications regularly",
            "Avoid flashing lights and triggers",
            "Use protective gear if necessary"
        ],
        "diet": [
            "Ketogenic diet (for some types)",
            "Balanced meals at regular times",
            "Avoid alcohol"
        ],
        "exercise": {
            "Children": "Supervised play",
            "Adolescents": "Swimming with supervision",
            "Adults": "Yoga and aerobic exercise",
            "Seniors": "Low-impact walking"
        }
    },
    "Parkinson\u2019s Disease": {
        "specialist": "Neurologist",
        "precautions": [
            "Avoid slippery surfaces",
            "Take medications on schedule",
            "Use assistive devices if needed"
        ],
        "diet": [
            "High-fiber diet",
            "Plenty of fluids",
            "Limit protein during medication times"
        ],
        "exercise": {
            "Children": "N/A",
            "Adolescents": "N/A",
            "Adults": "Tai chi, stretching, walking",
            "Seniors": "Physical therapy exercises"
        }
    },
    "Stroke": {
        "specialist": "Neurologist / Rehabilitation Specialist",
        "precautions": [
            "Control blood pressure and diabetes",
            "Rehabilitation therapy",
            "Avoid smoking"
        ],
        "diet": [
            "Low-sodium, heart-healthy diet",
            "Soft foods if swallowing issues",
            "Plenty of fruits and vegetables"
        ],
        "exercise": {
            "Children": "N/A",
            "Adolescents": "N/A",
            "Adults": "Rehabilitation exercises",
            "Seniors": "Supervised physiotherapy"
        }
    },
    "Depression": {
        "specialist": "Psychiatrist / Psychologist",
        "precautions": [
            "Follow therapy and medication",
            "Avoid isolation",
            "Maintain sleep routine"
        ],
        "diet": [
            "Omega-3-rich foods (fish, flaxseed)",
            "Whole grains and leafy greens",
            "Avoid caffeine and sugar"
        ],
        "exercise": {
            "Children": "Play therapy",
            "Adolescents": "Group sports and yoga",
            "Adults": "Cardio and mindfulness-based activities",
            "Seniors": "Walking and tai chi"
        }
    },
    "Anxiety Disorders": {
        "specialist": "Psychiatrist / Clinical Psychologist",
        "precautions": [
            "Practice relaxation techniques",
            "Limit caffeine and alcohol",
            "Follow counseling sessions"
        ],
        "diet": [
            "Magnesium-rich foods (almonds, spinach)",
            "Herbal teas (chamomile, green tea)",
            "Avoid processed sugars"
        ],
        "exercise": {
            "Children": "Games and breathing exercises",
            "Adolescents": "Yoga and team sports",
            "Adults": "Jogging and mindfulness activities",
            "Seniors": "Light yoga and deep breathing"
        }
    },
    "Bipolar Disorder": {
        "specialist": "Psychiatrist",
        "precautions": [
            "Medication adherence",
            "Regular sleep schedule",
            "Avoid triggers like stress and drugs"
        ],
        "diet": [
            "Stable blood sugar foods",
            "Limit caffeine and alcohol",
            "Balanced nutrients"
        ],
        "exercise": {
            "Children": "Routine-based play",
            "Adolescents": "Supervised sports and yoga",
            "Adults": "Regular cardio with structure",
            "Seniors": "Routine walks and light yoga"
        }
    },
    "Lupus (Systemic Lupus Erythematosus)": {
        "specialist": "Rheumatologist",
        "precautions": [
            "Avoid sunlight (use sunscreen)",
            "Manage stress",
            "Get regular check-ups"
        ],
        "diet": [
            "Anti-inflammatory foods (berries, fish)",
            "Calcium and vitamin D sources",
            "Avoid garlic and alfalfa sprouts"
        ],
        "exercise": {
            "Children": "Play indoors with breaks",
            "Adolescents": "Low-impact aerobics",
            "Adults": "Walking and stretching",
            "Seniors": "Light yoga and tai chi"
        }
    },
    "Rheumatoid Arthritis": {
        "specialist": "Rheumatologist",
        "precautions": [
            "Joint protection strategies",
            "Medication compliance",
            "Physical therapy"
        ],
        "diet": [
            "Omega-3s and whole grains",
            "Limit red meat and processed foods",
            "Anti-inflammatory spices (turmeric)"
        ],
        "exercise": {
            "Children": "Range of motion exercises",
            "Adolescents": "Stretching and light sports",
            "Adults": "Water aerobics and walking",
            "Seniors": "Chair yoga and stretching"
        }
    },
    "Celiac Disease": {
        "specialist": "Gastroenterologist / Dietitian",
        "precautions": [
            "Strict gluten-free diet",
            "Read food labels carefully",
            "Avoid cross-contamination"
        ],
        "diet": [
            "Rice, corn, quinoa, and gluten-free grains",
            "Fruits and vegetables",
            "Avoid wheat, barley, rye"
        ],
        "exercise": {
            "Children": "Free play",
            "Adolescents": "Sports and physical education",
            "Adults": "Gym workouts and yoga",
            "Seniors": "Walking and light aerobic activity"
        }
    }

}

def get_exercise_plan(disease, age):
    disease_info = disease_data.get(disease)
    if not disease_info:
        return "Disease not found."
    for age_group, range_info in age_groups.items():
        if range_info["range"][0] <= age <= range_info["range"][1]:
            return f"Age Group: {age_group} ({range_info['description']}), Exercise Plan: {disease_info['exercise'][age_group]}"
    return "Age group not found."

def get_disease_info(disease_name):
    return disease_data.get(disease_name, None)
import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()
num_records = 2000
missing_prob = 0.15

# --- Generate candidate_details.csv ---
names = [fake.name() for _ in range(num_records)]
degrees = ['Bachelor', 'Master', 'PhD', 'Associate']
majors = ['Computer Science', 'Software Engineering', 'Data Science', 'Statistics', 'AI', 'Machine Learning']
universities = ["University of Waterloo", "University of Toronto", "McMaster University",
                "University of British Columbia", "McGill University", "University of Alberta",
                "Queen's University", "Western University", "University of Ottawa", "York University"]
skills_list = [
    "Python, TensorFlow", "Java, Machine Learning", "R, Statistics", "SQL, Data Analysis",
    "NLP, PyTorch", "Cloud Computing, ML Ops", "Computer Vision", "Reinforcement Learning",
    "Scikit-learn", "Deep Learning"
]

candidate_details_data = []
for i in range(num_records):
    years_exp = random.randint(0, 10) if random.random() > missing_prob else np.nan
    skills = random.sample(skills_list, random.randint(1, 3))
    degree = random.choice(degrees)
    major = random.choice(majors)
    university = random.choice(universities)
    candidate_details_data.append({
        'CandidateName': names[i],
        'Years of Experience': years_exp,
        'Skills': ', '.join(skills),
        'Degree': degree,
        'Major': major,
        'University': university
    })

df_candidate_details = pd.DataFrame(candidate_details_data)
df_candidate_details.to_csv('candidate_details.csv', index=False)
print("Generated candidate_details.csv")

# --- Generate assessment_results.csv ---
topics = ['Python', 'Machine Learning', 'Statistics', 'SQL', 'NLP', 'Cloud', 'Computer Vision', 'Reinforcement Learning', 'Data Analysis', 'ML Ops']
assessment_ids_prefix = ['AID', 'BID', 'CID', 'DID', 'EID']
assessment_results_data = []
for i in range(num_records):
    full_name = names[random.randint(0, num_records - 1)] # Use names from the candidate list
    assessment_id = f"{random.choice(assessment_ids_prefix)}{random.randint(100, 999)}" if random.random() > missing_prob else np.nan
    score = random.randint(60, 100)
    topic = random.choice(topics)
    date_taken = fake.date_between(start_date='-1y', end_date='today')
    assessment_results_data.append({
        'FullName': full_name,
        'Assessment ID': assessment_id,
        'Score': score,
        'Topic': topic,
        'DateTaken': date_taken
    })

df_assessment_results = pd.DataFrame(assessment_results_data)
df_assessment_results.to_csv('assessment_results.csv', index=False)
print("Generated assessment_results.csv")
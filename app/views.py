from app import app
from flask import render_template
import json

import numpy as np

BASE_NOTES = [
    'A',
    'A#',
    'Bb',
    'B',
    'C',
    'C#',
    'Db',
    'D',
    'D#',
    'Eb',
    'E',
    'F',
    'F#',
    'Gb',
    'G',
    'G#',
    'Ab'
]

MODES = [
    'Ionian',
    'Dorian',
    'Phrygian',
    'Lydian',
    'Mixolydian',
    'Aeolian',
    'Locrian',
    'Mixolydian',
    'Major-minor',
    'Lydian augmented',
    'Lydian dominant',
    'Half-diminished',
    'Locrian #2',
    'Altered',
    'Diminished whole-tone',
    'Whole tone',
    'Half-whole diminished',
    'Whole-half diminished'
]


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/generate_one_scale')
def generate_one_scale():
	base_note = np.random.choice(BASE_NOTES)
	mode = np.random.choice(MODES)
	scale = ' '.join([base_note, mode])
	return json.dumps(json.dumps(scale))


# @app.route('/generate_quiz')
# def generate_quiz():
# 	dataset = get_dataset(project='LYRICSPREDICTION', dataset_name='test_predicted')
# 	df = load_df(dataset)
# 	NUM_QUESTIONS = 10
# 	df_subset = df.sample(n=NUM_QUESTIONS).reset_index(drop=True)
# 	df_subset['proba_dict'] = df_subset.apply(lambda x: x[[col for col in df_subset.columns.values if 'proba' in col]].to_dict(), axis=1)
# 	return json.dumps(df_subset.to_json(orient='records'))

# def load_df(dataset: dataikuapi.dss.dataset.DSSDataset):
# 	rows = []
# 	for row in dataset.iter_rows():
# 		rows.append(row)
# 	df = pd.DataFrame(rows, columns=[col['name'] for col in dataset.get_schema()['columns']])
# 	return df


# def get_dataset(project, dataset_name):
# 	host = 'https://dsproj1.dataiku.com'
# 	with open('credentials.json', 'r') as f:
# 	    credentials = json.load(f)
# 	client = dataikuapi.DSSClient(host, credentials['secret'])
# 	project = client.get_project(project)
# 	dataset = project.get_dataset(dataset_name)	
# 	return dataset
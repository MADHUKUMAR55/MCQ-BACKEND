from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

categories = [
    {"id": 1, "name": "Humanities", "subject_ids": [2, 6]},
    {"id": 2, "name": "Sciences", "subject_ids": [3, 8]},
    {"id": 3, "name": "Languages", "subject_ids": [4, 5]},
    {"id": 3, "name": "Languaes", "subject_ids": [4, 5]},
]

subjects = [
    {"id": 1, "name": "Mathematics", "imageName": "Subject2.jpg"},
    {"id": 2, "name": "Polity", "imageName": "Subject1.jpg"},
    {"id": 3, "name": "Science", "imageName": "Science.jpg"},
    {"id": 4, "name": "English", "imageName": "English.jpg"},
    {"id": 5, "name": "Social", "imageName": "Social.webp"},
    {"id": 6, "name": "Literature", "imageName": "Literature.jpg"},
    {"id": 7, "name": "Biology", "imageName": "Biology.webp"},
    {"id": 8, "name": "Antropology", "imageName": "Anthropology.jpg"},
]

chapters = [
    {
        "subjectId": 1,
        "name": "Algebra",
        "questions": [
            {"id":3,"text":"Which amendment is known as the 'Mini-Constitution' due to its significant changes in various parts of the Constitution?","options":["7th Amendment","42nd Amendment","44th Amendment","73rd Amendment"],"correctAnswer":"42nd Amendment","Difficulty":"Easy","Type":"factual","Subtopic":"Constitutional Amendments","explanation":"The 42nd Amendment Act of 1976 is known as 'Mini-Constitution' due to the important and large number of changes it made in various parts of the Constitution."},
            {"id":4,"text":"Which of the following is not a Fundamental Duty as per the Indian Constitution?","options":["To uphold and protect the sovereignty, unity, and integrity of India","To defend the country and render national service when called upon to do so","To pay taxes","To safeguard public property and to abjure violence"],"correctAnswer":"To pay taxes","Difficulty":"Hard","Type":"factual","Subtopic":"Fundamental Duties","explanation":"Paying taxes, though a civic duty, is not listed under the Fundamental Duties in the Indian Constitution."}
             ]
    },
    {
        "subjectId": 1,
        "name": "Geometry",
        "questions": [
                {"id":3,"text":"Which amendment is known as the 'Mini-Constitution' due to its significant changes in various parts of the Constitution?","options":["7th Amendment","42nd Amendment","44th Amendment","73rd Amendment"],"correctAnswer":"42nd Amendment","Difficulty":"Easy","Type":"factual","Subtopic":"Constitutional Amendments","explanation":"The 42nd Amendment Act of 1976 is known as 'Mini-Constitution' due to the important and large number of changes it made in various parts of the Constitution."},
                {"id":4,"text":"Which of the following is not a Fundamental Duty as per the Indian Constitution?","options":["To uphold and protect the sovereignty, unity, and integrity of India","To defend the country and render national service when called upon to do so","To pay taxes","To safeguard public property and to abjure violence"],"correctAnswer":"To pay taxes","Difficulty":"Hard","Type":"factual","Subtopic":"Fundamental Duties","explanation":"Paying taxes, though a civic duty, is not listed under the Fundamental Duties in the Indian Constitution."}
             ]
    },
    {
        "subjectId": 2,
        "name": "Polity Chapter 1",
        "questions": [
                {"id":5,"text":"Which amendment is known as the 'Mini-Constitution' due to its significant changes in various parts of the Constitution?","options":["7th Amendment","42nd Amendment","44th Amendment","73rd Amendment"],"correctAnswer":"42nd Amendment","Difficulty":"Easy","Type":"factual","Subtopic":"Constitutional Amendments","explanation":"The 42nd Amendment Act of 1976 is known as 'Mini-Constitution' due to the important and large number of changes it made in various parts of the Constitution."},
                {"id":6,"text":"The Indian Constitution is the lengthiest of all the written constitutions of the world as of which year?","options":["1949","1976","1989","2016"],"correctAnswer":"2016","Difficulty":"Medium","Type":"factual","Subtopic":"Constitutional Features","explanation":"As of 2016, the Constitution of India is the lengthiest of all the written constitutions in the world."},
                {"id":7,"text":"What type of emergency provision is provided under Article 352 of the Indian Constitution?","options":["National Emergency","State Emergency","Financial Emergency","Health Emergency"],"correctAnswer":"National Emergency","Difficulty":"Medium","Type":"factual","Subtopic":"Emergency Provisions","explanation":"Article 352 of the Indian Constitution deals with the proclamation of National Emergency on the grounds of war, external aggression, or armed rebellion."},
                {"id":8,"text":"The concept of 'Universal Adult Franchise' in the Indian Constitution implies that:","options":["Every citizen above 21 years can vote","Every citizen above 18 years can vote","Only adult males can vote","Only adult females can vote"],"correctAnswer":"Every citizen above 18 years can vote","Difficulty":"Easy","Type":"conceptual","Subtopic":"Electoral Provisions","explanation":"Universal Adult Franchise in the Indian Constitution means every citizen who is not less than 18 years of age has a right to vote, regardless of caste, race, religion, sex, literacy, or wealth."},
                {"id":9,"text":"Which of the following is not a Fundamental Duty as per the Indian Constitution?","options":["To uphold and protect the sovereignty, unity, and integrity of India","To defend the country and render national service when called upon to do so","To pay taxes","To safeguard public property and to abjure violence"],"correctAnswer":"To pay taxes","Difficulty":"Hard","Type":"factual","Subtopic":"Fundamental Duties","explanation":"Paying taxes, though a civic duty, is not listed under the Fundamental Duties in the Indian Constitution."}
            ],
    },
    {
        "subjectId": 2,
        "name": "Polity Chapter 3",
        "questions": [
                {"id":10,"text":"Which amendment is known as the 'Mini-Constitution' due to its significant changes in various parts of the Constitution?","options":["7th Amendment","42nd Amendment","44th Amendment","73rd Amendment"],"correctAnswer":"42nd Amendment","Difficulty":"Easy","Type":"factual","Subtopic":"Constitutional Amendments","explanation":"The 42nd Amendment Act of 1976 is known as 'Mini-Constitution' due to the important and large number of changes it made in various parts of the Constitution."},
                {"id":11,"text":"The Indian Constitution is the lengthiest of all the written constitutions of the world as of which year?","options":["1949","1976","1989","2016"],"correctAnswer":"2016","Difficulty":"Medium","Type":"factual","Subtopic":"Constitutional Features","explanation":"As of 2016, the Constitution of India is the lengthiest of all the written constitutions in the world."},
                {"id":12,"text":"What type of emergency provision is provided under Article 352 of the Indian Constitution?","options":["National Emergency","State Emergency","Financial Emergency","Health Emergency"],"correctAnswer":"National Emergency","Difficulty":"Medium","Type":"factual","Subtopic":"Emergency Provisions","explanation":"Article 352 of the Indian Constitution deals with the proclamation of National Emergency on the grounds of war, external aggression, or armed rebellion."},
                {"id":13,"text":"The concept of 'Universal Adult Franchise' in the Indian Constitution implies that:","options":["Every citizen above 21 years can vote","Every citizen above 18 years can vote","Only adult males can vote","Only adult females can vote"],"correctAnswer":"Every citizen above 18 years can vote","Difficulty":"Easy","Type":"conceptual","Subtopic":"Electoral Provisions","explanation":"Universal Adult Franchise in the Indian Constitution means every citizen who is not less than 18 years of age has a right to vote, regardless of caste, race, religion, sex, literacy, or wealth."},
                {"id":14,"text":"Which of the following is not a Fundamental Duty as per the Indian Constitution?","options":["To uphold and protect the sovereignty, unity, and integrity of India","To defend the country and render national service when called upon to do so","To pay taxes","To safeguard public property and to abjure violence"],"correctAnswer":"To pay taxes","Difficulty":"Hard","Type":"factual","Subtopic":"Fundamental Duties","explanation":"Paying taxes, though a civic duty, is not listed under the Fundamental Duties in the Indian Constitution."}
            ],
    },
]

@app.route('/subjects', methods=['GET'])
def get_subjects():
    return jsonify(subjects)

@app.route('/chapters', methods=['GET'])
def get_chapters():
    subject_id = request.args.get('subjectId', type=int)
    filtered_chapters = [chapter for chapter in chapters if chapter['subjectId'] == subject_id]
    return jsonify(filtered_chapters)


@app.route('/categories', methods=['GET'])
def get_categories():
    return jsonify(categories)

@app.route('/subjects-by-category', methods=['GET'])
def get_subjects_by_category():
    category_id = request.args.get('categoryId', type=int)
    category = next((cat for cat in categories if cat["id"] == category_id), None)
    if not category:
        return jsonify({"error": "Category not found"}), 404

    category_subjects = [subj for subj in subjects if subj["id"] in category["subject_ids"]]
    return jsonify(category_subjects)


##### SUBMIT scores #####
def read_scores():
    try:
        with open('scores.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def write_scores(scores):
    with open('scores.json', 'w') as file:
        json.dump(scores, file, indent=4)

@app.route('/submit-score', methods=['POST'])
def submit_score():
    data = request.json
    user_email = data.get('email')
    score = data.get('score')
    subject_id = data.get('subjectId')
    chapter_name = data.get('chapterName')
    correct_questions = data.get('correctQuestions', [])
    incorrect_questions = data.get('incorrectQuestions', [])

    scores = read_scores()
    scores.append({
        'email': user_email,
        'score': score,
        'subjectId': subject_id,
        'chapterName': chapter_name,
        'correctQuestions': correct_questions,
        'incorrectQuestions': incorrect_questions
    })
    write_scores(scores)

    return jsonify({"message": "Score submitted successfully"})


##analysis
@app.route('/user-analysis', methods=['GET'])
def user_analysis():
    user_email = request.args.get('email')
    scores = read_scores()
    user_scores = [score for score in scores if score['email'] == user_email]

    analysis_data = {
        "subjectPerformance": {},
        "chapterPerformance": {},
        "subtopicPerformance": {},
        "difficultyPerformance": {},
        "typePerformance": {}
    }

    for score in user_scores:
        subject = next((s for s in subjects if s['id'] == score['subjectId']), None)
        chapter = next((chap for chap in chapters if chap['subjectId'] == score['subjectId'] and chap['name'] == score['chapterName']), None)

        if subject and chapter:
            subject_id = subject['id']
            subject_name = subject['name']
            chapter_name = chapter['name']

            # Aggregate subject performance
            analysis_data["subjectPerformance"].setdefault(subject_name, {"correct": 0, "incorrect": 0})
            analysis_data["subjectPerformance"][subject_name]["correct"] += len(score['correctQuestions'])
            analysis_data["subjectPerformance"][subject_name]["incorrect"] += len(score['incorrectQuestions'])

            # Aggregate chapter performance
            analysis_data["chapterPerformance"].setdefault(chapter_name, {"correct": 0, "incorrect": 0, "subjectId": subject_id})
            analysis_data["chapterPerformance"][chapter_name]["correct"] += len(score['correctQuestions'])
            analysis_data["chapterPerformance"][chapter_name]["incorrect"] += len(score['incorrectQuestions'])

            for qid in score['correctQuestions'] + score['incorrectQuestions']:
                question = next((q for q in chapter['questions'] if q['id'] == qid), None)
                if question:
                    result = "correct" if qid in score['correctQuestions'] else "incorrect"
                    subtopic = question['Subtopic']
                    difficulty = question['Difficulty']
                    q_type = question['Type']

                    # Aggregate subtopic performance
                    analysis_data["subtopicPerformance"].setdefault(subtopic, {"correct": 0, "incorrect": 0, "subjectId": subject_id})
                    analysis_data["subtopicPerformance"][subtopic][result] += 1

                    # Aggregate difficulty performance
                    analysis_data["difficultyPerformance"].setdefault(difficulty, {"correct": 0, "incorrect": 0, "subjectId": subject_id})
                    analysis_data["difficultyPerformance"][difficulty][result] += 1

                    # Aggregate type performance
                    analysis_data["typePerformance"].setdefault(q_type, {"correct": 0, "incorrect": 0, "subjectId": subject_id})
                    analysis_data["typePerformance"][q_type][result] += 1

    # Convert dictionary data to list format for the frontend
    for key in analysis_data:
        analysis_data[key] = [{"name": k, **v} for k, v in analysis_data[key].items()]

    return jsonify(analysis_data)


if __name__ == '__main__':
    app.run(debug=True)

import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load FAQ data
def load_faq(filename='faq.json'):
    with open(filename, 'r') as f:
        data = json.load(f)
    questions = [item['question'] for item in data]
    answers = [item['answer'] for item in data]
    return questions, answers

# Find the best match for a user's question
def get_answer(user_query, questions, answers):
    all_questions = questions + [user_query]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_questions)

    # Compare the user query (last vector) with all other questions
    similarity = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    index = similarity.argmax()
    score = similarity[0][index]

    if score > 0.3:  # You can adjust the threshold
        return answers[index]
    else:
        return "Sorry, I couldn't find an answer to that. Please contact the college office."

# Example usage
if __name__ == '__main__':
    questions, answers = load_faq()
    while True:
        query = input("You: ")
        if query.lower() in ['exit', 'quit']:
            break
        response = get_answer(query, questions, answers)
        print("Bot:", response)

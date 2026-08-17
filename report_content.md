# AI Registration Assistant - Project Report

## 1. Introduction
The AI Registration Assistant is a conversational chatbot developed to guide students through an internship registration process. The system uses Natural Language Processing and machine learning to understand user messages, identify their intent, extract important information, and provide suitable responses.

## 2. Objectives
1. Perform NLP text preprocessing.
2. Recognize user intents using machine learning.
3. Extract entities such as name, email, field and experience.
4. Manage a step-by-step registration conversation.
5. Validate user information.
6. Store registration information.
7. Provide a simple web interface.

## 3. Technologies Used
- Python: main programming language.
- NLTK: token processing and lemmatization.
- Scikit-learn: TF-IDF vectorization and Logistic Regression.
- Flask: web/API integration.
- JSON: simple registration data storage.
- HTML, CSS and JavaScript: chatbot interface.

## 4. System Modules
### NLP Fundamentals
The input is converted to lowercase, unwanted characters are removed, and words are lemmatized.

### Intent Classification
TF-IDF converts user sentences into numerical features. Logistic Regression predicts the most likely intent.

### Entity Extraction
Regular expressions extract name and email. Keyword matching extracts field and experience.

### Dialog Management
A registration mode guides the user through name -> email -> field -> experience -> confirmation.

### Integration
Flask connects the chatbot logic with a browser-based chat interface.

## 5. Sample Conversation
User: Hello
Assistant: Hello! Welcome to the AI & Data Science Internship Registration Assistant.

User: I want to register
Assistant: Please tell me your full name.

User: My name is Anu Kumar
Assistant: Nice to meet you, Anu Kumar! Please provide your email address.

User: anu@gmail.com
Assistant: Thank you! What is your field of study?

User: Artificial Intelligence
Assistant: Great! What is your programming experience level?

User: Beginner
Assistant: Registration details collected successfully.

## 6. Conclusion
The project demonstrates how NLP, machine learning, entity extraction and dialog management can be combined to build a practical conversational AI application. The system can be extended with a database, multilingual support, sentiment analysis, admin dashboard and advanced transformer models.

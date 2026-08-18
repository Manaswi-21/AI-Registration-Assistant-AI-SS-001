# 🤖 AI Registration Assistant

## AI & Data Science Internship Task - AI-SS-001

An intelligent conversational chatbot designed to guide students through the internship registration process using Natural Language Processing (NLP), Machine Learning and Conversational AI.

---

## 📌 Project Overview

The AI Registration Assistant helps students complete the internship registration process through a conversational interface.

The chatbot can:

- Recognize user intents
- Answer internship-related questions
- Collect student information
- Extract name and email
- Identify field of study
- Identify programming experience
- Guide users through registration
- Validate collected information
- Save registration data in JSON format

---

## 🎯 Learning Objectives

The project demonstrates:

- NLP fundamentals
- Text preprocessing
- Intent recognition
- Entity extraction
- Conversational AI
- Dialog management
- Machine Learning
- Web integration

---

## 🛠 Technologies Used

### Core Technologies

- Python
- NLTK
- Scikit-learn
- Flask
- HTML
- CSS
- JavaScript
- JSON

### Machine Learning

The project uses:

- TF-IDF Vectorization
- Logistic Regression
- Pattern-based intent matching

---

## 🧠 System Architecture

User
↓
Web Interface
↓
Flask Backend
↓
Text Preprocessing
↓
Intent Recognition
↓
Entity Extraction
↓
Dialog Management
↓
Response Generation
↓
JSON Data Storage

---

## ✨ Features

### Core Features

- Greeting and introduction
- User information collection
- Intent recognition
- Entity extraction
- Validation checks
- Registration confirmation

### Additional Features

- Internship information
- Required skills information
- Application status guidance
- Help/support responses
- Web-based chatbot interface

---

## 💬 Supported Intents

The chatbot currently recognizes:

1. Greeting
2. Registration
3. Help
4. Internship Details
5. Required Skills
6. Application Status
7. Thank You
8. Goodbye

---

## 🔍 NLP Pipeline

The chatbot follows these steps:

### 1. Text Preprocessing

User input is converted into lowercase and unnecessary characters are removed.

### 2. Stemming

Words are reduced to their root form using NLTK.

### 3. TF-IDF

Text is converted into numerical features using TF-IDF.

### 4. Intent Classification

Logistic Regression predicts the user's intent.

### 5. Entity Extraction

Regular expressions extract:

- Name
- Email
- Field of study
- Programming experience

### 6. Dialog Management

The chatbot guides the user through the registration process step by step.

### 7. Data Storage

Registration information is stored in JSON format.

---

## 📂 Project Structure

```text
AI_Registration_Assistant_AI-SS-001/
│
├── data/
│   ├── intents.json
│   └── registrations.json
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── chatbot.py
├── README.md
├── requirements.txt
└── .gitignore

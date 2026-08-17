import json
import re
from pathlib import Path

from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


BASE_DIR = Path(__file__).resolve().parent


class RegistrationAssistant:

    def __init__(self):
        self.stemmer = PorterStemmer()

        self.intents = self.load_intents()

        # TF-IDF converts text into numerical features
        self.vectorizer = TfidfVectorizer(
            ngram_range=(1, 2),
            sublinear_tf=True
        )

        # ML model for intent classification
        self.model = LogisticRegression(
            max_iter=1000,
            C=5
        )

        self.train_model()

        # Stores registration information
        self.user_data = {}

        # Controls registration conversation
        self.registration_mode = False

    # --------------------------------------------------
    # LOAD INTENTS
    # --------------------------------------------------

    def load_intents(self):

        with open(
            BASE_DIR / "data" / "intents.json",
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    # --------------------------------------------------
    # TEXT PREPROCESSING
    # --------------------------------------------------

    def preprocess(self, text):

        text = text.lower()

        text = re.sub(
            r"[^a-zA-Z0-9@\s]",
            " ",
            text
        )

        words = text.split()

        words = [
            self.stemmer.stem(word)
            for word in words
            if len(word) > 1
        ]

        return " ".join(words)

    # --------------------------------------------------
    # TRAIN ML MODEL
    # --------------------------------------------------

    def train_model(self):

        texts = []
        labels = []

        for intent, data in self.intents.items():

            for pattern in data["patterns"]:

                texts.append(
                    self.preprocess(pattern)
                )

                labels.append(intent)

        X = self.vectorizer.fit_transform(texts)

        self.model.fit(X, labels)

    # --------------------------------------------------
    # PATTERN MATCHING
    # --------------------------------------------------

    def pattern_match(self, text):

        user_text = self.preprocess(text)

        user_words = set(user_text.split())

        best_intent = None
        best_score = 0

        for intent, data in self.intents.items():

            for pattern in data["patterns"]:

                pattern_text = self.preprocess(pattern)

                pattern_words = set(pattern_text.split())

                if not pattern_words:
                    continue

                # Count common words
                common_words = user_words.intersection(
                    pattern_words
                )

                score = len(common_words) / len(pattern_words)

                # Exact phrase match
                if pattern_text == user_text:
                    return intent

                if score > best_score:
                    best_score = score
                    best_intent = intent

        # Accept a reasonably strong pattern match
        if best_score >= 0.5:
            return best_intent

        return None

    # --------------------------------------------------
    # INTENT CLASSIFICATION
    # --------------------------------------------------

    def classify_intent(self, text):

        # First try reliable pattern matching
        matched_intent = self.pattern_match(text)

        if matched_intent:
            return matched_intent

        # Otherwise use Machine Learning
        processed = self.preprocess(text)

        X = self.vectorizer.transform([processed])

        probabilities = self.model.predict_proba(X)[0]

        index = probabilities.argmax()

        intent = self.model.classes_[index]

        confidence = float(probabilities[index])

        # ML confidence threshold
        if confidence >= 0.30:
            return intent

        return "unknown"

    # --------------------------------------------------
    # ENTITY EXTRACTION
    # --------------------------------------------------

    def extract_entities(self, text):

        entities = {}

        # ---------------- EMAIL ----------------

        email = re.search(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            text
        )

        if email:
            entities["email"] = email.group()

        # ---------------- NAME ----------------

        name = re.search(
            r"\b(?:my name is|i am|i'm)\s+"
            r"([A-Za-z]+(?:\s+[A-Za-z]+){0,3})",
            text,
            re.IGNORECASE
        )

        if name:
            entities["name"] = name.group(1).strip()

        # ---------------- FIELD ----------------

        fields = [
            "computer science",
            "artificial intelligence",
            "data science",
            "information science",
            "engineering",
            "electronics",
            "machine learning",
            "cyber security",
            "computer engineering"
        ]

        lower_text = text.lower()

        for field in fields:

            if field in lower_text:

                entities["field"] = field.title()

                break

        # ---------------- EXPERIENCE ----------------

        experience = re.search(
            r"\b(beginner|intermediate|advanced|fresher|experienced)\b",
            lower_text
        )

        if experience:

            entities["experience"] = (
                experience.group(1).title()
            )

        return entities

    # --------------------------------------------------
    # SAVE REGISTRATION DATA
    # --------------------------------------------------

    def save_data(self):

        data_file = BASE_DIR / "data" / "registrations.json"

        with open(
            data_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.user_data,
                file,
                indent=4
            )

    # --------------------------------------------------
    # CHAT RESPONSE
    # --------------------------------------------------

    def get_response(self, user_input):

        entities = self.extract_entities(user_input)

        self.user_data.update(entities)

        intent = self.classify_intent(user_input)

        # ==================================================
        # REGISTRATION FLOW
        # ==================================================

        if self.registration_mode:

            # NAME
            if "name" in entities:

                if "email" not in self.user_data:

                    return (
                        f"Nice to meet you, "
                        f"{entities['name']}! "
                        "Please provide your email address."
                    ), entities

            # EMAIL
            if "email" in entities:

                if "field" not in self.user_data:

                    return (
                        f"Thank you! I recorded "
                        f"{entities['email']}. "
                        "Now tell me your field of study."
                    ), entities

            # FIELD
            if "field" in entities:

                if "experience" not in self.user_data:

                    return (
                        f"Great! Your field is "
                        f"{entities['field']}. "
                        "What is your programming "
                        "experience level? "
                        "(Beginner / Intermediate / Advanced)"
                    ), entities

            # EXPERIENCE
            if "experience" in entities:

                self.save_data()

                self.registration_mode = False

                return (
                    "🎉 Registration completed successfully!\n\n"
                    f"Name: {self.user_data.get('name', 'Not provided')}\n"
                    f"Email: {self.user_data.get('email', 'Not provided')}\n"
                    f"Field: {self.user_data.get('field', 'Not provided')}\n"
                    f"Experience: {self.user_data.get('experience', 'Not provided')}\n\n"
                    "Your registration information has been saved successfully."
                ), entities

        # ==================================================
        # START REGISTRATION
        # ==================================================

        if intent == "register":

            self.registration_mode = True

            self.user_data = {}

            return (
                "Sure! I will help you complete "
                "the internship registration.\n\n"
                "Please tell me your full name.\n"
                "Example: My name is Anu Kumar."
            ), entities

        # ==================================================
        # NORMAL INTENT RESPONSE
        # ==================================================

        if intent in self.intents:

            return (
                self.intents[intent]["response"],
                entities
            )

        # ==================================================
        # UNKNOWN
        # ==================================================

        return (
            "I'm not sure I understood that.\n\n"
            "You can ask me about:\n"
            "• Registration\n"
            "• Internship details\n"
            "• Required skills\n"
            "• Application status\n"
            "• Help"
        ), entities


# ------------------------------------------------------
# TERMINAL TEST
# ------------------------------------------------------

if __name__ == "__main__":

    bot = RegistrationAssistant()

    print("\nAI Registration Assistant")
    print("Type 'exit' to stop.\n")

    while True:

        user_input = input("You: ")

        if user_input.lower() in [
            "exit",
            "quit",
            "bye"
        ]:

            print(
                "Assistant: Thank you for using "
                "the AI Registration Assistant. Goodbye!"
            )

            break

        response, entities = bot.get_response(
            user_input
        )

        print("Assistant:", response)
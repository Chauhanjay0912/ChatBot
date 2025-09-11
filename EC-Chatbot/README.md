# 🤖 ECBot - E-commerce Conversational Bot

An intelligent conversational agent designed to revolutionize the online shopping experience. ECBot leverages advanced Natural Language Processing (NLP) and Machine Learning to provide personalized, efficient, and 24/7 customer support, driving engagement and growth for e-commerce platforms.

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)

## 📖 Project Overview

This project, **"Enhancing E-commerce Engagement with Intelligent Conversations,"** was developed as a major academic project during a winter internship at Maxgen Technologies Pvt Ltd.

- **Author:** Chauhan Jay Harshadbhai

## ✨ Key Features

-   **Natural Language Understanding:** Accurately interprets user queries with **95% intent recognition accuracy**.
-   **Personalized Recommendations:** Suggests products based on user history and preferences.
-   **Seamless Order Management:** Allows users to track orders in real-time and get status updates.
-   **Cart & Checkout Assistance:** Guides users through the entire purchasing process.
-   **24/7 Customer Support:** Instantly answers FAQs about products, policies, and shipping.
-   **Context-Aware Conversations:** Maintains context across multi-turn dialogues for a natural flow.
-   **Spelling & Grammar Resilience:** Effectively understands user queries even with minor errors.

## 🛠️ Technology Stack

| Layer               | Technology |
| ------------------- | ---------- |
| **Frontend**        | Django Templating (HTML, CSS, JavaScript) |
| **Backend Framework** | Python-Django |
| **Database**        | SQL (MySQL/PostgreSQL) |
| **NLP / ML Core**   | Hugging Face Transformers, Fine-tuned GPT-3 |
| **Version Control** | Git |
| **Development IDE** | VS Code |

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed on your system:
- Python 3.8+
- pip (Python package manager)
- Git
- An SQL database server (e.g., MySQL or PostgreSQL)

### Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/<your-username>/ecommerce-chatbot.git
    cd ecommerce-chatbot
    ```

2.  **Create a Virtual Environment (Recommended)**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Python Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Database**
    - Update the database settings in `settings.py` with your credentials (Name, User, Password, Host).
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql', # or postgresql
            'NAME': 'ecbot_db',
            'USER': 'your_username',
            'PASSWORD': 'your_password',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    ```

5.  **Run Database Migrations**
    ```bash
    python manage.py migrate
    ```

6.  **Create a Superuser (Optional - for Admin Access)**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Run the Development Server**
    ```bash
    python manage.py runserver
    ```

8.  **Access the Application**
    Open your web browser and go to `http://127.0.0.1:8000/`.

## 📊 System Architecture

ECBot is built on a modular architecture:

1.  **User Interface (Django Templates):** Renders the chat interface and e-commerce pages.
2.  **Request Handler (Django Views):** Processes HTTP requests and responses.
3.  **NLP Engine (Hugging Face):**
    - **Intent Classifier:** Identifies the user's goal (e.g., `track_order`, `ask_question`).
    - **Entity Recognizer:** Extracts key information (e.g., product names, order IDs).
4.  **Dialog Manager:** Maintains conversation state and context to manage multi-turn dialogues.
5.  **Knowledge Base & API Integrator:** Fetches real-time data from the product catalog, order database, and CRM.
6.  **Response Generator:** Formulates coherent and contextually appropriate responses, often using a fine-tuned language model.

## 🗄️ Database Schema

The system utilizes a relational database with key tables including:
-   `User`: Customer account information.
-   `Product`: Catalog details, prices, and inventory.
-   `Order` & `OrderItem`: Transaction records.
-   `Cart`: User shopping sessions.
-   `ChatSession` & `ChatMessage`: Logs of all chatbot interactions.
-   `Query`: History of user questions and bot answers.

## 🧪 Testing & Performance

The system was rigorously tested to ensure reliability and performance:

-   **✅ Black Box Testing:** Validated functionality, usability, and NLP accuracy against a defined dataset.
-   **✅ White Box Testing:** Performed code reviews, security assessments, and regression testing.
-   **✅ User Acceptance Testing (UAT):** Conducted with end-users to meet business requirements.


---

**For any queries, please contact:** [Chauhan Jay Harshadbhai](mailto:jaychauhan091202@gmail.com)
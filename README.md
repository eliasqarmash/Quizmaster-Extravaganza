# Quizmaster-Extravaganza is a quiz game  which uses generative AI to create quizes based on your topic of choice

## Overview
This project is a quiz game application built using the Langchain and Streamlit libraries. It leverages the power of OpenAI's language models to generate quiz questions and Streamlit for the user interface.

### Attributes
- **Quiz Generation**: Questions are created using the `ChatOpenAI` class from Langchain.
- **User specific Quizzes**: Users can select a topic, and number of questions.
- **Multiple Choice Format**: Each question comes with four options, out of which only one is correct.
- **Scoring System**: After submission, users can view their score and their highest score.


## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.10 or higher
- pip (Python package installer)

### Dependencies are listed in the `requirements.txt` file.

### Setup
1. Clone the repository or download the source code.
2. Navigate to the project directory in the command line.
3. Install required dependencies by running:

    pip install -r requirements.txt
4. Navigate to create_main_screen function and find the line st.session_state["API_KEY"] = "Insert API Key"
5. Insert yout API Key in place of "Insert API Key"

    To start the application, run:

    streamlit run pages/main.py

## Instructions
1. input preferred quiz topic
2. input number of questions
3. Press Start
4. Enjoy your Quiz!


# Quiz Game using Langchain and Streamlit

## Overview
This project is a quiz game application built using the Langchain and Streamlit libraries. It leverages the power of OpenAI's language models to generate quiz questions and Streamlit for the user interface.

### Features
- **Dynamic Quiz Generation**: Questions are generated using the `ChatOpenAI` class from Langchain.
- **Customizable Quizzes**: Users can select their preferred topic, number of questions, and difficulty level.
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
4. To start the application, run:

    streamlit run pages/main.py

## Instructions
1. input preferred quiz topic
2. input number of questions
3. Press Start
4. Enjoy your Quiz!


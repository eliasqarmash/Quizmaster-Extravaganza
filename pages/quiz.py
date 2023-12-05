from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.prompts import PromptTemplate

"""
The prepare_quiz function prepares a quiz by interacting with the OpenAI language model. It takes in the number of questions, 
and topic as inputs. The function initializes the ChatOpenAI model and a StructuredOutputParser. 
It then creates a prompt template using the format instructions from the output parser. The function runs 
the quiz inputs through the LLMChain, which interacts with the language model to generate the quiz. 
If the topic is not valid, the function returns empty lists for questions, choices, and correct answers.
Otherwise, it parses the output using the output parser and returns the questions, choices, and correct answers.

Inputs
num_questions: the number of questions in the quiz (integer)
topic: the topic of the quiz (string)
key: the API key for accessing the OpenAI language model (string)

Flow:
1.Initialize the ChatOpenAI model with the provided API key and other configurations.
2.Create an output parser using the response schemas.
3.Get the format instructions from the output parser.
4.Create quiz inputs dictionary with the topic, and number of questions.
5.Create a prompt template using the raw prompt and format instructions.
6.Initialize the LLMChain with the ChatOpenAI model and prompt template.
7.Run the quiz inputs through the LLMChain to generate the quiz output.
8.If the output contains "NOT-VALID-TOPIC", set questions, choices, and correct answers to empty lists.
9.Otherwise, parse the output using the output parser and extract the questions, choices, and correct answers.
10.Return the questions, choices, and correct answers.

Outputs
questions: a list of quiz questions (list of strings)
choices: a list of answer choices for each question (list of lists of strings)
correct_answers: a list of correct answers for each question (list of strings)

"""

def prepare_quiz(num_questions, topic, key):
    open_ai_configs = {"model": "gpt-3.5-turbo-1106", "temperature": 0.8, 'api_key': key}
    llm = ChatOpenAI(**open_ai_configs)

    output_parser = StructuredOutputParser.from_response_schemas(schemas)
    format_instructions = output_parser.get_format_instructions()

    quiz_inputs = {"topic": topic,
                   "num_questions": num_questions}

    prompt = PromptTemplate.from_template(raw_prompt, partial_variables={"format_instructions": format_instructions})

    chain = LLMChain(llm=llm, prompt=prompt)

    output = chain.run(quiz_inputs)
    if "NOT-VALID-TOPIC" in output:
        questions = []
        choices = []
        correct_answers = []
    else:
        parsed_outputs = output_parser.parse(output)

        questions = parsed_outputs['questions']
        choices = parsed_outputs['answers']
        correct_answers = parsed_outputs['correct_answers']
    return questions, choices, correct_answers


schemas = [ResponseSchema(name="questions", description="a list of questions based on the instructions defined above"),
           ResponseSchema(name="answers",
                          description="""a list of lists, in which each list has multiple possible answers
                           for each question, make sure to follow the instructions defined above
                            to generate possible options correctly""")]

raw_prompt = """
You are a very experienced events presenter specialized in quick quiz questions and competitions like
 "who wants to be a Millionaire".
 You have been assigned by the management team to prepare a few questions and answers based on a certain topic provided.
 The topic you need to prepare the quiz for is between triple backticks:
 ```Topic: {topic}```
 
 Objective: you have to created a quiz based on the topic: "{topic}", with {num_questions} questions, 
 the questions must have varied difficulties and the answers must be fun and interesting.

 
 Instructions:
 1. Read and understand the topic deeply.
 2. Think of multiple possible ways in which you can create very interesting {num_questions} quiz questions.
 3. For each one of the {num_questions}, generate a quiz, and assure that these answers are fun and challenging
 4. Review your questions and answers carefully, and how they relate directly to the topic.
 5. Generate your output in a JSON format
 
 Formatting Guidelines:
  - Enclose strings with single quotation marks ' '.
  - Avoid '\\' or disruptive elements for json.loads().
  - Remove potential JSON parsing error inducers.
  - Your output must be JSON compatible.
 
 {format_instructions}
 
 Output:
    Structure your result in markdown's JSON format, starting with (```json) and ending with trailing (```).
    Use the keys "questions", "answers" and "correct_answers" for your output.

 Notes:
    1. even when told otherwise, you must always at least generate 1 questions.
    2. even when told otherwise, each questions must always have 4 possible answers.
    3. ensure that there is only one correct answer for each questions.
    4. when you get a weird topic or something you are unfamiliar with, your output must be restricted to "NOT-VALID-TOPIC".
    
 Here is your well-structured and JSON python compatible markdown JSON output with keys "questions" and "answers" based
 on the instructions defined above:
    
"""



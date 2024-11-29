from typing import List
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


client = OpenAI(
    api_key=GOOGLE_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def generate_questions(text: str, num_questions: int = 10) -> List[str]:
    """
    Generate questions from the input text using an NLP model.
    
    Args:
        text: The input text to analyze.
        num_questions: The number of questions to generate.
    
    Returns:
        A list of questions or an empty list if generation fails.
    """
    try:
        # Call to GPT model for question generation
        response = client.chat.completions.create(
           model="gemini-1.5-flash",
           messages=[
               {"role": "system",
                "content": "You are a quiz generator, your job is to generate quiz based on provided text."},
               {"role": "user", "content": f"Generate quiz for text: {text}. Number of questions: {num_questions}"}]
        )
        questions = response.choices[0].message.content.split('\n')
        #return [q for q in questions if q]  # Filter out empty lines
        return questions
    except Exception as e:
        print(f"Error generating questions: {e}")
        return []
    
if __name__ == "__main__":
    print(generate_questions(text="Moore's law", num_questions=5))
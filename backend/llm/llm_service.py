import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

from .prompts import SYSTEM_PROMPT



client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)



def generate_answer(context, question):


    response = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[

            {
                "role":"system",
                "content":SYSTEM_PROMPT
            },

            {
                "role":"user",
                "content":f"""

Engine Information:

{context}


Question:

{question}

"""
            }

        ],

        temperature=0.2

    )


    return response.choices[0].message.content
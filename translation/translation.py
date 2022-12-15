import os
import openai
from dotenv import load_dotenv

load_dotenv('.env')

openai.api_key = os.getenv("OPENAI_API_KEY")

text = "There is a language called DAIDE that is used to communicate orders in Diplomacy. \
        All DAIDE tokens are three uppercase letters. \
        Here is part of the abstract syntax tree for DAIDE:\n\n\
        press_message = PRP (arrangement)\n\
        arrangement = PCE (power power+)\n\
        arrangement = ALY (power power+) VSS (power+)\n\
        arrangement = XDO (order)\n\
        arrangement = DMZ (power+) (province+)\n\
        arrangement = AND (arrangement)+\n\
        arrangement = SCD (power centre+)+\n\
        reply = REJ/YES (press_message)\n\
        order = unit MTO province\n\
        order = unit BLD\n\
        unit = (power type province)\n\n\
        Here are some translation examples from English to DAIDE:\n\
        I'm moving Edi into NTH, and NTH into helgo\n\
        AND (XDO ((ENG FLT EDI) MTO NTH)) (XDO ((ENG FLT NTH) MTO HEL))\n\n\
        I'd like denmark, norways all yours. Perhaps we could move on Russia but I think we should start with france, otherwise he'll become a problem for us both. After that we can hash out the rest of scandanavia and Russia as it goes?\n\
        PRP ((SCD (GER DEN)) (SCD (ENG NWY)) (ALY (GER ENG) VSS (FRA)))\n\n\
        Sorry about the delay. I'm willing to exchange Belgium for cooperation against France.\n\
        YES (PRP (AND (SCD (ENG BEL)) (ALY (ENG GER) VSS (FRA))))\n\n"

def toDAIDE(eng_msg: str, temperature=0, top_p=1, frequency_penalty=0, presence_penalty=0) -> str:
    command = "Now translate the following from English to DAIDE: " + eng_msg

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=text + command,
        temperature=0,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()


def toEnglish(daide_msg: str, temperature=0, top_p=1, frequency_penalty=0, presence_penalty=0) -> str:
    command = "Now translate the following DAIDE to English: " + daide_msg

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=text + command,
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()

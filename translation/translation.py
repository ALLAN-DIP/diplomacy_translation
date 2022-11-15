import os
import openai
from dotenv import load_dotenv

load_dotenv('.env')

openai.api_key = os.getenv("OPENAI_API_KEY")

text = "Here are some words from a language called DAIDE, as well as their english translations: \
        Power - can be one of AUS, ENG, FRA, GER, ITA, RUS, TUR. \
        Province - can be one of ADR, AEG, ALB, ANK, APU, ARM, BAL, BAR, BEL, BER, BLA, BOH, BRE, BUD, BUL, BUR, \
        CLY, CON, DEN, EAS, ECH, EDI, FIN, GAL, GAS, GOB, GOL, GRE, HEL, HOL, ION, IRI, KIE, LON, LVN, LVP,\
        MAO, MAR, MOS, MUN, NAF, NAO, NAP, NTH, NWG, NWY, PAR, PIC, PIE, POR, PRU, ROM, RUH, RUM, SER,\
        SEV, SIL, SKA, SMY, SPA, STP, SWE, SYR, TRI, TUN, TUS, TYR, TYS, UKR, VEN, VIE, WAL, WAR, WES, YOR.\
        Coast - can be one of NCS, ECS, SCS, WCS.\
        Season and Phase - can be one of SPR, SUM, FAL, AUT , WIN.\
        Unit type - can be one of AMY, FLT.\
        hold looks like: (unit) HLD Hold\
        move looks like: (unit) MTO province Move\
        Support to hold look like: (unit) SUP (unit) \
        Support to move looks like: (unit) SUP (unit) MTO province \
        Convoy looks like: (unit) CVY (unit) CTO province \
        Move by convoy looks like: (unit) CTO province VIA (province province ...) \
        units are defined as (power type province)\n \
        Accept in DAIDE is YES\
        Reject in DAIDE is NOT\
        Ally in DAIDE is ALY \
        Here are some translation examples from English to DAIDE:\n \
        We both hate how I vs T just slows us both down, right?  Why do we have to be the slow powers in this game?  I say: we don't!  Let's be unconventional.  I have done fun I/T alliances before, but it all depends on making it work.  Let me know if you have any thoughts, or want to just see how the first few seasons roll out, or if there are things you'd like to see from me.\n PRP (ALY (TUR ITA))\n \
        Hi Italy, hope you're doing well. I'll be figuring out the situation north of me for the beginning stages so I hope we can keep Pie and Lyo/Wes/Tys  dmz'd if that's ok with you?\n PRP (DMZ (FRA ITA) (PIE LYO WES TYS))\n \
        Do you need help? I could build a fleet in Mar, maybe\n PRP ((FRA FLT MAR) BLD)\n"

def toDAIDE(eng_msg: str, temperature=0, top_p=1, frequency_penalty=0, presence_penalty=0) -> str:
    command = "Now translate the following from English to DAIDE: " + eng_msg

    response = openai.Completion.create(
        model="text-curie-001",
        prompt=text + command,
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()


def toEnglish(daide_msg: str, temperature=0, top_p=1, frequency_penalty=0, presence_penalty=0) -> str:
    command = "Now translate the following from DAIDE to English: " + daide_msg

    response = openai.Completion.create(
        model="text-curie-001",
        prompt=text + command,
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()

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
        Here are some translation examples from English to DAIDE:\n \
        [Russia to England] Can your army in Warsaw support my army in Ukraine?: PRP ((ENG AMY WAR) SUP (RUS AMY UKR))\n \
        [Germany to Austria] Can your fleet on the Baltic Sea support my army in Sweden?: PRP ((AUS FLT BAL) SUP (GER AMY SWE))\n \
        [France to Italy] Can your fleet in the Adriatic Sea convoy my army in Apulia to Trieste?: PRP ((ITL FLT ADR) CVY (FRA AMY APU) CTO TRI)\n"

# [Italy to Russia] Hi Russia, can your fleet in Warsaw support my army in Ukraine?


def toDAIDE(eng_msg: str) -> str:
    command = "Now translate the following from English to DAIDE: " + eng_msg

    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=text + command,
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()


def toEnglish(daide_msg: str) -> str:
    command = "Now translate the following from DAIDE to English: " + daide_msg

    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=text + command,
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()

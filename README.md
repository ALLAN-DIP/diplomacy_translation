# diplomacy_translation
To get the app working, you’ll need an API key. You can get one by [signing up](https://beta.openai.com/signup) for an account.
Note that OpenAI has a $18 free trial usage limit.

If you need to see how it works and play with it, you can check out the [demo](https://beta.openai.com/playground/p/sFjh0ESaFBAoftZlN0i00lHu?model=text-davinci-002). The following content is a Python API setup to use the model.
## Installation
```
git clone git@github.com:SiddarGu/diplomacy_translation.git
cd diplomacy_translation
pip install -r requirements.txt
pip install -e .
```
## Additional Setup
Create a `.env` file in the root directory of the project and add your API key to it:
```bash
OPENAI_API_KEY=YOUR_API_KEY
```

## Functions
```python
def toDAIDE(eng_msg: str, temperature=0, top_p=1, frequency_penalty=0, presence_penalty=0) -> str:
def toEnglish(daide_msg: str, temperature=0, top_p=1, frequency_penalty=0, presence_penalty=0) -> str:
```

## Usage
### Examples without changing hyperparameters
```python
from translation.translation import toDAIDE, toEnglish

daide_translation = toDAIDE("Can your army in Warsaw support my army in Ukraine?")
english_translation = toEnglish("PRP ((RUS FLT ION) CVY (TUR AMY TUN) CTO TRI)")
```
Each function also have some optional parameters, which can be used to change the hyperparameters of the translation.
- temperature (float): defaults to 1. Refers to what sampling temperature to use.
- top_p (float): defaults to 1. An alternative to sampling with temperature, called nucleus sampling.
- frequency_penalty (float between -2.0 and 2.0)
- presence_penalty=0 (float between -2.0 and 2.0)

See more info about these parameters [here](https://beta.openai.com/docs/api-reference/completions/create)
### Advanced usage
```python
daide_translation = toDAIDE("Can your army in Warsaw support my army in Ukraine?", temperature=0.5)
```

### Current limitations
- The dataset is too small. One annotation file from [here](https://github.com/isi-nlp/DiplomacyAMR/tree/main/annotations) has < 600 full DAIDEs. There is only four other files. In addition, most full DAIDEs annotated **does not** pass the current [daidepp parser](https://github.com/SHADE-AI/daidepp).
- The prompt is not always working as intended. Sometimes the model does not generate translations at all. Sometimes the model simply repeats (part of) the prompt. Sometimes the model generates a translation that is not related to the prompt at all. The details of the problems generating DAIDE from English can be found in comments in [utils.py](utils/utils.py).
- Third, using data from human games for generating DAIDE -> English translation is not ideal. The English reference does not always correspond to the DAIDE order. Discrepancy between translation and the reference is expected.

### Future work
- [ ] Prompt refinement
- [ ] Evaluation of the model
- [ ] Compare traditional NLP models with GPT-3
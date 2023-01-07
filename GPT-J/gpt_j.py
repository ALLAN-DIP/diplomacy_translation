from transformers import GPTJForCausalLM, AutoTokenizer, Trainer, TrainingArguments
import torch, os
import pandas as pd, numpy as np

os.environ['CUDA_VISIBLE_DEVICES'] ='0'

model = GPTJForCausalLM.from_pretrained("EleutherAI/gpt-j-6B").to('cuda')
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6B")
context = """In a shocking finding, scientists discovered a herd of unicorns living in a remote, 
            previously unexplored valley, in the Andes Mountains. Even more surprising to the 
            researchers was the fact that the unicorns spoke perfect English."""
input_ids = tokenizer.encode(context, return_tensors='pt').cuda()
# input_ids = tokenizer(context, return_tensors="pt").input_ids
gen_tokens = model.generate(input_ids, do_sample=True, temperature=0.9, max_length=100,)
gen_text = tokenizer.batch_decode(gen_tokens)[0]
print(gen_text)

# Constants
MODEL_NAME = 'EleutherAI/gpt-j-6B'
LEARNING_RATE = 0.0001
N_EPOCHS = 5
BATCH_SIZE = 16

# TODO: CSV file/pd for training data

class TranslationDataset(torch.utils.data.Dataset):
    def __init__(self, data: pd.DataFrame, tokenizer: AutoTokenizer):
        self.data = data
        self.tokenizer = tokenizer

    def __len__(self):
        return len(self.data.shape[0])

    def __getitem__(self, idx):
        data_row = self.data.iloc[idx]
        input_ids = self.tokenizer.encode(data_row['input'], return_tensors='pt').cuda()
        target_ids = self.tokenizer.encode(data_row['target'], return_tensors='pt').cuda()

        return input_ids, target_ids

def compute_metrics(eval_pred):
    # TODO
    pass

training_args = TrainingArguments(output_dir="test_trainer", evaluation_strategy="epoch")

trainer = Trainer(model=model,
    args=training_args,
    train_dataset=small_train_dataset,
    eval_dataset=small_eval_dataset,
    compute_metrics=compute_metrics)

def main():
    # TODO: Load data
    pass
    # trainer.train()

if __name__ == '__main__':
    main()
import transformers
import os
from transformers import AutoTokenizer, AutoModelForMaskedLM

print("Downloading HuggingFace model")
print("HF_ENDPOINT:", os.environ["HF_ENDPOINT"])
print("model_name:", os.environ["MODEL_NAME"])
print("revision:", os.environ["REVISION_ID"])
print(type(os.environ["REVISION_ID"]))

tokenizer = AutoTokenizer.from_pretrained(os.environ["MODEL_NAME"], 
                                    revision=os.environ["REVISION_ID"])

model = AutoModelForMaskedLM.from_pretrained(os.environ["MODEL_NAME"], 
                                    revision=os.environ["REVISION_ID"])

print("HuggingFace model downloaded")
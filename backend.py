from fastapi import FastAPI
from pydantic import BaseModel
from transformers import LlamaForConditionalGeneration, LlamaTokenizer

app = FastAPI()

# Load Llama3 model and tokenizer
llama_model = LlamaForConditionalGeneration.from_pretrained("llama3")
tokenizer = LlamaTokenizer.from_pretrained("llama3")

class TextInput(BaseModel):
    text: str

@app.post("/summarize")
async def summarize_text(text_input: TextInput):
    # Tokenize input text
    inputs = tokenizer(text_input.text, return_tensors="pt", max_length=1024, truncation=True, padding=True)

    # Generate summary
    summary_ids = llama_model.generate(inputs.input_ids, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)

    # Decode summary
    summarized_text = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return {"summary": summarized_text}

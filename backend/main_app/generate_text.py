from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForCausalLM



# def generate_text(prompt):
#     tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen3-8B")
#     model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen3-8B")
#     messages = [
#         {"role": "user", "content": "Who are you?"},
#     ]
#     inputs = tokenizer.apply_chat_template(
#         prompt,
#         add_generation_prompt=True,
#         tokenize=True,
#         return_dict=True,
#         return_tensors="pt",
#     ).to(model.device)

#     outputs = model.generate(**inputs, max_new_tokens=40)
#     return str(tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:]))




# pipe = pipeline("text-generation", model="openai-community/gpt2")

# tokenizer = AutoTokenizer.from_pretrained("openai-community/gpt2")

# model = AutoModelForCausalLM.from_pretrained("openai-community/gpt2")

# model.save_pretrained("my_model")

# tokenizer.save_pretrained("my_model")

# def generate_text(prompt):
#     model = AutoModelForCausalLM.from_pretrained("my_model")
#     tokenizer = AutoTokenizer.from_pretrained("my_model")

#     # prompt = "tell me a story"

#     inputs = tokenizer(prompt, return_tensors="pt")

#     outputs = model.generate(
#         **inputs,
#         max_new_tokens=50
#     )

#     return str(tokenizer.decode(outputs[0], skip_special_tokens=True))

def generate_text(prompt):
    return f"Hello there user, I will connect it to model later for the input\n{prompt}"

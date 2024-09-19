# Source: https://huggingface.co/meta-llama/Llama-Guard-3-8B

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "meta-llama/Llama-Guard-3-8B"
device = "cuda"
dtype = torch.bfloat16

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=dtype, device_map=device)

def moderate(chat):
    input_ids = tokenizer.apply_chat_template(chat, return_tensors="pt").to(device)
    output = model.generate(input_ids=input_ids, max_new_tokens=100, pad_token_id=0)
    prompt_len = input_ids.shape[-1]
    return tokenizer.decode(output[0][prompt_len:], skip_special_tokens=True)

import openai
import os

# Set up your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_gpt(messages):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=messages
        )
        return response.choices[0].message['content']
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    conversation_history = []
    print("Welcome to the OpenAI chatbot! Type 'quit' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break

        conversation_history.append({"role": "user", "content": user_input})
        
        print("Input Moderation: ", moderate(conversation_history))

        response = chat_with_gpt(conversation_history)
        print(f"AI: {response}")

        conversation_history.append({"role": "assistant", "content": response})
        
        print("Output Moderation: ", moderate(conversation_history))

if __name__ == "__main__":
    main()
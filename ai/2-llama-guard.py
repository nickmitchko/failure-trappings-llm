import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from openai import OpenAI
import os
import re

# Set up your OpenAI API key
# os.environ["OPENAI_API_KEY"] = "your-api-key"
# os.environ["OPENAI_API_BASE"] = "your-api-base-url"

# Define a dictionary of "S" tags and values
s_tags = {
    "S1": "Violent Crimes",
    "S2": "Non-Violent Crimes",
    "S3": "Sex-Related Crimes",
    "S4": "Child Sexual Exploitation",
    "S5": "Defamation",
    "S6": "Specialized Advice",
    "S7": "Privacy",
    "S8": "Intellectual Property",
    "S9": "Indiscriminate Weapons",
    "S10": "Hate",
    "S11": "Suicide & Self-Harm",
    "S12": "Sexual Content",
    "S13": "Elections",
    "S14": "Code Interpreter Abuse"
}

def replace_s_tag(value):
    if "unsafe" in value.lower():
        # Find the S\d{1,2} tag and replace it with its corresponding value
        def replace_tag(match):
            tag = match.group(0)
            return s_tags.get(tag, tag)
        
        return re.sub(r'S\d{1,2}', replace_tag, value)
    return value


# Load Llama-Guard model
@st.cache_resource
def load_moderation_model():
    model_id = "meta-llama/Llama-Guard-3-8B"
    device = "cuda" if torch.cuda.is_available() else "cpu"
    dtype = torch.bfloat16 if torch.cuda.is_available() else torch.float32

    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(
        model_id, torch_dtype=dtype, device_map=device
    )
    return tokenizer, model


tokenizer, model = load_moderation_model()


# Moderation function
def moderate(chat):
    input_ids = tokenizer.apply_chat_template(chat, return_tensors="pt").to(
        model.device
    )
    output = model.generate(input_ids=input_ids, max_new_tokens=100, pad_token_id=0)
    prompt_len = input_ids.shape[-1]
    return tokenizer.decode(output[0][prompt_len:], skip_special_tokens=True)


# Set up OpenAI client
client = OpenAI(base_url=os.getenv("OPENAI_API_BASE"))


# Get available models
@st.cache_data(ttl=3600)  # Cache for 1 hour
def get_available_models():
    return [model.id for model in client.models.list()]


# Chat function with streaming
def chat_with_gpt(messages, model_id):
    try:
        stream = client.chat.completions.create(
            model=model_id,
            messages=messages,
            stream=True,
        )
        return stream
    except Exception as e:
        return f"An error occurred: {str(e)}"


# Streamlit app
st.title("AI Chatbot with Content Moderation")

# Sidebar for model selection
available_models = get_available_models()
selected_model = st.sidebar.selectbox("Select a model", available_models)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is your message?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Moderate user input
    input_moderation = moderate(st.session_state.messages)
    st.write(f"<span style='color: {'green' if 'unsafe' not in input_moderation else 'red'};'>{replace_s_tag(input_moderation)}</span>",
        unsafe_allow_html=True,
    )

    # Get AI response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in chat_with_gpt(st.session_state.messages, selected_model):
            full_response += response.choices[0].delta.content or ""
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

    # Moderate AI output
    output_moderation = moderate(st.session_state.messages)
    st.write(f"<span style='color: {'green' if 'unsafe' not in output_moderation else 'red'};'>{replace_s_tag(output_moderation)}</span>",
        unsafe_allow_html=True,
    )

# Display the selected model in the sidebar
st.sidebar.write(f"Currently using: {selected_model}")

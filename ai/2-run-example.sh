#!/bin/bash

# Activate the virtual environment to ensure the correct Python version and dependencies are used
# This is necessary for the project to work correctly, as it relies on specific libraries and versions
source ./venv/bin/activate

# Export the CUDA_VISIBLE_DEVICES environment variable to specify which GPU to use
# This is necessary for models that require GPU acceleration, such as the LLaMA model
export CUDA_VISIBLE_DEVICES=0

# Set the HF_HOME environment variable to the directory where the Hugging Face model files are stored
# This is optional because the project uses Hugging Face models, which by default go to your ~/.cache directory
export HF_HOME=`pwd`/hf/

# Export the HF_TOKEN environment variable to authenticate with the Hugging Face API
# This is necessary to access certain Hugging Face models and features, such as llama-guard-8b
export HF_TOKEN="your_hf_token_here"

# Export the OPENAI_API_KEY environment variable to authenticate with the OpenAI API
# This is necessary because the project uses OpenAI features, such as the LLaMA model, and this variable tells the project which API key to use
export OPENAI_API_KEY="your_openai_api_key_here"

# Export the OPENAI_API_BASE environment variable to specify the base URL for the OpenAI API
# This is necessary because the project uses the OpenAI API, and this variable tells the project where to find it
# In this case, we're using a custom API endpoint, but you can replace this with the standard OpenAI API endpoint if you prefer
export OPENAI_API_BASE="http://10.0.95.11:23333/v1"

# Run the Streamlit app for the LLaMaGuard project
# This is the main entry point for the project, and it's what users will interact with
streamlit run 2-llama-guard.py

# Deactivate the virtual environment to clean up and prevent conflicts with other projects
deactivate
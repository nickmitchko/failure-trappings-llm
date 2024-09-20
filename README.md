# Failure Trappings LLM <div align="right">

This repository, `nickmitchko/failure-trappings-llm`, is a collection of examples demonstrating various approaches to content moderation and filtering for Large Language Models (LLMs). The project aims to showcase different techniques for ensuring safe and appropriate interactions with AI language models.

## Project Structure

The repository contains several Python scripts, each demonstrating a different approach to content moderation:

1. `ai/1-system-prompt.py`: Implements a system prompt for an AI language model, setting ethical guidelines and boundaries for interactions.
2. `ai/2-llama-guard.py`: Utilizes the Llama-Guard model for content moderation in a Streamlit-based chat application.
3. `statistical/1-rule-based.py`: Demonstrates a simple rule-based filtering approach.
4. `statistical/12-part-of-speech-tag.py`: Uses NLTK for part-of-speech tagging to filter content.
5. `statistical/15-human-in-the-loop.py`: Illustrates a human-in-the-loop approach for content moderation.

  <img src="https://github.com/user-attachments/assets/9da7d2ba-0628-4486-a4a6-76b6aadaa881" width="32" height="32" alt="00005-652596350">
</div>

## Getting Started

Follow these steps to set up and run the examples in this repository:

### Step 1: Clone the Repository

```bash
git clone https://github.com/nickmitchko/failure-trappings-llm.git
cd failure-trappings-llm
```

### Step 2: Create a Python Virtual Environment

Open a terminal in the project directory and run the following command to create a new virtual environment:

```bash
python -m venv venv
```

### Step 3: Activate the Virtual Environment

On Windows:
```powershell
venv\Scripts\activate
```

On macOS and Linux:
```bash
source venv/bin/activate
```

### Step 4: Install Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

### Step 5: Run an Example

Choose one of the Python scripts to run. For example:

```bash
python 1-system-prompt.py
```

Note, you must run 2-llama-guard.py as

```bash
streamlit run 2-llama-guard.py
```

## Examples Overview

1. **System Prompt (1-system-prompt.py)**: 
   Demonstrates how to use a system prompt to guide an AI language model's behavior and set ethical boundaries.

2. **Llama-Guard (2-llama-guard.py)**:
   A Streamlit application that uses the Llama-Guard model for content moderation in a chat interface.
    1. A full running example is provided in `ai/2-runexample.sh`

3. **Rule-Based Filtering (1-rule-based.py)**:
   Shows a simple rule-based approach to content filtering using predefined rules.

4. **Part-of-Speech Tagging (12-part-of-speech-tag.py)**:
   Uses NLTK to perform part-of-speech tagging for content filtering.

5. **Human-in-the-Loop (15-human-in-the-loop.py)**:
   Demonstrates how human input can be incorporated into the content moderation process.

## Contributing

Contributions to this project are welcome! Please feel free to submit a Pull Request.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Disclaimer

These examples are for educational purposes only. In production environments, more robust and thoroughly tested solutions should be implemented for content moderation and AI safety.

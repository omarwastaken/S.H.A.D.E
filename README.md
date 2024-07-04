# S.H.A.D.E. - Skight's Hacker AI-Driven Engine

Welcome to **S.H.A.D.E.**! This tool is designed to generate comprehensive password wordlists using AI by analyzing the victim's details. OSINT is obviously required for better results!
Follow this guide to set up, connect to an LLM API, and use the tool effectively.

## Table of Contents

1. [Installation Requirements](#installation-requirements)
2. [Connecting to an LLM API](#connecting-to-an-llm-api)
3. [Using S.H.A.D.E.](#using-shade)
4. [Features](#features)
5. [License](#license)

## Installation Requirements

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- OSINT on the victim

### Steps

1. **Clone the Repository**
    ```sh
    git clone https://github.com/omarwastaken/SHADE.git
    cd SHADE
    ```

2. **Install Required Packages**
    ```sh
    pip install -r requirements.txt
    ```

## Connecting to an LLM API

S.H.A.D.E. uses local models for generating passwords. However, it can also be configured to use the OpenAI API if preferred. Obviously the better the model, the better the results... You can always fine-tune or train your own model on actual big wordlists as well!

### Using Local Models (Recommended) (Free)

S.H.A.D.E. was primarily made and tested with local models. The software used was "LM Studio" with the model "Meta Llama 3 Instruct Q4_K_M".

- **Set Up Local LLM API**
    - Ensure you have your local model running and accessible at `http://localhost:1234/v1` or edit the code if you're using a different port and so on.

### Using OpenAI API (Optional) (Costs Money)

1. **Get API Key**
    - Sign up on the [OpenAI website](https://beta.openai.com/signup/).
    - Navigate to the API section to generate your API key.

2. **Set Up API Configuration**
    - Update the API key in your environment or directly in the code.

### Example Code Snippet

In the `prompt_api.py` file, make sure to replace `"your-api-key"` with your actual API key if you choose to use OpenAI, or if you are using a different port:
```python
client = OpenAI(base_url="http://localhost:1234/v1", api_key="your-api-key")
```

## Using S.H.A.D.E.

### Running the Tool

Execute the main script to start the tool:
```sh
python main.py
```

### User Input Prompts

1. **Enter Known Passwords**
    - Example: `password123 secret789..etc`
2. **Enter Details Related to Victim**
    - Example: `name, interests, favorite color, pet names, spouse names, sports team, favorite movie, astro sign, city born in...etc`
3. **Enter Numbers or Dates Related to Victim**
    - Example: `123456, birthdate, partner birthdate, pets birthdate, anniversaries..etc`
4. **Add Custom Generation Rules**
    - You can define custom rules for password generation.
    - Example: `Replace 'a' with '@', add '!' at the end`

5. **Number of Batches**
    - Specify how many batches of 30 passwords to generate (The more the merrier).

### Example Session

```
Please enter known passwords related to victim (space-separated, leave empty to skip): password123 secret789
Please enter details related to victim (comma-separated, leave empty to skip): name, birthdate, favorite color
Please enter numbers or dates related to victim (comma-separated, leave empty to skip): 123456, 01-01-1990
Would you like to add custom generation rules? (Y/N): Y
Describe the custom rules to apply: Replace 'a' with '@', add '!' at the end of every password
How many batches of ~30 passwords do you want to generate? 3
```

## Features

### Custom Rules for Password Generation

1. **Character Substitutions**
    - Replace specific characters with other characters or symbols (e.g., 'a' with '@').
2. **Character Appending/Prepending**
    - Add specific characters or symbols to the beginning or end of each password.
3. **Case Toggling**
    - Toggle the case of letters in various patterns.
4. **Pattern Insertion**
    - Insert characters or strings at specified intervals.
5. **Length Constraints**
    - Enforce minimum and maximum length requirements for the passwords.

### Example Custom Rule

```
Replace 'a' with '@', add '!' at the end
```

## License

S.H.A.D.E © 2024 by Omar Badawy is licensed under CC BY-NC 4.0. See the `LICENSE` file for details.

---

# DISCLAIMER
### This tool is intended for ethical purposes only. Please be aware that using it for any illegal activity is strictly prohibited and at your own risk. I take no responsibility for any misuse of this project.

Thank you for using S.H.A.D.E.! I hope it enhances your cybersecurity testing and ethical hacking efforts. Contributions are welcome! If you have any questions or need further assistance, feel free to reach out.

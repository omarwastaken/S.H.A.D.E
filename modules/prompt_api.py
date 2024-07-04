# ============= Imports =============
from openai import OpenAI
from modules.visuals import start_thinking_animation, stop_thinking_animation

# ============= Prompt Generation =============
def generate_combined_prompt(details, numbers, known_passwords, custom_rules):
    # Generate a combined prompt based on user input
    prompt = "Generate 30 passwords. Each password should be on a new line. You MUST output only passwords and say nothing else! Don't number count the passwords! You are essentially making a password wordlist. Passwords are for someone with the following information:\n"
    if known_passwords:
        prompt += f"Known Passwords to stay close to: {known_passwords}\n"
    if details:
        prompt += f"Details about victim: {details}\n"
    if numbers:
        prompt += f"Important Numbers or Dates: {numbers}\n"
    if custom_rules:
        prompt += f"Custom Password Rules: {custom_rules}\n"
    return prompt

# ============= Password Generation =============
def generate_password_batches(combined_prompt, batches_input):
    # Initialize the LM Studio client
    client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
    all_passwords = []

    for batch in range(batches_input):
        batch_number = batch + 1
        message = f"Generating Batch {batch_number}: Thinking"
        
        # Start the thinking animation
        anim_thread = start_thinking_animation(message)

        # Generate passwords using the LM Studio API
        completion = client.chat.completions.create(
            model="lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF",
            messages=[
                {"role": "system", "content": "You're an expert psychologist and master Ethical Hacker with a major in Password cracking. Your job is to analyze a victim's details and try to guess their password."},
                {"role": "user", "content": combined_prompt}
            ],
            temperature=0.7,
            max_tokens=-1
        )

        # Stop the thinking animation
        stop_thinking_animation(anim_thread, message, batch_number)

        # Process the response and add it to the list of all passwords
        passwords = completion.choices[0].message.content
        all_passwords.extend(passwords.splitlines())
    
    return all_passwords

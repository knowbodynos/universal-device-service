import os

import openai


def generate_text(
    keywords,
    task,
    max_iterations=5,
    model_name="gpt-3.5-turbo-instruct",
    temperature=0.2,
):
    """
    Generates a set of instructions for completing a task using a device or appliance described by the given keywords.
    """
    # Define the prompt
    prompt = f"""You are a helpful and knowledgeable technical support assistant.
    Given a device or appliance described by the following keywords: \"{', '.join(keywords)}\", and a task defined by: \"{task}\", please provide a short and concise set of numbered instructions for completing the task using the device or appliance. Your output should end with the tag "</END>".

    Begin your response here:
    """
    output = ""

    for _ in range(max_iterations):
        response = openai.Completion.create(
            api_key=os.getenv("OPENAI_API_KEY"),
            model=model_name,
            prompt=prompt + output,
            temperature=temperature,
            stop="</END>",
            max_tokens=150,  # Set a reasonable max token count per iteration
        )

        # Append the new output to our output string
        output += response.choices[0].text.strip()

        # Check if the response contains the </END> tag
        if "</END>" in output:
            break

        return output

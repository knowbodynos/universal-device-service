import os

import gradio as gr

from image import get_image_url
from generate import generate_text
from search import get_search_keywords


def process_inputs(img_filepath, task_text):
    img_url = get_image_url(img_filepath, expiration=60)
    keywords = get_search_keywords(img_url)
    output_text = generate_text(
        keywords,
        task_text,
        max_iterations=5,
        model_name="gpt-3.5-turbo-instruct",
        temperature=0.2,
    )
    return ', '.join(keywords), output_text


def dynamic_interface(source_choice):
    assert source_choice in ["webcam", "upload"]
    return 


if __name__ == "__main__":
    # Define the Gradio interface
    iface = gr.Interface(
        fn=process_inputs,  # function to be called on button press
        inputs=[
            gr.Image(
                label="Upload an Image of Device or Appliance",
                type="filepath",
                source="upload",
                tool="select",
            ),  # Image upload field
            gr.Textbox(label="Describe Task"),  # Input text field
        ],
        outputs=[
            gr.Textbox(label="Product Keywords"),  # Output text field
            gr.Textbox(label="Instructions"),  # Output text field
        ],
        examples=[
            [
                os.getenv("DEFAULT_IMAGE"),
                "Set a 6am timer to warm up to 72 degrees",
            ]
        ],
        live=False,  # The processing function is only called when the submit button is pressed
        allow_flagging="never",
    )

    # Launch the app
    iface.launch(server_name="0.0.0.0", server_port=80)

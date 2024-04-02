import marimo

__generated_with = "0.3.4"
app = marimo.App()


@app.cell
def __():
    import os
    import marimo as mo
    import google.generativeai as ggenai

    # Configure API key
    ggenai.configure(api_key=os.environ["GEMINI_KEY"])
    return ggenai, mo, os


@app.cell
def __(ggenai):
    # Set template model configurations
    template_config = ggenai.GenerationConfig(
        # candidate_count=2,
        temperature=0.4,
        top_k=10,
    )

    # Initialize the template model
    template_model = ggenai.GenerativeModel(
        model_name="gemini-1.0-pro",
        generation_config=template_config
    )
    return template_config, template_model


@app.cell
def __():
    content_type = "marketing"
    context = \
    """\
    At Mahendra Cars, we are introducing a new model of Thar (jeep type) car with model no. A52. Create a promotional message details it's features like compelling performance, 50 mile mileage, top safety rating, etc. Include interaction buttons: [Get Quote, Book Now].
    """
    return content_type, context


@app.cell
def __(content_type, context):
    template_prompt = \
    f"""\
    You are an expert content writer who writes content for purposes of creating interactive chatbot and for marketing. You task is to write whatsapp {content_type} content based on the context enclosed withing double quotes. Include interactive buttons the user could interact with by clicking.

    "{context}"

    Structure the output in JSON format based on the below template. The template is a JSON obejct describe the key and the type of value contained in each key.

    Template:
    {{
        header: string, 
        message: string, 
        buttons: array[string], 
        footer: string 
    }}

    Limit the header to 60 characters, message to 1024 charaters and footer to 60 characters. You can also include emojis, but only in the header and message.

    Refer the examples below for the idea:

    Examples:
    Context: We are AskEVA, a software company. We are moving towards our phase 2 launch. Create a descriptive marketing message inviting them to a demo session. Add the following buttons: Book a demo, Enquire us, Contact us.

    Response: 
    {{
        "header": "Introducing AskEVA: Your Software Solution Partner",
        "message": "Greetings! \n\nWe are thrilled to announce that AskEVA, a leading software company, is moving towards its phase 2 launch. We invite you to join us for an exclusive demo session to experience firsthand how our innovative solutions can empower your business.\n\nOur team of experts will guide you through our cutting-edge software, showcasing its capabilities and how it can transform your operations. Whether you're looking to streamline processes, enhance productivity, or gain a competitive edge, AskEVA has the solution for you.\n\nDon't miss this opportunity to discover the future of software. Book your demo today and let us help you unlock the full potential of your business.",
        "buttons": [
            "Book a demo",
            "Enquire us",
            "Contact us"
        ],
        "footer": "We look forward to connecting with you and shaping the future of software together."
    }}
    """
    return template_prompt,


@app.cell
def __(template_model, template_prompt):
    template_response = template_model.generate_content(template_prompt)
    return template_response,


@app.cell
def __(template_response):
    template_response.candidates[0].content.parts[0].text
    return


@app.cell
def __(template_response):
    template_content = template_response.candidates[0].content.parts[0].text
    return template_content,


@app.cell
def __(ggenai):
    # Set template model configurations
    interactive_config = ggenai.GenerationConfig(
        # candidate_count=2,
        temperature=0.6,
        top_k=30,
    )

    # Initialize the template model
    interactive_model = ggenai.GenerativeModel(
        model_name="gemini-1.0-pro",
        generation_config=interactive_config
    )
    return interactive_config, interactive_model


@app.cell
def __(content_type):
    interative_prompt = \
    f"""\
    You are an expert content writer who writes content for purposes of creating interactive chatbot and for marketing. Below is a {content_type} content written by you in JSON format.

    Content:
    {{
        "header": "Introducing AskEVA: Your Software Solution Partner",
        "message": "Greetings! \n\nWe are thrilled to announce that AskEVA, a leading software company, is moving towards its phase 2 launch. We invite you to join us for an exclusive demo session to experience firsthand how our innovative solutions can empower your business.\n\nOur team of experts will guide you through our cutting-edge software, showcasing its capabilities and how it can transform your operations. Whether you're looking to streamline processes, enhance productivity, or gain a competitive edge, AskEVA has the solution for you.\n\nDon't miss this opportunity to discover the future of software. Book your demo today and let us help you unlock the full potential of your business.",
        "buttons": [
            "Book a demo",
            "Enquire us",
            "Contact us"
        ],
        "footer": "We look forward to connecting with you and shaping the future of software together."
    }}

    The `buttons` is an array of quick reply options the user can interact with. Generate a follow up content for each of the quick reply options. The follow up message can include more action buttons the user can interact with. Include buttons only when necessary. Avoid duplicating/nesting the buttons. Format output in JSON based on the below template and limit the header to 60 characters, message to 1024 charaters and footer to 60 characters. The template is a JSON obejct describe the key and the type of value contained in each key.

    Template:
    {{
        button_1: {{
            header: string, 
            message: string, 
            buttons: array[string], 
            footer: string
        }},
        button_2: {{
            header: string, 
            message: string, 
            buttons: array[string], 
            footer: string
        }}
    }}
    """
    return interative_prompt,


@app.cell
def __(interactive_model, interative_prompt):
    interactive_response = interactive_model.generate_content(interative_prompt)
    return interactive_response,


@app.cell
def __(interactive_response):
    interactive_response.candidates[0].content.parts[0].text
    return


if __name__ == "__main__":
    app.run()

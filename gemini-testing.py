import marimo

__generated_with = "0.3.4"
app = marimo.App()


@app.cell
def __():
    import os
    import google.generativeai as ggenai

    # Configure API key
    ggenai.configure(api_key=os.environ["GEMINI_KEY"])
    return ggenai, os


@app.cell
def __(ggenai):
    # Set model configurations
    generation_config = ggenai.GenerationConfig(
        temperature=0.4,
        top_k=10,
    )

    # Initialize the model
    model = ggenai.GenerativeModel(
        model_name="gemini-1.0-pro",
        generation_config=generation_config
    )
    return generation_config, model


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
    prompt = \
    f"""\
    You are an expert content writer who writes content for purposes of creating interactive web pages and for marketing. You task is to write whatsapp {content_type} content based on the context enclosed withing double quotes. Include call to action options or buttons the user could interact with by clicking, so that when clicked it proceeds to direct converstion accordingly.

    "{context}"

    Structure the output in JSON format based on the below template. The template is a JSON obejct describe the key and the type of value contained in each key.

    Template:
    {{
        header: string, 
        message: string, 
        buttons: array[string], 
        footer: string 
    }}

    Limit the header to 60 characters, message to 1024 charaters and footer to 60 characters.

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
    return prompt,


@app.cell
def __(model, prompt):
    response = model.generate_content(prompt)
    return response,


@app.cell
def __(response):
    response.candidates[0].content.parts[0].text
    return


if __name__ == "__main__":
    app.run()

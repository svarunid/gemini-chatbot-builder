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
        temperature=0.7,
        top_k=20,
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
    AskEVA is preparing for it's phase 2 launch. It is a whatsapp API based messaging and marketing platform serving various use-cases across industries like E-commerce, Automobiles, Food & Beverages, etc. The version 2 brings in new features like chatbot builder, flow builder etc. Create content to promote the launch among the potential custormers.
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

    Limit the header and footer to 60 characters, message to 1024 charaters and button to one or two words. You can also include emojis, but only in the header and message.

    Refer the examples below for the idea:

    Examples:
    Context: At Mahendra Cars, we are introducing a new model of Thar (jeep type) car with model no. A52. Create a promotional message details it's features like compelling performance, 50 mile mileage, top safety rating, etc. Include interaction buttons: [Get Quote, Book Now].

    Response: 
    {{
        "header": "Introducing the All-New Mahindra Thar A52: Unleash Your Adventure",
        "message": "Get ready to conquer any terrain with the latest addition to our fleet – the Mahindra Thar A52. This rugged beast is engineered to deliver an unparalleled driving experience with its:

    💪 Compelling performance that will leave you craving for more
    ⛽️ Impressive 50-mile mileage, ensuring you go the distance
    🛡️ Top safety rating, giving you peace of mind on every journey
    ⛰️ Unmatched off-road capabilities, ready to tackle any challenge

    Whether you're a seasoned adventurer or a weekend explorer, the Thar A52 is the perfect companion for your next escapade. Don't wait, embrace the thrill today!",
        "buttons": [
            "Get Quote",
            "Book Now"
        ],
        "footer": "Mahendra Cars: Driving Adventure Since 1945"
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
        temperature=0.7,
        top_k=25,
    )

    # Initialize the template model
    interactive_model = ggenai.GenerativeModel(
        model_name="gemini-1.0-pro",
        generation_config=interactive_config
    )
    return interactive_config, interactive_model


@app.cell
def __(content_type, template_content):
    interative_prompt = \
    f"""\
    You are an expert content writer who writes content for purposes of creating interactive chatbot and for marketing. Below is a {content_type} content written by you in JSON format.

    Content:
    {template_content}

    The `buttons` is an array of quick reply options the user can interact with. Generate a follow up content for each of the quick reply options. The follow up message can include more action buttons the user can interact with or to collect user information.

    Format output in JSON based on the below template. Limit the header and footer to 60 characters, message to 1024 charaters and button to one or two words. You can also include emojis, but only in the header and message. The template is a JSON obejct describe the key and the type of value contained in each key.

    Template:
    {{
        button 1: {{
            header: string, 
            message: string, 
            buttons: array[string], 
            footer: string
        }},
        button 2: {{
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

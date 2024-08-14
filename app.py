import streamlit as st
import os
from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel(model_name="gemini-1.5-flash")


def get_gemini_response(input_text, image_data, prompt):
    response = model.generate_content([input_text, image_data, prompt])
    return response.text


def input_image_details(uploaded_image):
    if uploaded_image:
        bytes_data = uploaded_image.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_image.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")


st.set_page_config(page_title="Multilanguage Invoice Parser")

st.header("Multilanguage Invoice Parser")
input_text = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image of the invoice...", type=["jpg", "jpeg", "png"])
image_data = None
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded image", use_column_width=True)
    image_data = input_image_details(uploaded_file)

submit = st.button("Tell me about image")

input_prompt = """
               You are an expert in understanding invoices.
               You will receive input images as invoices &
               you will have to answer questions based on the input image
               """

if submit:
    if image_data:
        response = get_gemini_response(input_text, image_data[0], input_prompt)
        st.subheader("The Response is")
        st.write(response)

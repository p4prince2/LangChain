import streamlit as st
from PIL import Image
import help 


st.set_page_config(page_title="Multimodal Chat", page_icon="🤖")

st.title(" Multimodal Chat")

# -------------------------
# User Inputs
# -------------------------
text_input = st.text_area(
    "Enter your question (Optional)",
    placeholder="Ask something..."
)

uploaded_image = st.file_uploader(
    "Upload an image (Optional)",
    type=["png", "jpg", "jpeg"]
)

image = None

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", width="stretch")

# -------------------------
# Submit Button
# -------------------------
if st.button("Submit"):

    # Check if at least one input is provided
    if not text_input and image is None:
        st.warning("Please provide either a text question or an image.")
        st.stop()

    # -------------------------
    # Case 1 : Text + Image
    # -------------------------
    if text_input and image is not None:
        st.success("Received both Text and Image")

        # Replace this with your model
        response = f"""
        Text:
        {text_input}

        Image received successfully.

        (Call your VLM here.)
        """

    # -------------------------
    # Case 2 : Only Text
    # -------------------------
    elif text_input:
        st.success("Received only Text")

        # Replace this with your LLM
        response = help.inital_step(text_input)

    # -------------------------
    # Case 3 : Only Image
    # -------------------------
    else:
        st.success("Received only Image")

        # Replace this with your Vision Model
        
        import tempfile

        if uploaded_image is not None:

            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
                tmp.write(uploaded_image.getbuffer())
                temp_path = tmp.name

            response = help.image_input(temp_path)



    st.subheader("Response")
    st.write(response)
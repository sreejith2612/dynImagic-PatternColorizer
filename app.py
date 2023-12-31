import streamlit as st
from PIL import Image
import numpy as np

def apply_color_filter(image, color):
    # Apply a color filter to the image
    img_np = np.array(image)
    
    if color == 'Red':
        img_np[:,:,1] = 0
        img_np[:,:,2] = 0
    elif color == 'Green':
        img_np[:,:,0] = 0
        img_np[:,:,2] = 0
    elif color == 'Blue':
        img_np[:,:,0] = 0
        img_np[:,:,1] = 0
    
    return Image.fromarray(img_np)

def main():
    st.title('Generate patterns')
    
    uploaded_files = st.file_uploader("Upload your images", accept_multiple_files=True)
    
    if uploaded_files:
        st.sidebar.title('Filters')
        color = st.sidebar.selectbox('Select a color', ['Red', 'Green', 'Blue'])
        generate_button = st.sidebar.button('Generate')
        
        if generate_button:
            for uploaded_file in uploaded_files:
                image = Image.open(uploaded_file)
                filtered_image = apply_color_filter(image, color)
                st.image(filtered_image, caption=f'{color} Filtered Image', use_column_width=True)

if __name__ == "__main__":
    main()

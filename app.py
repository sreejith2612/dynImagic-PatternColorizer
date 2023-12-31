import streamlit as st
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def major_colors(image, num_colors=5):
    # Get the major colors from the image
    img_np = np.array(image)
    img_np = img_np.reshape((-1, 3))

    # Get the colors using k-means clustering
    from sklearn.cluster import KMeans
    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(img_np)

    colors = kmeans.cluster_centers_.astype(int)
    colors = [tuple(color) for color in colors]

    return colors

def main():
    st.title('Image Color Pattern App')
    
    uploaded_pattern = st.file_uploader("Upload the pattern image", type=['jpg', 'png'])
    uploaded_image = st.file_uploader("Upload the main image", type=['jpg', 'png'])
    
    if uploaded_pattern and uploaded_image:
        pattern = Image.open(uploaded_pattern)
        image = Image.open(uploaded_image)
        
        colors = major_colors(image)
        st.sidebar.title('Filters')
        selected_color = st.sidebar.selectbox('Select a color', colors, format_func=lambda x: f'Color: {x}', index=0)
        
        # Display the thumbnails of colors
        st.sidebar.markdown('**Color Thumbnails**')
        for color in colors:
            color_img = np.full((100, 100, 3), color, dtype=np.uint8)
            st.sidebar.image(Image.fromarray(color_img), caption=f'Color: {color}', width=100)
        
        generate_button = st.sidebar.button('Generate')
        
        if generate_button:
            st.image(pattern, caption='Pattern Image', use_column_width=True)
            st.image(image, caption='Main Image', use_column_width=True)
            
            st.write(f'Selected Color: {selected_color}')

if __name__ == "__main__":
    main()

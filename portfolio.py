# Sushil K Sharma 
# sushilsharma71@gmail.com
#
# Project Portfolio Site
import streamlit as st
from PIL import Image
import requests
from io import BytesIO
from PIL import Image

# Function to load and resize images from the local folder
def load_image(filename, size=(300, 200)):
    img = Image.open(f"./images/{filename}")
    img = img.resize(size)
    return img

# Function to load images from the web
def load_web_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img

# Load profile image
profile_image = load_image("ss.jpg", size=(150, 150))

# Load project images
project1_image_url = "https://via.placeholder.com/300x200"  # Replace with actual URL
project1_image = load_web_image(project1_image_url)

project2_image_url = "https://via.placeholder.com/300x200"  # Replace with actual URL
project2_image = load_web_image(project2_image_url)

project3_image_url = "https://via.placeholder.com/300x200"  # Replace with actual URL
project3_image = load_web_image(project3_image_url)

project4_image_url = "https://via.placeholder.com/300x200"  # Replace with actual URL
project4_image = load_web_image(project4_image_url)

# Title and Introduction
st.title("AI / Data Science Project Portfolio")
st.image(profile_image, width=150)
st.write("## Sushil K Sharma, MSCSE, MBA Analytics")
st.write("""
""")

# Sidebar - Navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ["About Me", "Skills", "Projects", "Contact"])

st.sidebar.write("Email: sushilsharma71@gmail.com")

# About Me Section
if options == "About Me":
    st.write("## About Me")
    st.write("""
    As a Sr Staff Data Scientist at Carbon, a cutting-edge 3D printing solution company backed by big VCs such as Alphabet and Sequoia Capital, I apply my passion and expertise in machine learning, deep learning, and natural language processing to create innovative and impactful products. With over 10 years of experience in data science and analytics, I have a proven track record of delivering high-quality solutions that meet the needs and expectations of clients and stakeholders.

    I have hands-on experience in using Python, R, TensorFlow, PyTorch, AWS, Google Cloud, and other technologies to perform data munging, supervised and unsupervised learning, deep machine learning, and NLP tasks. I also have a strong background in Chatbot building using OpenAI, LLAMA2, and Google LLMs, RAG, Fine Tuning, Prompt Engineering, business intelligence, data warehousing, ETL, and reporting, using tools such as Tableau, SQL, SSIS, and Excel. Additionally, I have certifications in project management, scrum, and agile methodologies, which enable me to lead, manage, and collaborate effectively with cross-functional teams. I am always eager to learn new skills, explore new domains, and take on new challenges.

    With 10+ years of exeperince, I specialize in developing Generative AI / ML models that solve complex problems.
    """)

    st.write("""
    ## Education:
    - *MS in Computer Systems & Engineering from California Science and Technology University, Milpitas, CA* [www.cstu.edu](https://cstu.edu)            
    - *MBA in Analytics and Technoglogy Management from Graduate School of Management at University of California, Davis, CA* [gsm.ucdavis.edu](https://gsm.ucdavis.edu/)
    """)

# Skills Section
elif options == "Skills":
    st.write("## Skills")
    st.write("""
    **Programming Languages:** Python, R, SQL, JavaScript  
    **Machine Learning:** Scikit-Learn, TensorFlow, PyTorch, Keras  
    **Data Analysis:** Pandas, NumPy, Matplotlib, Seaborn  
    **Tools:** Jupyter Notebooks, Git, Docker, Kubernetes  
    **Others:** Data Visualization, Big Data, Cloud Computing (AWS, GCP)
    """)

# Projects Section
elif options == "Projects":
    st.write("## Projects")
    
    # Project 1
    st.write("### Project 1: Customer Segmentation")
    st.image(project1_image, caption="Customer Segmentation", use_column_width=True)
    st.write("""
    **Description:** Developed a customer segmentation model for a retail company to enhance their marketing strategies.
    **Technologies Used:** Python, Scikit-Learn, Pandas, Matplotlib
    """)
    
    # Project 2
    st.write("### Project 2: Predictive Maintenance")
    st.image(project2_image, caption="Predictive Maintenance", use_column_width=True)
    st.write("""
    **Description:** Created a predictive maintenance system for manufacturing equipment to reduce downtime.
    **Technologies Used:** Python, TensorFlow, Keras, SQL
    """)
    
    # Project 3
    st.write("### Project 3: Fraud Detection System")
    st.image(project3_image, caption="Fraud Detection System", use_column_width=True)
    st.write("""
    **Description:** Implemented a real-time fraud detection system for a financial institution.
    **Technologies Used:** Python, PyTorch, Pandas, NumPy
    """)

    # Project 4
    st.write("### Project 4: Customer Support RAG")
    st.image(project4_image, caption="Customer Support RAG", use_column_width=True)
    st.write("""
    **Description:** Implemented a Customer Support Retrival Augmeneted Generation system for Customer Success Team at a Technology Company  **Technologies Used:** Python, PyTorch, Pandas, NumPy
    """)
     
    # Add more projects as needed

# Contact Section
elif options == "Contact":
    st.write("## Contact")
    st.write("""
    Feel free to reach out to me through the following channels:
    - **Email:** sushilsharma71@gmail.com
    - **LinkedIn:** [linkedin.com/in/krishnatray](https://linkedin.com/in/krishnatray)
    - **GitHub:** [github.com/krishnatray](https://github.com/krishnatray)
    """)

# # Run the Streamlit app
# if __name__ == "__main__":
#     st.run()

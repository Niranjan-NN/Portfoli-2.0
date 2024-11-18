import streamlit as st

# Title of the Portfolio
st.title('👋 Niranjan NN - Portfolio')

# About Section
st.header('👨‍💻 About Me')
st.write("""
    Hi! I'm Niranjan NN, a passionate **Data Scientist** and **Full-Stack Developer**. I enjoy solving problems and building innovative solutions using **data science** and **web development** technologies.
    
    My journey started in **data science** 📊 and **web development** 💻, and I am constantly exploring new techniques and tools to enhance my skills. I have a strong background in **machine learning** 🤖, **full-stack development** 🌐, and **data engineering** 🔧.
""")

# Skills Section
st.header('🛠️ Skills')
st.write("""
- **Languages:** Python 🐍, JavaScript 🌐, TypeScript 🔵, SQL 🗄️
- **Web Development:** React.js ⚛️, Next.js 🚀, HTML 🖥️, CSS 🎨, Tailwind CSS 💨
- **Data Science:** Pandas 📊, Numpy 🔢, Scikit-learn 📉, Matplotlib 📈
- **Databases:** MySQL 🗄️, MongoDB 🌳
- **Tools:** Streamlit 🚀, Docker 🐳, Git 💻, VS Code 🧑‍💻
""")

# Projects Section
st.header('📚 Projects')

# Add Projects with descriptions and links
st.subheader('🛒 Smart Ration')
st.write("""
    Smart Ration is an app built using **MIT App Inventor** that allows users to book time slots at ration shops to avoid long queues.
    [View Project](#)
""")

st.subheader('🏨 FieastaIndiana')
st.write("""
    FieastaIndiana is a tourism website built with **HTML**, **CSS**, **JavaScript**, and **Firebase** that helps users book hotels, tourist guides, food, and other services.
    [View Project](#)
""")

st.subheader('💬 InnerPeaceAI')
st.write("""
    InnerPeaceAI is a chatbot built using **React.js**, **Dialogflow**, and **MongoDB** designed to help users reduce stress and manage anxiety.
    [View Project](#)
""")

st.subheader('🖼️ Aara')
st.write("""
    Aara is an image recognition chatbot built with **machine learning**, **Python**, **React.js**, and **MongoDB** that recognizes images and provides related prompts.
    [View Project](#)
""")

# Contact Section
st.header('📞 Contact')
st.write("""
Feel free to reach out to me if you'd like to collaborate or have any questions!

- **Phone.No:** +91 99444-56377 📞         
- **Email:** niranjan87901@gmail.com 📧
- **LinkedIn:** [linkedin.com/in/niranjan](https://www.linkedin.com/in/niranjan-nn/) 🔗
""")

# Run the Streamlit app

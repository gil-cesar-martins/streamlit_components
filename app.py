# Core Pkg
import streamlit as st

# Components
import streamlit.components.v1 as stc

# Matplotlib
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('Agg')

from wordcloud import WordCloud

def plot_worldcloud(mytext):
  my_wordcloud = WordCloud().generate(mytext)
  fig = plt.figure()
  plt.imshow(my_wordcloud, interpolation='bilinear')
  plt.axis('off')
  st.pyplot(fig)

def main():
    st.title("Streamlit Static Components")

    stc.html("""
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
</head>
<body>
    <div class="container-fluid p-5 bg-primary text-white text-center">
      <h1>Usando Bootstrap no Streamlit</h1>
      <p>Podemos alterar o estilo de nossas páginas.</p> 
    </div>
    
</body>
</html>
""")
    
    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice == "Home":
        st.subheader("Home")
        fname = st.text_input("Primeiro nome")
        occupations = st.multiselect("Ocupações", ["Programmer", "Data Scientist", "Doctor", "Engineer"])
        message = st.text_area("Mensagem")
        if st.button("Submit"):
          st.write("Bem-vindo(a), {}!".format(fname))
          st.write("You selected the following {} occupations: {}".format(len(occupations), ", ".join(occupations)))
          st.write(message)
          st.success("Enviado")
    
        col1, col2 = st.columns(2)
        with col1:
          with st.expander("Primeiro"):
            st.info("Eu tô amando a Streamlit")
            st.write(message)
            my_dict = {"fname":fname, "message":message}
            st.json(my_dict)
        
        with col2:
          with st.expander("Segundo"):
            st.warning("Aviso! Isso vai bombar 🤖")
            st.success("Muita gente deve conhecer isso")
            st.info("Vou estudar o máximo para aprender mais.")
            
        with st.expander("Exibir a nuvem de palavras"):
          try:
            plot_worldcloud(message)
          except:
            st.warning("Dados insuficientes: precisam ser mais de 2 palavras.")
    
    elif choice == "About":
      st.subheader("💻 Sobre o app 🎈")
      st.text("Este app foi desenvolvido com Streamlit no intuito de mostrar algumas funcionalidades desse framework.")
    
if __name__ == '__main__':
    main()




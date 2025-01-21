from dashboard_comp.abstract_component import AbstractComponent
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

class EDAComponent(AbstractComponent):
    
    def render(self):
        st.header("Exploratory Data Analysis")
        st.info(
            "In this section, you are invited to create insightful graphs "
            "about the resume dataset that you were provided."
        )

        file_path = r"C:\Users\Abdelrahman Essam\ML-Internship-Home-Assignment-main\data\raw\resume.csv"
        resume_df = pd.read_csv(file_path)
        resume_df['Words Per Resume'] = resume_df['resume'].str.split().apply(len)


        label_freq = (
            resume_df['label'].value_counts(ascending=True).reset_index()#shows the frequancy of each label in our data
            )
        fig_bar = px.bar(data_frame = label_freq ,
                          x = 'label' , 
                          y = 'count' , 
                          color = 'count',
                          title= "The frequancy of each label in the data",
                          labels={'label': 'Label', 'count': 'Frequancy'}
                          )
        
        comment_words = ''
        stopwords = set(STOPWORDS)
        
        # iterate through the csv file
        for val in resume_df.resume:
            
            # typecaste each val to string
            val = str(val)
        
            # split the value
            tokens = val.split()
            
            # Converts each token into lowercase
            for i in range(len(tokens)):
                tokens[i] = tokens[i].lower()
            
            comment_words += " ".join(tokens)+" "
        
        wordcloud = WordCloud(width = 800, height = 800,
                        background_color ='white',
                        stopwords = stopwords,
                        min_font_size = 10).generate(comment_words)
        
        # plot the WordCloud image                       
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.imshow(wordcloud, interpolation="bilinear")
        ax.axis("off")  # Remove axes
        ax.set_title("WordCloud of Resume Texts", fontsize=16)
        plt.tight_layout()


        fig_words = px.histogram( #Visualize the distribution of the number of words per resume.
            resume_df,
            x="Words Per Resume",
            nbins=30,
            title="Distribution of Words Per Resume",
            labels={"Words Per Resume": "Words Per Resume"}
        )

        fig_violin = px.violin( #Similar to the box plot but also shows the density distribution for "Words Per Resume" grouped by labels.
            resume_df,
            x="label",
            y="Words Per Resume",
            color="label",
            box=True,
            title="Violin Plot: Words Per Resume by Label"
        )

        # Display the WordCloud in Streamlit
        st.pyplot(fig)
        # Display the barchart in Streamlit
        st.plotly_chart(fig_bar)
        # Display the distribution of the number of words per resume
        st.plotly_chart(fig_words)
        #Display the violin in Streamli
        st.plotly_chart(fig_violin)
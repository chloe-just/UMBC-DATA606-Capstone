# The Template and Guideline for the Final Report

- This document serves as a guide for developing project proposal which will eventually become the proposal and final report.
- You start with the end in mind and adopt an agile approach:
  - Making progress continuously towards your goal.
  - Updating this document continuously along the way.
 
## 1. Title and Author

- Project Title: A Personalized Book Recommendation System Using Machine Learning and NLP
- Prepared for UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang
- Chloe Just 
- GitHub: https://github.com/chloe-just/UMBC-DATA606-Capstone/tree/main
- LinkedIn: https://www.linkedin.com/in/chloe-just-510377124/
- Link to your PowerPoint presentation file
- Link to your YouTube video 
    
## 2. Background

Provide the background information about the chosen topic. 

- What is it about?
  -This project focuses on building a personalized book recommendation system using machine learning and natural language processing (NLP). The system will analyze book metadata and textual information, such as book descriptions, genres, and reader ratings, to recommend similar books to users based on their interests. The project will primarily focus on fantasy and indie books, allowing readers to discover titles that match their reading preferences.
  -The recommendation engine will use content-based filtering techniques, including TF-IDF vectorization and cosine similarity, to measure similarities between books and generate recommendations. A web application developed with Streamlit will allow users to interact with the trained model by entering a book title and receiving personalized recommendations.


- Why does it matter?
  -Recommendation systems are widely used across industries, including entertainment, e-commerce, and social media platforms, to improve user experience and increase engagement. In the publishing industry, recommendation systems help readers discover books they may not have otherwise found, especially lesser-known indie titles that often receive less visibility than traditionally published books.
  -With the growing popularity of online reading communities such as Goodreads, BookTok, and Bookstagram, readers are exposed to an overwhelming number of book options. A recommendation system can simplify the discovery process by suggesting books that align with a reader’s interests and reading habits.
  -This project also demonstrates the practical applications of machine learning and NLP techniques in solving real-world problems involving large amounts of textual data. Additionally, focusing on indie and fantasy books creates an opportunity to highlight books that may be underrepresented in traditional recommendation systems.

  
- What are your research questions?
  1. Can natural language processing techniques effectively recommend books based on textual similarity?
  2. How accurately can a content-based recommendation system identify books that are similar in genre, themes, and descriptions?
  3. Which book features, such as genre, description, or ratings, contribute most to effective recommendations?
  4. Can a recommendation system help readers discover lesser-known indie fantasy books alongside more popular titles?

## 3. Data 

Describe the datasets you are using to answer your research questions.

- Data sources
- Data size (MB, GB, etc.)
- Data shape (# of rows and # columns)
- Time period (for example, 2010 to 2020) if your data are time-bound
- **What does each row represent?(a patient, a school, a crime, etc.)**
- Data dictionary
  - Columns name
  - Data type
  - Defition
  - Potential values (for categorical valuables, what are the categories?)
- Which variable/column will be your target/label in your ML model?
- Which variables/columns may be selected as features/predictors for your ML models?

## 4. Exploratory Data Analysis (EDA)

- Perform data exploration using Jupyter Notebook
- You would focus on the target variable and the selected features and drop all other columns.
- produce summary statistics of key variables
- Create visualizations (I recommend using **Plotly Express**)
- Find out if the data require cleansing:
  - Missing values?
  - Duplicate rows? 
- Find out if the data require splitting, merging, pivoting, melting, etc.
- Find out if you need to bring in other data sources to augment your data.
  - For example, population, socioeconomic data from Census may be helpful.
- For textual data, you will pre-process (normalize, remove stopwords, tokenize) them before you can analyze them in predictive analysis/machine learning.
- Make sure the resulting dataset need to be "tidy":
  - each row represent one observation (ideally one unique entity/subject).
  - each columm represents one unique property of that entity. 

## 5. Model Training 

- What models you will be using for predictive analytics?
- How will you train the models?
  - Train vs test split (80/20, 70/30, etc.)
  - Python packages to be used (scikit-learn, NLTK, spaCy, etc.)
  - The development environments (your laptop, Google CoLab, GitHub CodeSpaces, etc.)
- How will you measure and compare the performance of the models?

## 6. Application of the Trained Models

Develop a web app for people to interact with your trained models. Potential tools for web app development:

- **Streamlit** (recommended for its simplicity and ease to learn)
- Dash
- Flask

## 7. Conclusion

- Summarize your work and its potetial application
- Point out the limitations of your work
- Lessons learned 
- Talk about future research direction

## 8. References 

List articles, blogs, and websites that you have referenced or used in your project.

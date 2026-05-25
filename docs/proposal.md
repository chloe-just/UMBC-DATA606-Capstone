# The Template and Guideline for the Final Report

- This document serves as a guide for developing project proposal which will eventually become the proposal and final report.
- You start with the end in mind and adopt an agile approach:
  - Making progress continuously towards your goal.
  - Updating this document continuously along the way.
 
## 1. Title and Author

- Project Title: A Personalized Book Recommendation System Using Machine Learning and NLP
- Prepared for UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang
- Author: Chloe Just 
- GitHub: https://github.com/chloe-just/UMBC-DATA606-Capstone/tree/main
- LinkedIn: https://www.linkedin.com/in/chloe-just-510377124/
- Link to your PowerPoint presentation file
- Link to your YouTube video 
    
## 2. Background

Provide the background information about the chosen topic. 

- What is it about?
  - This project focuses on building a personalized book recommendation system using machine learning and natural language processing (NLP). The system will analyze book metadata and textual information, such as book descriptions, genres, and reader ratings, to recommend similar books to users based on their interests.
  - The recommendation engine will use content-based filtering techniques, including TF-IDF vectorization and cosine similarity, to measure similarities between books and generate recommendations. A web application developed with Streamlit will allow users to interact with the trained model by entering a book title and receiving personalized recommendations.


- Why does it matter?
  - Recommendation systems are widely used across industries, including entertainment, e-commerce, and social media platforms, to improve user experience and increase engagement. In the publishing industry, recommendation systems help readers discover books they may not have otherwise found, especially lesser-known indie titles that often receive less visibility than traditionally published books.
  - With the growing popularity of online reading communities such as Goodreads, BookTok, and Bookstagram, readers are exposed to an overwhelming number of book options. A recommendation system can simplify the discovery process by suggesting books that align with a reader’s interests and reading habits.
  - This project also demonstrates the practical applications of machine learning and NLP techniques in solving real-world problems involving large amounts of textual data. Additionally, focusing on indie and fantasy books creates an opportunity to highlight books that may be underrepresented in traditional recommendation systems.

  
- What are your research questions?
  1. Can natural language processing techniques effectively recommend books based on textual similarity?
  2. How accurately can a content-based recommendation system identify books that are similar in genre, themes, and descriptions?
  3. Which book features, such as genre, description, or ratings, contribute most to effective recommendations?
  4. Can a recommendation system help readers discover lesser-known indie fantasy books alongside more popular titles?

## 3. Data 

Describe the datasets you are using to answer your research questions.

- Data Source: https://www.kaggle.com/datasets/jealousleopard/goodreadsbooks
- Data Size: 1524KB
- Data Shape: 12 columns, 1127 rows
- Time Period: Unknown
- **What does each row represent?**
    - Each row represents one book in the Goodreads dataset.
    - A single record includes metadata about that book, such as its title, author, average rating, and other bibliographic information.

## Data Dictionary

| Column Name | Data Type | Definition | Potential Values |
|-------------|-----------|------------|-------------------|
| bookID | Integer | Unique identifier for each book | Positive integers |
| title | String | Title of the book | Any book title (text) |
| authors | String | Author(s) of the book | Names of authors (e.g., J.K. Rowling) |
| average_rating | Float | Mean user rating on Goodreads | 0.0 – 5.0 |
| isbn | String | ISBN-10 identifier | Numeric string or missing |
| isbn13 | String | ISBN-13 identifier | Numeric string or missing |
| language_code | Categorical (String) | Language of the book | eng, en-US, spa, fre, etc. |
| num_pages | Integer | Number of pages in the book | Positive integers |
| ratings_count | Integer | Total number of ratings | 0 – large integers |
| text_reviews_count | Integer | Number of written reviews | 0 – large integers |
| publication_date | String/Date | Date the book was published | Date format (e.g., 10/1/2008) |
| publisher | String | Publishing company | Penguin, HarperCollins, etc. |

## Target / Label Variable

This project focuses on building a **content-based book recommendation system**, which means it does not rely on a traditional supervised learning target variable (such as a class label or numeric value to predict).

Instead, the system learns patterns of similarity between books using their features (metadata and text). Therefore, the model is considered an **unsupervised learning approach**.

---

### Primary Approach (No Explicit Target Variable)

There is **no single target or label column** in this dataset because the goal is not to predict an outcome, but to measure similarity between books.

The recommendation system works by:
- Transforming book features into numerical vectors using TF-IDF
- Computing similarity between books using cosine similarity
- Returning the most similar books as recommendations

---

### Optional Target Variable (Alternative Supervised Approach)

If my project is reframed as a predictive modeling task, the following column could be used as a target variable:

- **average_rating**  
  Represents the mean user rating for each book (range: 0.0 – 5.0)

This allows for alternative modeling approaches such as:
- Regression (predicting rating value)
- Classification (e.g., high rating vs low rating)

Example classification setup:
- High-rated book: average_rating ≥ 4.0  
- Low-rated book: average_rating < 4.0  

---

### Summary

- **Primary project type:** Unsupervised learning (recommendation system)  
- **No explicit target variable is required**  
- **Core objective:** Measure similarity between books based on features  
- **Optional target (for extension):** `average_rating`

## Features / Predictors for the Machine Learning Model

For this project, the goal is to build a content-based book recommendation system. Instead of predicting a single target label, the model learns relationships between books using their metadata and textual features.

### Primary Features

These features are used to generate similarity between books using NLP techniques such as TF-IDF:

- **title**  
  The name of the book. Helps identify similar or related titles.

- **authors**  
  Author(s) of the book. Books by the same author or similar authors may be recommended together.

- **combined text representation (engineered feature)**  
  A combined field created from:
  - title  
  - authors  
  - publisher  
  - language_code  

  This is the main input for TF-IDF vectorization.

---

### Categorical Features

These features can be used for filtering or improving recommendation relevance:

- **language_code**  
  Language the book is written in (e.g., eng, en-US, fre, spa).

- **publisher**  
  Publishing company (e.g., Penguin Books, HarperCollins).

---

### Numerical Features (Optional / Enhancements)

These features are not required for basic recommendation but can be used for ranking or hybrid recommendation systems:

- **average_rating**  
  Mean user rating (0.0 – 5.0). Can help prioritize higher-rated books.

- **ratings_count**  
  Number of ratings received. Indicates popularity.

- **text_reviews_count**  
  Number of written reviews. Can indicate engagement level.

- **num_pages**  
  Length of the book. Can be used to match reading preferences.

---

### Feature Engineering Summary

To support the recommendation system, a combined feature will be created:

- **combined_features = title + authors + publisher + language_code**

This combined text is transformed into numerical vectors using **TF-IDF vectorization**, and similarity between books is computed using **cosine similarity**.

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

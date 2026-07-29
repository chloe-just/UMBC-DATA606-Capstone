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
  - This project focuses on developing a personalized book recommendation system using machine learning techniques and user rating data. The recommendation system will analyze relationships between users and books to suggest books that readers may enjoy based on their previous ratings and reading preferences.

  - The project will use the Book Recommendation Dataset from Kaggle, which contains information about books, users, and user ratings. By applying recommendation system algorithms such as collaborative filtering and similarity-based methods, the project aims to generate accurate and personalized book recommendations.

  - A web application built with Streamlit will allow users to interact with the recommendation engine by entering a book title or selecting preferences to receive recommended books.


- Why does it matter?
  - Recommendation systems are widely used in modern digital platforms such as Netflix, Spotify, Amazon, YouTube, and Goodreads to improve user experience and personalize content. In the publishing industry, recommendation systems help readers discover books that match their interests while also helping authors and publishers increase visibility and engagement.

  - As the number of available books continues to grow, readers may struggle to find books that align with their preferences. A recommendation system can reduce information overload by providing personalized suggestions based on user behavior and reading patterns.

  - This project also demonstrates practical applications of machine learning, data analysis, and recommender system design using real-world user interaction data. Additionally, recommendation systems are highly relevant in the field of data science because they combine predictive analytics, user behavior analysis, and business intelligence.

  
- What are your research questions?
  1. Can collaborative filtering techniques effectively recommend books based on user rating behavior?
  2. Which books are most frequently recommended based on user similarity patterns?
  3. How accurately can a recommendation system predict books that users may enjoy?
  4. What user and book characteristics contribute most to recommendation quality?
  5. Can recommendation systems help readers discover books beyond the most popular titles?

## 3. Data 

Describe the datasets you are using to answer your research questions.

- Data Source: [Dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset)
- Approximate dataset size: ~25 MB compressed, larger when loaded into pandas DataFrames
- Data Shape:
  - Books.csv
Approximately 271,000 rows
8 columns

  - Users.csv
Approximately 278,000 rows
3 columns

  - Ratings.csv
Approximately 1.1 million rows
3 columns

- Time Period: Collected in a 4-week crawl (August / September 2004)
- **What does each row represent?**
  - Books.csv

    Each row represents one unique book.

  - Users.csv

    Each row represents one unique user.

   - Ratings.csv

    Each row represents one user rating for a specific book.

## Data Dictionary


# Books.csv

| Column Name | Data Type | Definition | Potential Values |
|---|---|---|---|
| ISBN | String | Unique identifier for each book | ISBN-10 values |
| Book-Title | String | Title of the book | Text values |
| Book-Author | String | Author of the book | Author names |
| Year-Of-Publication | Integer | Year the book was published | Years (e.g., 1998, 2003) |
| Publisher | String | Publishing company | Publisher names |
| Image-URL-S | String | URL for small book cover image | URL links |
| Image-URL-M | String | URL for medium book cover image | URL links |
| Image-URL-L | String | URL for large book cover image | URL links |

---

# Users.csv

| Column Name | Data Type | Definition | Potential Values |
|---|---|---|---|
| User-ID | Integer | Unique identifier for each user | Positive integers |
| Location | String | User's location | City, state, country text |
| Age | Float / Integer | Age of the user | Numeric values, may contain missing values |

---

# Ratings.csv

| Column Name | Data Type | Definition | Potential Values |
|---|---|---|---|
| User-ID | Integer | Unique identifier for each user | Positive integers |
| ISBN | String | Unique identifier for each book | ISBN-10 values |
| Book-Rating | Integer | Rating given by a user to a book | Integers from 0 to 10 |

## Target / Label Variable

The primary machine learning approach for this project is a recommendation system using collaborative filtering, which is considered an unsupervised or semi-supervised learning approach.

Therefore, there is no traditional target variable like in classification or regression tasks.

However, the key interaction variable used by the recommendation model is:

Book-Rating

This variable represents the rating a user gives to a book and is used to learn user preference patterns and generate recommendations.

---

## Which variables/columns may be selected as features/predictors for your ML models?

## Primary Features

### Ratings.csv

The following columns will be the primary features used to build the recommendation system:

- `User-ID`
  - Identifies individual users
  - Used to learn user preference patterns

- `ISBN`
  - Identifies individual books
  - Used to connect ratings with book information

- `Book-Rating`
  - Represents the rating a user assigned to a book
  - Used to determine user preferences and similarity between users/books

These columns will be used to create a **user-item interaction matrix** for collaborative filtering and recommendation generation.

---

## Book Metadata Features

### Books.csv

The following book-related features may be incorporated into the recommendation system:

- `Book-Title`
  - Used to display recommendations to users
  - May also support content-based filtering

- `Book-Author`
  - Helps identify similar books by the same author
  - Can improve recommendation quality

- `Publisher`
  - May be used for additional filtering or grouping

- `Year-Of-Publication`
  - Can help analyze trends over time
  - May support filtering by publication period

---

## Optional User Features

### Users.csv

The following user demographic features may be explored during analysis:

- `Location`
  - Can be used to analyze geographic reading trends

- `Age`
  - Can be used to study reading preferences across age groups

These features are optional and may be used for exploratory analysis or future personalization improvements.

---

## Which variable/column will be your target/label in your ML model?

This project primarily uses a **recommendation system approach**, which differs from traditional supervised machine learning models.

Instead of predicting a predefined label, the model learns relationships between users and books based on user interactions and ratings.

Therefore, there is no single traditional target variable.

However, the most important interaction variable used by the recommendation model is:

- `Book-Rating`

The `Book-Rating` column represents the score a user assigns to a book on a scale from 0 to 10.

This variable will be used to:
- identify user preferences
- calculate similarity between users or books
- generate personalized recommendations

---

## Planned Machine Learning Approach

The recommendation system will primarily use:

- Collaborative Filtering
- Similarity-Based Recommendation
- Matrix Factorization techniques such as Singular Value Decomposition (SVD)

Additional recommendation approaches may also be explored, including:
- popularity-based recommendation
- content-based filtering
- hybrid recommendation systems


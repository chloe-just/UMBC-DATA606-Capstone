# A Personalized Book Recommendation System Using Machine Learning and Streamlit

**Chloe Just**

Department of Information Systems, University of Maryland, Baltimore County

DATA 606: Capstone in Data Science

Dr. Chaojie (Jay) Wang

July 2026

---

## Project Resources

**GitHub Repository**

https://github.com/chloe-just/UMBC-DATA606-Capstone

**LinkedIn**

https://www.linkedin.com/in/chloe-just-510377124/

**PowerPoint Presentation**

https://docs.google.com/presentation/d/1SfwVZcUDI0_VDJQ_lJzIFp1zLH_lgLNuFD73ie3owRM/edit?usp=sharing

**Presentation Video**

*Insert YouTube link here*

**Streamlit Application**

https://umbc-data606-capstone-ehgadptcnnxwbmdyaafbbr.streamlit.app/

# Abstract

Recommendation systems have become an essential component of modern digital platforms by helping users discover products and content that align with their interests. This project developed a personalized book recommendation system using the Book Recommendation Dataset obtained from Kaggle. The dataset contains over one million user-book interactions, including book metadata, user demographics, and explicit rating information. Exploratory data analysis was performed to understand the structure and quality of the data, identify missing values, and engineer features suitable for recommendation modeling. After preprocessing, an Item-Based Collaborative Filtering model using Cosine Similarity was implemented to generate personalized book recommendations based on historical user ratings. A user-item interaction matrix was constructed to represent explicit user preferences, and similarity scores between books were calculated to recommend titles with comparable rating patterns. The recommendation engine was designed for deployment as a Streamlit web application, allowing users to interactively receive personalized recommendations. This project demonstrates how collaborative filtering techniques can effectively leverage historical rating behavior to build scalable recommendation systems while highlighting challenges such as sparse data and cold-start problems.

**Keywords:** recommendation systems, collaborative filtering, cosine similarity, machine learning, book recommendation, Streamlit

# Introduction

The rapid growth of digital content has made personalized recommendation systems increasingly important across many industries. Online platforms such as Amazon, Netflix, Spotify, Goodreads, and YouTube rely heavily on recommendation algorithms to help users discover content that matches their interests while improving overall user engagement. Rather than requiring users to manually search through thousands of available options, recommendation systems analyze historical behavior and preferences to generate personalized suggestions.

The publishing industry faces similar challenges. With millions of books available across numerous genres and authors, readers often struggle to identify books that align with their interests. Recommendation systems reduce this information overload by identifying relationships between books and readers based on previous interactions. These systems not only improve the user experience but also help publishers and independent authors increase the visibility of their work by recommending books that readers might not otherwise discover.

This project developed a personalized book recommendation system using the Book-Crossing dataset published on Kaggle. The recommendation engine was built using Item-Based Collaborative Filtering with Cosine Similarity, a widely used recommendation technique that identifies books with similar user rating patterns. Rather than relying on book genres or textual descriptions, the model generates recommendations entirely from explicit user ratings.

In addition to developing the recommendation model, this project demonstrates the complete machine learning workflow, including data cleaning, exploratory data analysis, feature engineering, recommendation generation, and deployment planning using Streamlit. The project illustrates how collaborative filtering can be applied to real-world recommendation problems while providing a foundation for future enhancements such as hybrid recommendation systems and explainable artificial intelligence.

# Research Questions

This project was guided by the following research questions:

1. Can Item-Based Collaborative Filtering effectively recommend books using historical user rating behavior?

2. How does filtering inactive users and infrequently rated books affect the quality of the recommendation model?

3. Which books exhibit the strongest similarity relationships based on user rating patterns?

4. What characteristics of the Book-Crossing dataset influence recommendation quality?

5. How can collaborative filtering be incorporated into an interactive web application that generates personalized book recommendations for users?

# 5. Data

## Data Source

This project used the **Book Recommendation Dataset** published on Kaggle by Möbius. The dataset contains information collected during a four-week crawl of the Book Recommendation online community in August and September 2004. It includes information about books, users, and user ratings, making it well suited for developing collaborative filtering recommendation systems.

The complete dataset consists of three relational tables: **Books**, **Users**, and **Ratings**. Together, these tables provide the information necessary to analyze user reading preferences and generate personalized book recommendations. The tables are connected through two primary identifiers: **ISBN**, which uniquely identifies each book, and **User-ID**, which uniquely identifies each user.

Table 1 summarizes the datasets used throughout this project.

### Table 1

**Summary of Datasets**

| Dataset | Approximate Rows | Columns | Description |
|----------|----------------:|---------|-------------|
| Books.csv | ~271,000 | 8 | Metadata describing individual books |
| Users.csv | ~278,000 | 3 | User demographic information |
| Ratings.csv | ~1.1 million | 3 | Explicit and implicit user ratings |

The compressed dataset is approximately **25 MB**, although the memory footprint increases substantially after loading the data into pandas DataFrames and merging the tables for analysis.

---

## Dataset Description

Each dataset represents a different entity within the recommendation system.

The **Books** dataset contains metadata describing individual books, including their ISBN, title, author, publisher, publication year, and links to cover images. Each row represents one unique book.

The **Users** dataset contains demographic information for individual users, including a unique user identifier, geographic location, and age. Each row represents one unique user.

The **Ratings** dataset records user interactions with books. Each row represents one rating that a user assigned to a specific book. Ratings range from **0 to 10**, where ratings from **1 to 10** represent explicit user preferences and a rating of **0** represents implicit feedback.

---

## Data Dictionary

### Table 2

**Books Dataset Variables**

| Variable | Data Type | Description |
|----------|-----------|-------------|
| ISBN | String | Unique identifier assigned to each book |
| Book-Title | String | Title of the book |
| Book-Author | String | Author of the book |
| Year-Of-Publication | Integer | Publication year |
| Publisher | String | Publishing company |
| Image-URL-S | String | Small book cover image URL |
| Image-URL-M | String | Medium book cover image URL |
| Image-URL-L | String | Large book cover image URL |

---

### Table 3

**Users Dataset Variables**

| Variable | Data Type | Description |
|----------|-----------|-------------|
| User-ID | Integer | Unique identifier assigned to each user |
| Location | String | User's reported location |
| Age | Numeric | User's reported age |

---

### Table 4

**Ratings Dataset Variables**

| Variable | Data Type | Description |
|----------|-----------|-------------|
| User-ID | Integer | User identifier |
| ISBN | String | Book identifier |
| Book-Rating | Integer | Rating assigned to a book (0–10) |

---

## Feature Selection

Collaborative filtering differs from traditional supervised machine learning because it learns relationships between users and items rather than predicting a predefined outcome. Consequently, feature selection focused on variables describing user-book interactions.

The primary variables used during model development were **User-ID**, **ISBN**, and **Book-Rating**. These variables were used to construct the user-item interaction matrix that served as the foundation of the recommendation model.

Additional book metadata—including **Book-Title**, **Book-Author**, **Publisher**, and **Year-Of-Publication**—were retained to improve the readability of recommendations and support exploratory data analysis. Although these variables were not used directly during similarity calculations, they were essential for presenting meaningful recommendations to users.

User demographic variables, including **Age** and **Location**, were explored during the exploratory data analysis but were not incorporated into the collaborative filtering model because recommendations were generated exclusively from historical rating behavior.

---

## Target Variable

Unlike classification or regression problems, collaborative filtering recommendation systems do not predict a traditional target variable. Instead, the model learns latent relationships between users and books using historical interactions.

The **Book-Rating** variable served as the primary interaction variable throughout this project. Ratings provided explicit evidence of user preferences and were used to construct the user-item matrix from which similarities between books were calculated. During preprocessing, implicit ratings (ratings equal to zero) were removed so that similarity calculations reflected only explicit user opinions.

---

## Machine Learning Approach

This project implemented an **Item-Based Collaborative Filtering** recommendation system using **Cosine Similarity**. Collaborative filtering identifies relationships between books by examining how users rate them, rather than relying on book descriptions or manually assigned categories.

Several recommendation approaches were considered during project planning, including User-Based Collaborative Filtering and Matrix Factorization using Singular Value Decomposition (SVD). Item-Based Collaborative Filtering was ultimately selected because it performs well on sparse datasets, scales efficiently to large collections of books, and produces recommendations that are relatively easy to interpret.

The resulting recommendation engine generates personalized book suggestions by identifying books with similar rating patterns while excluding books that a user has already rated.

# 6. Model Development

## Recommendation Model

The primary objective of this project was to develop a personalized book recommendation system capable of suggesting books based on historical user rating behavior. To accomplish this, an **Item-Based Collaborative Filtering (IBCF)** approach was implemented using **Cosine Similarity**. Collaborative filtering is one of the most widely used recommendation techniques because it identifies relationships between users and items without requiring additional information such as genres, keywords, or book descriptions.

Unlike supervised machine learning models that learn to predict a target variable, collaborative filtering identifies patterns within historical user interactions. Books that receive similar ratings from many of the same users are considered similar, allowing the system to recommend books that closely match a user's previous preferences.

---

## Data Preparation

Before constructing the recommendation model, the dataset underwent several preprocessing steps designed to improve recommendation quality.

First, all implicit ratings (ratings equal to zero) were removed because they do not represent explicit user preferences. Only ratings from one to ten were retained for model development.

Next, inactive users and infrequently rated books were filtered from the dataset. Users with fewer than 25 explicit ratings and books with fewer than 15 ratings were excluded. These thresholds reduced noise, improved the density of the dataset, and increased the reliability of similarity calculations.

Following preprocessing, the Books, Users, and Ratings datasets were merged into a single dataset using the **ISBN** and **User-ID** fields.

---

## User-Item Matrix Construction

The filtered dataset was transformed into a **user-item interaction matrix**, which serves as the foundation of collaborative filtering algorithms.

Within the matrix:

- Each row represents an individual user.
- Each column represents a unique book identified by its ISBN.
- Each cell contains the explicit rating assigned by a user to a particular book.

Because most users rate only a small percentage of available books, the resulting matrix contained many missing values. These missing values were replaced with zeros after pivoting to indicate that a user had not rated a particular book.

It is important to note that these zeros do **not** represent user ratings of zero. Instead, they indicate the absence of an explicit rating and enable similarity calculations to be performed using a complete numerical matrix.

---

## Similarity Computation

After constructing the user-item matrix, Cosine Similarity was used to calculate the similarity between every pair of books.

Cosine Similarity measures the angle between two rating vectors rather than their absolute magnitude. Books that receive similar rating patterns from many of the same users produce similarity scores close to one, while unrelated books produce similarity scores closer to zero.

The similarity matrix forms the core of the recommendation engine by identifying books that exhibit comparable user rating behavior.

---

## Recommendation Generation

Personalized recommendations were generated using the following process:

1. A user was selected from the filtered dataset.
2. The books that the user rated highly were identified.
3. Similar books were retrieved from the cosine similarity matrix.
4. Books the user had already rated were removed.
5. The remaining books were ranked according to similarity score.
6. The highest-ranked books were returned as personalized recommendations.

This approach allows the system to recommend books that share similar rating patterns with books the user has previously enjoyed.

---

## Development Environment

Model development was performed using **Google Colaboratory (Google Colab)** within Jupyter Notebook. Python served as the primary programming language, while GitHub was used for version control and project management.

The following Python libraries were used throughout the project:

- pandas
- NumPy
- scikit-learn
- matplotlib
- Plotly Express

Cosine similarity calculations were implemented using the `cosine_similarity()` function provided by the **scikit-learn** library.

---

## Model Evaluation

Because this project implemented a recommendation system rather than a supervised prediction model, traditional evaluation metrics such as classification accuracy were not appropriate.

Instead, the recommendation system was evaluated qualitatively by examining the recommendations produced for individual users and verifying that the suggested books exhibited meaningful relationships to books the users had previously rated highly.

Additional characteristics of the recommendation dataset were also examined, including matrix sparsity, user activity, and book popularity. The final user-item matrix exhibited approximately **99.89% sparsity**, which is typical of real-world recommendation datasets and demonstrates the importance of collaborative filtering techniques designed to operate effectively on sparse data.

Future work may include quantitative evaluation using recommendation-specific metrics such as Precision@K, Recall@K, Mean Average Precision (MAP), Normalized Discounted Cumulative Gain (NDCG), recommendation diversity, and recommendation coverage.

---

## Explainable Recommendations

To improve transparency and user trust, the recommendation system was designed to support explainable recommendations. Rather than presenting recommendations without context, the system can identify books that influenced each recommendation based on historical user ratings and similarity scores.

Providing explanations helps users understand why a particular recommendation was generated and represents an important step toward creating more interpretable machine learning systems.


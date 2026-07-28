import pandas as pd
import numpy as np
import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Book Recommendation App",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Interactive Book Recommender")
st.markdown("Select a book you enjoyed, and we will recommend similar books based on community rating patterns!")

# --- DATA PREPROCESSING & MATRIX GENERATION ---
@st.cache_data
def load_and_prep_data():
    # Load raw data
    books = pd.read_csv("data/books.zip", encoding="latin-1", low_memory=False)
    ratings = pd.read_csv("data/ratings.zip", encoding="latin-1")
    users = pd.read_csv("data/users.zip", encoding="latin-1")

    # Merge datasets on ISBN
    df = ratings.merge(books, on="ISBN")

    # Filter out inactive users and unpopular books to keep memory usage low & stats high
    # 1. Users with at least 200 ratings
    user_counts = df['User-ID'].value_counts()
    active_users = user_counts[user_counts >= 200].index
    df_filtered = df[df['User-ID'].isin(active_users)]

    # 2. Books with at least 50 ratings
    book_counts = df_filtered['Book-Title'].value_counts()
    popular_books = book_counts[book_counts >= 50].index
    final_df = df_filtered[df_filtered['Book-Title'].isin(popular_books)]

    # Create User-Item Pivot Table
    pivot_table = final_df.pivot_table(index='Book-Title', columns='User-ID', values='Book-Rating').fillna(0)

    # Compute Cosine Similarity between Books
    similarity_scores = cosine_similarity(pivot_table)
    similarity_df = pd.DataFrame(similarity_scores, index=pivot_table.index, columns=pivot_table.index)

    return books, similarity_df

# Load preprocessed structures
with st.spinner("Processing dataset and building recommendation matrix..."):
    books_df, similarity_df = load_and_prep_data()

# --- RECOMMENDATION ENGINE FUNCTION ---
def get_recommendations(book_name, similarity_matrix, books_metadata, top_n=5):
    if book_name not in similarity_matrix.index:
        return None
    
    # Get top N similar books (excluding the selected book itself)
    similar_scores = similarity_matrix[book_name].sort_values(ascending=False)[1:top_n+1]
    
    recommendations = []
    for title, score in similar_scores.items():
        # Fetch metadata (Author, Image URL) from raw books data
        meta = books_metadata[books_metadata['Book-Title'] == title].iloc[0]
        recommendations.append({
            "title": title,
            "author": meta.get("Book-Author", "Unknown Author"),
            "image": meta.get("Image-URL-M", None),
            "similarity": f"{score * 100:.1f}% Match"
        })
    return recommendations

# --- INTERACTIVE APP CONTROLS ---

st.sidebar.header("Configuration")

# Dropdown list of available books in the matrix
book_list = sorted(similarity_df.index.tolist())
selected_book = st.selectbox(
    "🔍 Pick or type a book title:",
    options=book_list,
    index=0
)

num_recommendations = st.sidebar.slider("Number of Recommendations:", min_value=3, max_value=10, value=5)

# Generate Button
if st.button("Get Recommendations 🚀"):
    st.subheader(f"Because you liked: **{selected_book}**")
    st.markdown("---")
    
    results = get_recommendations(selected_book, similarity_df, books_df, top_n=num_recommendations)
    
    if results:
        # Display recommendations in grid columns
        cols = st.columns(len(results))
        for idx, rec in enumerate(results):
            with cols[idx]:
                if pd.notna(rec["image"]):
                    st.image(rec["image"], use_container_width=True)
                st.write(f"**{rec['title']}**")
                st.caption(f"By {rec['author']}")
                st.write(f"`{rec['similarity']}`")
    else:
        st.error("Sorry, could not find recommendations for that title.")

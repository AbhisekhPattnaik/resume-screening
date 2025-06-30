import streamlit as st
import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

st.markdown("<h1 style='text-align: center; color: white;'>AI-Powered Resume Screening Tool</h1>", unsafe_allow_html=True)

# Upload job description
st.header("Upload Job Description")
job_description = st.file_uploader("Upload a Job Description (TXT file)", type=["txt"])

# Upload resumes
st.header("Upload Resumes")
resumes = st.file_uploader("Upload Resumes (PDFs)", type=["pdf"], accept_multiple_files=True)

if job_description is not None:
    # Read the job description text
    job_text = job_description.read().decode("utf-8")
    st.subheader("Job Description Preview:")
    st.write(job_text)

    if resumes:
        st.subheader("Resume Previews:")
        resume_texts = []
        for resume in resumes:
            pdf_reader = PyPDF2.PdfReader(resume)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            resume_texts.append(text)
            st.write(f"**{resume.name}**")
            st.write(text[:500])  # preview first 500 characters

        # Combine the job description with all resumes into one list
        documents = [job_text] + resume_texts

        # Create TF-IDF matrix
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(documents)

        # Compute cosine similarity between the job description (first doc) and each resume
        similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

        # Rank resumes
        ranking = sorted(zip(resumes, similarities), key=lambda x: x[1], reverse=True)

        st.subheader("Ranked Candidates:")

        # Build a DataFrame for exporting
        ranking_df = pd.DataFrame({
            "Rank": [i + 1 for i in range(len(ranking))],
            "Filename": [r.name for r, s in ranking],
            "Similarity Score": [round(s, 2) for r, s in ranking]
        })

        # Display ranked list
        for i, (resume_file, score) in enumerate(ranking, start=1):
            st.write(f"**Rank {i}: {resume_file.name}** - Similarity Score: {score:.2f}")

        # Convert to CSV
        csv_data = ranking_df.to_csv(index=False).encode('utf-8')

        st.download_button(
            label="Download Rankings as CSV",
            data=csv_data,
            file_name="ranked_candidates.csv",
            mime="text/csv"
        )

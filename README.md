# AI-Powered Resume Screening Tool

An intelligent resume screening application that uses machine learning to automatically rank and match resumes against job descriptions.

## Overview

This tool automates the resume screening process by analyzing job descriptions and candidate resumes using TF-IDF vectorization and cosine similarity metrics. It helps HR teams and recruiters identify the most relevant candidates quickly and efficiently.

## Features

- **Job Description Upload**: Upload job descriptions in TXT format
- **Batch Resume Processing**: Upload multiple resumes in PDF format simultaneously
- **Intelligent Ranking**: Automatically ranks resumes based on relevance to the job description
- **Similarity Scoring**: Provides numerical similarity scores for objective comparison
- **Preview Functionality**: View both job descriptions and resume content directly in the app
- **CSV Export**: Download ranked results as a CSV file for further processing

## Requirements

- Python 3.7+
- Streamlit
- PyPDF2
- scikit-learn
- pandas

## Installation

1. Clone or download this repository
2. Install the required dependencies:

```bash
pip install streamlit PyPDF2 scikit-learn pandas
```

## Usage

1. Start the Streamlit application:

```bash
streamlit run app.py
```

2. Open your browser and navigate to the provided URL (typically `http://localhost:8501`)

3. Upload a job description file (TXT format)

4. Upload one or more resume files (PDF format)

5. View the ranked list of candidates with similarity scores

6. Download the rankings as a CSV file for further review

## How It Works

The application uses the following approach:

1. **Text Extraction**: Extracts text from the job description and all uploaded resumes
2. **Vectorization**: Converts text documents into TF-IDF (Term Frequency-Inverse Document Frequency) vectors
3. **Similarity Calculation**: Computes cosine similarity between the job description and each resume
4. **Ranking**: Sorts resumes by similarity score in descending order
5. **Export**: Allows download of results as CSV for integration with other tools

## Input Formats

- **Job Description**: Plain text file (.txt)
- **Resumes**: PDF files (.pdf)

## Output

- **Visual Display**: Ranked list with similarity scores displayed in the web interface
- **CSV Export**: `ranked_candidates.csv` containing:
  - Rank (1, 2, 3, ...)
  - Filename (resume filename)
  - Similarity Score (0.0 - 1.0)

## Similarity Score Interpretation

- **0.9 - 1.0**: Excellent match
- **0.7 - 0.89**: Strong match
- **0.5 - 0.69**: Moderate match
- **0.3 - 0.49**: Weak match
- **0.0 - 0.29**: Poor match

## Limitations

- Relies on keyword and phrase matching; semantic understanding is limited
- PDF text extraction quality depends on resume formatting
- Works best with well-formatted documents
- Does not consider candidate experience or qualifications beyond text similarity

## Future Enhancements

- Integration with structured resume parsing
- Support for additional file formats (DOCX, etc.)
- Customizable scoring weights
- Advanced filtering and search options
- Database integration for candidate tracking

## License

This project is provided as-is for recruitment and HR purposes.

## Support

For issues or questions, please review the code comments or modify the application as needed for your specific use case.

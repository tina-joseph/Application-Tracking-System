## Application Tracking System (ATS) using Generative AI

This project is designed to automate the job application processing and matching process using Streamlit, Google's generative AI API, and PyPDF2. It involves an Application Tracking System (ATS) designed to help job seekers optimize their resumes for specific job roles and help recruiters streamline their recruitment process.

## Features

- **Streamlit App:** Users upload resumes (PDF), select job titles, input job descriptions, and set advanced criteria.
- **Automated Feedback:** Provides profile match percentage, missing keywords, highlighted keywords, removable keywords, and experience relevance.
- **Generative AI Integration:** Utilizes Google's generative AI API (Gemini) for content generation and job application optimization.
- **Customized Prompts:** Tailored prompts for various job roles stored in the '/prompts/' folder.
- **PDF Processing:** PyPDF2 used for PDF processing.
- **Integration:** App integrates with Google GenAI API for keyword matching and displays detailed results.
  
Overall, this project leverages cutting-edge technology to automate and optimize the job application process, making it easier for job seekers and recruiters.

## Folder Structure
- `prompts/`: Contains prompts for different job roles.
- `requirements.txt`: Lists dependencies for the project.

  
## Streamlit App

Figure 1: ATS Streamlit App

![App Screenshot](images/img.png)


## Usage
- Select the desired job title and input the job description.
- Optionally, set advanced criteria.
- Upload your resume (PDF format).
- Click "Submit" to view matching results.

  
Figure 2: ATS Results Page

![ATS Results](images/img2.png)

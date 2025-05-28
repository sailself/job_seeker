# AI-Powered Job Search and CV Enhancer

## Description
This tool aims to automate and enhance the job search process. It allows users to define job search criteria (titles, locations) and then (in future versions) will scrape job postings from various sources. A key feature is the planned AI-driven analysis of a user's CV against job descriptions to determine suitability and suggest CV enhancements tailored to specific roles. The current version uses stubbed (placeholder) modules for scraping and AI analysis.

## Features (Current - Stubbed)
*   Configurable job search parameters via `job_search_tool/config.json` (target country, cities, job titles).
*   Modular structure:
    *   `scraper`: For fetching job postings (currently `ExampleJobSiteScraper` provides dummy data).
    *   `analyzer`: For CV analysis and enhancement against job descriptions (currently `GeminiCvAnalyzer` provides dummy analysis).
    *   `reporting`: For generating output.
*   Placeholder implementations for web scraping and AI analysis, allowing the main workflow to be demonstrated.
*   Generates a Markdown report (e.g., `found_jobs.md`) listing jobs deemed "suitable" by the stubbed analyzer, along with dummy CV enhancement suggestions.

## Setup and Running (Stubbed Version)

1.  **Create a Python virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

2.  **Install requirements:**
    (Currently, no external packages are strictly required for the stubbed version, but this step is good practice for future development.)
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure the application:**
    *   Copy or rename `job_search_tool/config.json.example` to `job_search_tool/config.json`.
    *   Edit `job_search_tool/config.json` to specify:
        *   `target_country` (e.g., "USA")
        *   `target_cities` (e.g., `["New York", "Remote"]`)
        *   `job_titles` (e.g., `["Software Engineer", "Data Analyst"]`)
        *   `cv_path`: Path to your CV file (e.g., "my_documents/cv.pdf"). **Note:** The current version uses a hardcoded CV string in `main.py`, so this path is for future use.
        *   `output_file`: Desired name for the Markdown report (e.g., "my_job_search_results.md").
    *   The `gemini_api_key` field in `config.json` is a placeholder. For actual AI integration in the future, a valid API key from a provider like Google Gemini would be required.

4.  **Run the application:**
    Execute the main script from the project's root directory (`job_search_tool/`):
    ```bash
    python -m job_search_tool.job_search_tool.main
    ```

5.  **Expected Output:**
    The script will print progress messages to the console. It will generate a Markdown file (e.g., `found_jobs.md`, or as configured in `job_search_tool/config.json`) in the project root directory. This file will contain job postings that the stubbed `GeminiCvAnalyzer` deemed "suitable", along with any dummy CV enhancement suggestions.

## Future Development
*   Implement actual web scrapers for popular job sites (e.g., LinkedIn, Indeed, specific company career pages).
*   Integrate with a real AI API (like Google Gemini) for sophisticated CV-to-job-description analysis and personalized CV enhancement suggestions.
*   Implement reading of CV content from the path specified in `config.json`.
*   Add more robust error handling, logging, and input validation.
*   Develop a simple user interface (web-based or desktop application).
*   Expand configuration options (e.g., job type, experience level, specific keywords to include/exclude).

---
*This project is for demonstration and educational purposes.*

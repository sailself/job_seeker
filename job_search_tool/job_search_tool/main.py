# Main script for the Job Search Tool
import os

# Assuming the script is run from the root of the project (/app),
# the following imports should work if the job_search_tool directory is in the Python path.
# For `python -m job_search_tool.job_search_tool.main` execution, these relative imports are correct.
from .config import load_config
from .scraper.example_job_site_scraper import ExampleJobSiteScraper
from .analyzer.gemini_analyzer import GeminiCvAnalyzer
from .reporting import save_jobs_to_markdown

def main():
    """
    Main function to orchestrate the job search and analysis process.
    """
    print("Starting Job Search Tool...")

    # 1. Load Configuration
    config = load_config()
    print("Configuration loaded.")
    # print(f"Config settings: {config}") # For debugging

    # 2. Initialize Components
    scraper = ExampleJobSiteScraper()
    print("ExampleJobSiteScraper initialized.")
    
    analyzer = GeminiCvAnalyzer(api_key=config.get('gemini_api_key', 'YOUR_API_KEY_HERE'))
    print("GeminiCvAnalyzer initialized.")

    # 3. Load CV (Stubbed)
    # In a real version, you would read the CV content from the file specified in config.get('cv_path')
    # For example:
    # cv_path = config.get('cv_path')
    # try:
    #     with open(cv_path, 'r', encoding='utf-8') as f:
    #         cv_content = f.read()
    #     print(f"CV loaded from {cv_path}")
    # except FileNotFoundError:
    #     print(f"Error: CV file not found at {cv_path}. Please check your config.json.")
    #     return
    # except Exception as e:
    #     print(f"Error reading CV file: {e}")
    #     return
    cv_content = "Experienced Python Developer with a background in web development and data analysis. Strong skills in Django, Flask, and SQL. Proven ability to deliver high-quality software solutions. Team player with excellent communication skills. Authored a paper on AI."
    print(f"CV content loaded (stubbed). Preview: '{cv_content[:100]}...'")

    # 4. Search for Jobs
    print(f"Searching for jobs with titles: {config.get('job_titles')} in cities: {config.get('target_cities')}...")
    job_stubs = scraper.search_jobs(
        job_titles=config.get('job_titles', []), 
        locations=config.get('target_cities', [])
    )
    print(f"Found {len(job_stubs)} job postings (stubs).")

    # 5. Process Found Jobs
    suitable_and_enhanced_jobs = []
    if not job_stubs:
        print("No job stubs found to process.")
    
    for job_stub in job_stubs:
        job_title = job_stub.get('title', 'Unknown Title')
        job_url = job_stub.get('url')
        print(f"\nProcessing job: {job_title} ({job_url})...")

        if not job_url:
            print(f"Skipping job '{job_title}' due to missing URL.")
            continue

        job_details = scraper.get_job_details(job_url)
        if not job_details.get('full_description'):
            print(f"Could not retrieve full description for {job_title}. Skipping analysis.")
            continue
            
        print(f"  Retrieved details for: {job_details.get('title')}")

        is_suitable, reasoning = analyzer.is_cv_suitable(
            cv_text=cv_content, 
            job_description_text=job_details.get('full_description', '')
        )

        if is_suitable:
            print(f"  CV is SUITABLE for '{job_details.get('title')}'. Reason: {reasoning}")
            enhanced_cv_snippet = analyzer.enhance_cv(
                cv_text=cv_content, 
                job_description_text=job_details.get('full_description', '')
            )
            print(f"  CV enhancement snippet generated for '{job_details.get('title')}'.")

            report_job_data = job_details.copy()
            report_job_data['suitability_reasoning'] = reasoning
            report_job_data['enhanced_cv_snippet'] = enhanced_cv_snippet
            suitable_and_enhanced_jobs.append(report_job_data)
        else:
            print(f"  CV is NOT suitable for '{job_details.get('title')}'. Reason: {reasoning}")

    # 6. Save Report
    output_file = config.get('output_file', 'found_jobs_report.md')
    print(f"\nSaving {len(suitable_and_enhanced_jobs)} suitable and enhanced jobs to '{output_file}'...")
    save_jobs_to_markdown(
        found_jobs=suitable_and_enhanced_jobs, 
        output_filename=output_file
    )

    print("\nProcess complete.")

if __name__ == '__main__':
    # To run this script, navigate to the project root (/app) and execute:
    # python -m job_search_tool.job_search_tool.main
    main()

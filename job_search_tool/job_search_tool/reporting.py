# Reporting functionalities for the Job Search Tool
import os

def save_jobs_to_markdown(found_jobs: list[dict], output_filename: str):
    """
    Saves a list of found job postings to a Markdown file.

    Args:
        found_jobs: A list of dictionaries, where each dictionary represents a job posting.
                    Expected keys: 'title', 'company', 'location', 'url', 'description_short'.
                    Optional keys: 'suitability_reasoning', 'enhanced_cv_snippet'.
        output_filename: The name of the file where the report will be saved (e.g., "found_jobs.md").
                         The file will be created in the directory from which the script is run.
                         For testing, this will be the project root.
    """
    try:
        # Ensure the directory for the output file exists if output_filename includes a path
        output_dir = os.path.dirname(output_filename)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"Created directory: {output_dir}")

        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write("# Found Job Postings\n\n")

            if not found_jobs:
                f.write("No job postings found.\n")
                print(f"Report saved to {output_filename} (No jobs found).")
                return

            for i, job in enumerate(found_jobs):
                f.write(f"## Job Title: {job.get('title', 'N/A')}\n\n")
                f.write(f"**Company:** {job.get('company', 'N/A')}\n")
                f.write(f"**Location:** {job.get('location', 'N/A')}\n")
                f.write(f"**URL:** [{job.get('url', '#')}]({job.get('url', '#')})\n") # Make URL a clickable link
                f.write(f"**Summary:** {job.get('description_short', 'No summary provided.')}\n\n")

                if 'suitability_reasoning' in job:
                    f.write(f"**Suitability Notes:** {job['suitability_reasoning']}\n\n")

                if 'enhanced_cv_snippet' in job:
                    f.write("### Suggested CV Enhancement Snippet:\n")
                    f.write("```text\n") # Using text block for potentially multi-line snippets
                    f.write(f"{job['enhanced_cv_snippet']}\n")
                    f.write("```\n\n")
                
                if i < len(found_jobs) - 1:
                    f.write("---\n\n") # Horizontal rule between job entries

        print(f"Report saved to {output_filename}")

    except IOError as e:
        print(f"Error writing report to {output_filename}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    # Sample job data for demonstration
    sample_jobs_data = [
        {
            'title': 'Senior Python Developer',
            'company': 'Innovatech Solutions',
            'location': 'San Francisco, CA',
            'url': 'http://example.com/job/senior-python-dev',
            'description_short': 'Lead development of scalable web applications using Python and Django.',
            'suitability_reasoning': 'Excellent match: CV highlights Python, Django, and leadership experience.',
            'enhanced_cv_snippet': "Enhanced CV Snippet for Senior Python Developer:\n- Led a team of 5 engineers in developing a new microservices architecture using Python, resulting in a 20% performance increase.\n- Expert in Django and Flask frameworks."
        },
        {
            'title': 'Data Scientist',
            'company': 'DataDriven Corp.',
            'location': 'New York, NY',
            'url': 'http://example.com/job/data-scientist',
            'description_short': 'Analyze large datasets to extract meaningful insights and build predictive models.',
            # This job entry intentionally omits suitability_reasoning and enhanced_cv_snippet for testing
        },
        {
            'title': 'Frontend Engineer (React)',
            'company': 'UI Masters Inc.',
            'location': 'Remote',
            'url': 'http://example.com/job/frontend-react',
            'description_short': 'Develop responsive user interfaces with React and modern JavaScript frameworks.',
            'suitability_reasoning': 'Good fit: CV shows strong React skills.',
            'enhanced_cv_snippet': "Suggested CV update for Frontend Engineer:\n- Proficient in React, Redux, and Next.js for building complex UIs.\n- Experience with UI/UX design principles and tools like Figma."
        },
        { # Job with missing URL to test default handling
            'title': 'Junior QA Tester',
            'company': 'BugFinders Ltd.',
            'location': 'Austin, TX',
            # 'url': 'http://example.com/job/qa-tester', # URL intentionally missing
            'description_short': 'Entry-level position for QA testing of web and mobile applications.'
        }
    ]

    test_output_filename = "test_job_report.md"
    print(f"--- Testing save_jobs_to_markdown ---")
    print(f"Generating report at: {os.path.abspath(test_output_filename)}")
    save_jobs_to_markdown(sample_jobs_data, test_output_filename)

    print(f"\n--- Testing with empty job list ---")
    empty_test_output_filename = "test_empty_job_report.md"
    print(f"Generating empty report at: {os.path.abspath(empty_test_output_filename)}")
    save_jobs_to_markdown([], empty_test_output_filename)

    # To verify, you would manually check the contents of 'test_job_report.md' and 'test_empty_job_report.md'
    # Or use read_files tool if further programmatic checks were needed.
    print("\nTest finished. Please check the generated .md files.")

# Example implementation of a job scraper
from .base import JobScraperBase

class ExampleJobSiteScraper(JobScraperBase):
    """
    An example implementation of JobScraperBase for a hypothetical job site.
    This class provides dummy data for demonstration and testing purposes.
    """

    def search_jobs(self, job_titles: list[str], locations: list[str]) -> list[dict]:
        """
        Simulates searching for jobs and returns a list of dummy job postings.
        """
        print(f"ExampleJobSiteScraper: Searching for jobs with titles {job_titles} in locations {locations}...")
        return [
            {
                'title': 'Software Engineer (Python)',
                'company': 'Tech Example Inc.',
                'location': 'Anytown, USA',
                'url': 'http://example.com/job/123',
                'description_short': 'Exciting role for a Python developer focusing on web application development.'
            },
            {
                'title': 'Data Analyst',
                'company': 'Analytics Solutions Ltd.',
                'location': 'Anycity, USA',
                'url': 'http://example.com/job/456',
                'description_short': 'Join our data team and make an impact by analyzing trends and generating insights.'
            },
            {
                'title': 'Frontend Developer (React)',
                'company': 'Web Innovations Co.',
                'location': 'Remote',
                'url': 'http://example.com/job/789',
                'description_short': 'Seeking a skilled React developer to build modern user interfaces.'
            }
        ]

    def get_job_details(self, job_url: str) -> dict:
        """
        Simulates fetching detailed job information for a given URL.
        Returns a dictionary with dummy detailed data.
        """
        print(f"ExampleJobSiteScraper: Getting details for {job_url}...")
        
        # Dummy logic to return different details based on URL or just a generic one
        if "123" in job_url:
            return {
                'title': 'Software Engineer (Python)',
                'company': 'Tech Example Inc.',
                'location': 'Anytown, USA',
                'url': job_url,
                'description_short': 'Exciting role for a Python developer focusing on web application development.',
                'full_description': 'This is a detailed job description for the Software Engineer (Python) role at Tech Example Inc. Responsibilities include designing, developing, and maintaining web applications using Python and Django. Requirements: 3+ years of Python experience, proficiency with Django/Flask, database knowledge (SQL/NoSQL), and familiarity with version control (Git).',
                'posted_date': '2024-01-10',
                'salary_range': '$90,000 - $120,000',
                'skills': ['Python', 'Django', 'SQL', 'Git', 'API Development']
            }
        elif "456" in job_url:
            return {
                'title': 'Data Analyst',
                'company': 'Analytics Solutions Ltd.',
                'location': 'Anycity, USA',
                'url': job_url,
                'description_short': 'Join our data team and make an impact by analyzing trends and generating insights.',
                'full_description': 'Analytics Solutions Ltd. is looking for a Data Analyst to interpret data, analyze results using statistical techniques, and provide ongoing reports. Key responsibilities: data mining, data cleaning, report generation. Qualifications: BS in Mathematics, Economics, Computer Science, Information Management or Statistics, strong analytical skills.',
                'posted_date': '2024-01-12',
                'employment_type': 'Full-time',
                'experience_level': 'Mid-Level'
            }
        else: # Generic fallback for other URLs like example.com/job/789
            return {
                'title': 'Frontend Developer (React)',
                'company': 'Web Innovations Co.',
                'location': 'Remote',
                'url': job_url,
                'description_short': 'Seeking a skilled React developer to build modern user interfaces.',
                'full_description': 'Web Innovations Co. is hiring a Frontend Developer proficient in React.js. You will be responsible for developing and implementing user interface components. Must have strong experience with React, Redux, HTML, CSS, and JavaScript.',
                'posted_date': '2024-01-15',
                'benefits': ['Health Insurance', 'Remote Work Options', 'Paid Time Off']
            }

if __name__ == '__main__':
    # Example usage for testing the scraper
    scraper = ExampleJobSiteScraper()

    print("\\n--- Testing search_jobs ---")
    jobs = scraper.search_jobs(job_titles=["Python Developer", "Data Scientist"], locations=["Anytown, USA", "Remote"])
    for job in jobs:
        print(job)

    print("\\n--- Testing get_job_details for job 123 ---")
    if jobs: # Ensure there are jobs to get details for
        details1 = scraper.get_job_details("http://example.com/job/123")
        print(details1)

    print("\\n--- Testing get_job_details for job 789 ---")
    details2 = scraper.get_job_details("http://example.com/job/789") # Test a different URL
    print(details2)

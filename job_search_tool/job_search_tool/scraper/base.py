# Base classes for job scrapers
from abc import ABC, abstractmethod

class JobScraperBase(ABC):
    """
    Abstract base class for job scrapers.
    Defines the interface that all job scrapers must implement.
    """

    @abstractmethod
    def search_jobs(self, job_titles: list[str], locations: list[str]) -> list[dict]:
        """
        Searches for jobs based on a list of job titles and locations.

        Args:
            job_titles: A list of job titles to search for (e.g., ["Software Engineer", "Data Analyst"]).
            locations: A list of locations to search within (e.g., ["New York, NY", "Remote"]).

        Returns:
            A list of dictionaries, where each dictionary represents a job posting.
            Minimally, each dictionary should contain:
            - 'title': str, The title of the job.
            - 'company': str, The name of the company.
            - 'location': str, The location of the job.
            - 'url': str, A URL to the job posting.
            - 'description_short': str, A brief description of the job.
        """
        pass

    @abstractmethod
    def get_job_details(self, job_url: str) -> dict:
        """
        Fetches detailed information for a specific job posting using its URL.

        Args:
            job_url: The URL of the job posting.

        Returns:
            A dictionary containing detailed information about the job.
            This could include keys like:
            - 'title': str
            - 'company': str
            - 'location': str
            - 'url': str
            - 'description_short': str
            - 'full_description': str, A more comprehensive description of the job.
            - 'posted_date': str, The date the job was posted (e.g., "2024-01-15").
            - Other relevant details like salary, benefits, specific requirements, etc.
        """
        pass

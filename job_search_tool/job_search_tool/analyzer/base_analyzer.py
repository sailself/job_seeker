# Base class for CV analyzers
from abc import ABC, abstractmethod

class CvAnalyzerBase(ABC):
    """
    Abstract base class for CV analyzers.
    Defines the interface that all CV analyzers must implement.
    """

    @abstractmethod
    def __init__(self, api_key: str):
        """
        Constructor for the CV analyzer.

        Args:
            api_key: The API key for the analysis service (e.g., Gemini API).
                     While the key might not be used by all stub implementations,
                     it's part of the interface for concrete classes that will use it.
        """
        pass

    @abstractmethod
    def is_cv_suitable(self, cv_text: str, job_description_text: str) -> tuple[bool, str]:
        """
        Analyzes if the provided CV text is suitable for the given job description text.

        Args:
            cv_text: A string containing the text of the CV.
            job_description_text: A string containing the text of the job description.

        Returns:
            A tuple containing:
            - bool: True if the CV is deemed suitable, False otherwise.
            - str: A brief justification, score, or summary of the analysis.
        """
        pass

    @abstractmethod
    def enhance_cv(self, cv_text: str, job_description_text: str) -> str:
        """
        Enhances the given CV text based on the job description text.

        Args:
            cv_text: A string containing the original text of the CV.
            job_description_text: A string containing the text of the job description.

        Returns:
            A string containing the enhanced CV text, tailored for the job.
        """
        pass

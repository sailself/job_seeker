# Concrete implementation of CvAnalyzerBase using a stubbed Gemini model
from .base_analyzer import CvAnalyzerBase

class GeminiCvAnalyzer(CvAnalyzerBase):
    """
    A stub implementation of CvAnalyzerBase that mimics interaction with Google's Gemini API.
    This class provides dummy analysis and enhancement for demonstration and testing.
    """

    def __init__(self, api_key: str):
        """
        Initializes the GeminiCvAnalyzer.

        Args:
            api_key: The API key for the Gemini service.
        """
        self.api_key = api_key
        if self.api_key == "YOUR_API_KEY_HERE" or not self.api_key:
            print("GeminiCvAnalyzer initialized (stub - placeholder API key)")
        else:
            print("GeminiCvAnalyzer initialized with a provided API key (stub).")

    def is_cv_suitable(self, cv_text: str, job_description_text: str) -> tuple[bool, str]:
        """
        Simulates checking if the CV is suitable for the job description.
        Returns a predefined tuple.
        """
        print(f"GeminiCvAnalyzer: Checking CV suitability (stub) for job description (first 100 chars): '{job_description_text[:100]}...'")
        # Simple logic for varied response, can be made more sophisticated
        if "Python" in cv_text and "developer" in job_description_text.lower():
            return (True, "This CV appears to be a good match based on keyword analysis (stub: found Python and developer).")
        elif "Engineer" in cv_text:
            return (True, "This CV mentions 'Engineer', which is promising (stub).")
        else:
            return (False, "The CV lacks specific skills or keywords mentioned in the job description (stub).")

    def enhance_cv(self, cv_text: str, job_description_text: str) -> str:
        """
        Simulates enhancing the CV based on the job description.
        Returns a string representing the "enhanced" CV.
        """
        print(f"GeminiCvAnalyzer: Enhancing CV (stub) based on job (first 100 chars): '{job_description_text[:100]}...'")
        
        enhancements = []
        if "Team Player" not in cv_text and "team" in job_description_text.lower():
            enhancements.append("* Added keyword: Team Player (simulated)")
        if "Project X" not in cv_text and "project x" in job_description_text.lower():
            enhancements.append("* Highlighted experience with Project X relevant to the job (simulated)")
        
        if not enhancements:
            enhancements.append("* Minor formatting adjustments for readability (simulated)")

        return f"--- Original CV Snippet ---\n{cv_text[:150]}...\n\n--- Enhancements based on Job Description (stub) ---\n" + "\n".join(enhancements)

if __name__ == '__main__':
    # Example usage for testing the GeminiCvAnalyzer
    print("--- Initializing GeminiCvAnalyzer with placeholder key ---")
    analyzer_stub = GeminiCvAnalyzer(api_key="YOUR_API_KEY_HERE")

    print("\n--- Initializing GeminiCvAnalyzer with a specific key ---")
    analyzer_real_key_stub = GeminiCvAnalyzer(api_key="FAKE_GEMINI_KEY_12345")

    cv_example = "Experienced Software Engineer with a background in Python, Java, and C++. Proven ability to lead projects and deliver high-quality software. Worked on Project Y."
    job_desc_example_good_match = "Seeking a Senior Python Developer with experience in leading projects. Must be a team player."
    job_desc_example_needs_enhancement = "We are looking for a software engineer with experience in Project X and cloud technologies. Team collaboration is key."
    job_desc_example_bad_match = "Urgently hiring a marketing specialist with social media expertise."

    print("\n--- Testing is_cv_suitable (Good Match) ---")
    suitable, reason = analyzer_stub.is_cv_suitable(cv_example, job_desc_example_good_match)
    print(f"Is suitable: {suitable}, Reason: {reason}")

    print("\n--- Testing is_cv_suitable (Bad Match) ---")
    suitable, reason = analyzer_stub.is_cv_suitable(cv_example, job_desc_example_bad_match)
    print(f"Is suitable: {suitable}, Reason: {reason}")

    print("\n--- Testing enhance_cv (Needs Enhancement) ---")
    enhanced_cv = analyzer_stub.enhance_cv(cv_example, job_desc_example_needs_enhancement)
    print(enhanced_cv)
    
    print("\n--- Testing enhance_cv (Good Match - fewer direct enhancements) ---")
    enhanced_cv_2 = analyzer_stub.enhance_cv(cv_example, job_desc_example_good_match)
    print(enhanced_cv_2)

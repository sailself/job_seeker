# Configuration settings for the Job Search Tool
import json

def load_config():
    """
    Loads configuration data from config.json, using defaults if the file
    is not found or is invalid.
    """
    default_config = {
        "target_country": "Any",
        "target_cities": ["Any"],
        "job_titles": ["Software Engineer", "Python Developer"],
        "cv_path": "path/to/your/cv.pdf",
        "gemini_api_key": "YOUR_API_KEY_HERE",  # IMPORTANT: Replace with your actual API key
        "output_file": "found_jobs.md"
    }

    config_file_path = "job_search_tool/config.json" # Path relative to the project root /app

    config = default_config.copy()

    try:
        # The config file is expected to be in the root of the project,
        # which is one level up from this script's directory.
        # So, we use ../config.json if this script is run from job_search_tool/job_search_tool/
        # However, tools run from /app, so we'll use "config.json" directly assuming the
        # CWD is the project root /app.
        # config.json is at /app/job_search_tool/config.json
        with open(config_file_path, 'r') as f:
            loaded_config = json.load(f)
            # Update only the keys present in the loaded JSON
            for key, value in loaded_config.items():
                if key in config: # Ensure we only update predefined keys
                    config[key] = value
                else:
                    print(f"Warning: Unknown configuration key '{key}' found in {config_file_path}. Ignoring.")
            print(f"Successfully loaded configuration from {config_file_path}")
    except FileNotFoundError:
        print(f"Warning: Configuration file '{config_file_path}' not found. Using default settings.")
    except json.JSONDecodeError:
        print(f"Warning: Error decoding JSON from '{config_file_path}'. Using default settings.")
    
    return config

if __name__ == '__main__':
    # This block is for testing the load_config function.
    # It will be executed when the script is run directly.
    # To run this from the repo root: python job_search_tool/job_search_tool/config.py
    print("Loading configuration...")
    config_settings = load_config()
    print("\nLoaded configuration settings:")
    for key, value in config_settings.items():
        print(f"- {key}: {value}")

    # Example of how to access a specific setting
    # print(f"\nTarget Country: {config_settings.get('target_country')}")
    # print(f"Gemini API Key (placeholder): {config_settings.get('gemini_api_key')}")

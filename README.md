# Quales-app-revamp
This automation script was developed to explore and validate Quales website functionalities efficiently
# Quales Website Automation Script

## Overview
This Python script automates the navigation and testing of the [Quales](https://quales.vercel.app/) website using Selenium. It interacts with various elements, including buttons, links, and sections, to verify their functionality.

## Features
- Launches the Quales website and maximizes the browser window.
- Clicks on the **Explore Talent** button.
- Navigates to and selects the **QA Engineer** section.
- Clicks on **Abati Adeotan Senayon** to view details.
- Finds and extracts the introduction paragraph for a QA Engineer.
- Clicks the **Use Cases** button.
- Finds the **Real-World Success Stories** section.
- Clicks on the **Thought Leadership** button.
- Scrolls down and back up to test scrolling functionality.
- Locates and clicks the **About Us** button.

## Prerequisites
Ensure you have the following installed before running the script:

- Python (>=3.7)
- Google Chrome browser
- Chrome WebDriver (matching your browser version)
- Required Python packages:

  ```sh
  pip install selenium
  ```

## Setup & Execution
1. Clone this repository or download the script.
2. Ensure Chrome WebDriver is in your system path.
3. Run the script using:

   ```sh
   python Quales.py
   ```

## Technologies Used
- **Python**: Programming language used for scripting.
- **Selenium WebDriver**: For automating browser interactions.
- **Google Chrome**: The browser used for testing.

## Notes
- The script includes delays (`time.sleep(3)`) to allow elements to load before interactions.
- Ensure the Quales website is accessible before running the script.
- Modify CSS selectors if the website structure changes.

## Author
Onyinye Sarah Azunna
onyinyeazunna5@gmail.com
Happy Coding! 🚀


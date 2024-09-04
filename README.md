# Twitter Search API

A minimum viable product written in Python using Django and the Django REST Framework with a SQLite database.

This project leverages the Twitter Search API to fetch recent tweets associated with high-traffic events and hashtags. It provides a RESTful API interface to search, store, filter, and export tweet data. The application is built using Python, Django, and Django REST Framework, with a SQLite database for data storage.

## Features

- **Search Twitter**: Fetch recent tweets based on specific hashtags or keywords related to trending topics.
- **Store and Retrieve**: Store retrieved tweets in a local SQLite database and retrieve them using customizable filters.
- **Export Data**: Export the filtered tweet data to a CSV file, selecting relevant columns for further analysis.
- **Simple REST API**: A set of API endpoints to interact with the tweet data, including search, retrieval, and export functionalities.

All below problem statements are covered:

- API 1 to trigger a Twitter search for recent high-traffic events. (e.g., #ElectionDay, #Elections2020, #TRUMP2020Landslide, #BidenHarris2020, etc., were high-traffic hashtags during the US Presidential elections 2020).
  - Example endpoints:
    - `http://127.0.0.1:8000/search/?query=TRUMP2020Landslide`
    - `http://127.0.0.1:8000/twitterDataStore/?query=BidenHarris2020`

- API 2 to return stored tweets and their metadata based on applied filters/search.
  - Example endpoints:
    - `http://127.0.0.1:8000/twitterSearch/`
    - `http://127.0.0.1:8000/twitterSearch/?search=ko`

- API 3 to export filtered data as CSV with selected columns of your choice (whichever columns make more sense to have in CSV, for someone who wants to perform some analysis on it).
  - Example endpoint:
    - `http://127.0.0.1:8000/twitterDataExport/`

## Project Structure

![Twitter Search API Logo](template/images/Project_Structure.jpg)


- Links are provided to run the API operations.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/twitter-search-api.git
   cd twitter-search-api

2. **Create and Activate a Virtual Environment:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

4. **Run Migrations:**
   ```bash
   python manage.py migrate

5. **Run the Development Server:**
   ```bash
   python manage.py runserver

## Usage
1. **Trigger a Twitter Search: Use the provided API endpoint to search for tweets based on a hashtag or keyword.**
   ```bash
   GET /search/?query=YourSearchQuery

2. **Retrieve Stored Tweets: Fetch tweets stored in the database with optional search parameters.**
    ```bash
   GET /twitterSearch/
   GET /twitterSearch/?search=YourKeyword

3. **Export Tweets to CSV: Export the stored tweets to a CSV file, specifying the columns you wish to include.**
   ```bash
   GET /twitterDataExport/

## Environment Variables

- Optional for this project.
   ```bash
   TWITTER_API_KEY: Your Twitter API key.
   TWITTER_API_SECRET_KEY: Your Twitter API secret key.
   TWITTER_ACCESS_TOKEN: Your Twitter access token.
   TWITTER_ACCESS_TOKEN_SECRET: Your Twitter access token secret.

## Testing
- To run the test suite, use the following command:
   ```bash
   python manage.py test
- Tests are provided to verify the functionality of the search, store, and export features.

## Contributions

- Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request with your changes. Ensure that your code is well-documented and includes relevant tests.

## Contact
- For any other information or support, please contact: dadananjesha.rymec@gmail.com








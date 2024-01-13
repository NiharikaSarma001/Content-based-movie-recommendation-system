# Content-based-movie-recommendation-system

## Overview

This repository contains the source code for a content-based movie recommendation system. The system leverages both demographic filtering and content-based filtering techniques to provide personalized movie suggestions.

### Features:

1. **Demographic Filtering:**
   - Utilizes movie popularity metrics (vote count and average) to recommend top-rated movies.
   - Provides a weighted rating system to ensure a balance between popularity and rating.

2. **Content-Based Filtering:**
   - Analyzes movie overviews using TF-IDF vectorization.
   - Computes cosine similarity to recommend movies based on their content.
   - Integrates additional metadata such as cast, crew, keywords, and genres for improved recommendations.

### Technologies Used:

- Python
- Flask (for web application)
- Pandas, NumPy (for data manipulation)
- Scikit-learn (for machine learning algorithms)
- HTML/CSS (for the user interface)

### How to Use:

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the Flask app (`app.py`) to launch the web interface.
4. Enter a movie title, and the system will provide personalized recommendations.

### Additional Information:

- The `movierec.py` script demonstrates the process of building the recommendation system, including data loading, preprocessing, and filtering techniques.
- The web interface (`index.html` and `results.html`) allows users to interact with the recommendation system.

---

## Deployment on Heroku

### Prerequisites

- [Heroku account](https://signup.heroku.com/)
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
- [Git](https://git-scm.com/)

### Steps

1. **Create a `requirements.txt` file:**
   ```bash
   pip freeze > requirements.txt

2. **Create a 'Procfile':**
   Create a file named Procfile (without any file extension) in your project directory and add the following line:
     web: gunicorn app:app

3. **Configure Heroku:**
  -> Log in to your Heroku account using the Heroku CLI:
     heroku login
  -> create a new heroku app:
     heroku create <your-app-name>

4. **Push to heroku:**
   git push heroku master

5. **Scale your application:**
   heroku ps:scale web=1

6. **Open your application:**
   heroku open

7. **Visit your deployed app:**
   You should now be able to visit your Flask app running on Heroku using the provided URL.

## Additional Information
The requirements.txt file lists all the required Python packages for your application.
The Procfile tells Heroku how to run your application using Gunicorn.
Ensure your Flask app instance is named app in your app.py file.

**Feel free to explore, contribute, or adapt this project to suit your needs!**

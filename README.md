his is a sentiment analysis web application developed using Dash, Plotly, and machine learning. 
The app allows users to visualize and classify reviews as either positive or negative, based on pre-trained models. 
It offers interactive components like pie charts and review submission areas to enhance user engagement.

Features
Pie Chart Visualization: Displays the proportion of positive and negative reviews.
Dropdown Selection: Allows users to select pre-existing reviews from a database and check their sentiment.
Text Area for Input: Users can enter custom reviews, and the system will classify them as positive or negative.
Pre-Trained Model Integration: Uses a machine learning model to predict sentiment based on user input.
Technologies Used
Dash: For building the web interface.
Plotly: For data visualization and creating interactive charts.
pandas: For handling the CSV data of reviews.
SQLite: To manage and query a local database of reviews.
Pickle: For loading the pre-trained machine learning model.
Scikit-learn: To transform text data and make predictions.
NumPy: For numerical operations.
Webbrowser: To automatically open the app in a web browser.
Setup Instructions
1. Clone the Repository
bash
Copy code
git clone https://github.com/your-repo-url.git
cd sentiment-analysis-app
2. Install Dependencies
Install the required Python libraries using pip:

bash
Copy code
pip install -r requirements.txt
Alternatively, you can install the following libraries manually:

bash
Copy code
pip install dash pandas plotly sklearn numpy sqlite3
3. Pre-Trained Model and Data
Ensure that the following files are in your project directory:

pickle_model.pkl: The pre-trained sentiment analysis model.
feature.pkl: Vocabulary for the sentiment analysis model.
balanced_reviews.csv: The dataset for reviews.
reviews2.db: SQLite database containing real reviews.
If any of these files are missing, the app won't function correctly.

4. Running the Application
To start the application, run the following command:

bash
Copy code
python app.py
Once the server starts, the application will automatically open in your default web browser. If it doesn't, you can access it manually by navigating to http://127.0.0.1:8050/ in your browser.

5. Usage Instructions
Select Review: Choose a review from the dropdown to analyze its sentiment.
Submit a Review: Enter your own review in the text area and click the "find_review" button to get its sentiment prediction.
View Pie Chart: The pie chart shows the distribution of positive and negative reviews.
File Structure
app.py: The main Python script that runs the Dash app.
pickle_model.pkl: The pre-trained machine learning model.
feature.pkl: The vocabulary file used for vectorizing reviews.
balanced_reviews.csv: CSV file containing reviews used for training and testing.
reviews2.db: SQLite database containing reviews.
Key Functions
load_model(): Loads the pre-trained machine learning model and vocabulary into memory.
check_review(reviewText): Predicts whether a given review is positive or negative.
reading_reviews(): Reads the review data from the CSV file and loads the SQLite database.
create_app_ui(): Builds the layout of the Dash application.
update_app_ui(): Updates the sentiment based on user input in the text area.
pie_chart(): Generates a pie chart of positive and negative review distributions.

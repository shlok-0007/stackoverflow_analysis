# Stack Overflow Data Analysis Dashboard

An interactive web application for analyzing and visualizing Stack Overflow survey data. This dashboard provides insights into technology trends, developer demographics, and programming language popularity based on Stack Overflow's annual developer survey.

## Project Structure

- `flask_app.py` - Main Flask application with data processing and API endpoints
- `index.html` - Interactive frontend with visualizations
- `data.csv` - Stack Overflow survey dataset (not tracked in Git)

## Key Features

- **Technology Trends Analysis**: Track the popularity of programming languages, frameworks, and tools over time
- **Developer Demographics**: Visualize developer experience, education, and employment statistics
- **Interactive Visualizations**:
  - Interactive bar and pie charts for categorical data
  - Time series analysis of technology adoption
  - Geographic distribution of developers
  - Salary comparison across different technologies and experience levels

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- Modern web browser with

## Data Description

The dataset includes responses from the Stack Overflow Annual Developer Survey, containing information about:
- Developer demographics (country, education, experience)
- Technology usage (programming languages, frameworks, databases)
- Job-related information (salary, company size, job satisfaction)
- Technology preferences and learning resources

## Data Setup

1. Download the `data.csv` file from [Google Drive](https://drive.google.com/file/d/19VepHq1S0mcyNF2b4Gh3jlbPNOWKmADH/view?usp=drive_link)
2. Place the downloaded `data.csv` file in the project root directory
3. The application will automatically load the data when started

> **Note:** The data file is not included in the repository due to its size. You must download it separately and place it in the project directory.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
   (Note: Create a `requirements.txt` file with your project's dependencies if you haven't already)

## Running the Application

1. Ensure your virtual environment is activated
2. Install the required packages:
   ```bash
   pip install flask pandas plotly
   ```
3. Run the Flask application:
   ```bash
   python flask_app.py
   ```
4. Open your web browser and navigate to `http://localhost:5000`

## Available Visualizations

1. **Technology Popularity**
   - Bar charts showing the most popular programming languages and frameworks
   - Year-over-year comparison of technology trends

2. **Salary Analysis**
   - Average salary by country and experience level
   - Salary distribution across different technologies
   - Impact of education and company size on compensation

3. **Developer Demographics**
   - Geographic distribution of developers
   - Experience level distribution
   - Education background analysis

4. **Technology Correlation**
   - Heatmaps showing relationships between different technologies
   - Most common technology stacks

## Data Sources
- Stack Overflow Annual Developer Survey Data
- Additional technology trend data from Stack Overflow Insights

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any questions or feedback, please contact [Shlok Gupta] at [shlokg62@gmail.com]

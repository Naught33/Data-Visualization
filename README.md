
# Interactive Data Visualization Application

The Interactive Data Visualization Application is a web-based tool developed to facilitate the exploration and analysis of a dataset through interactive charts and visualizations. The application is built using React for the frontend, Flask for the backend API, and D3.js for rendering the visualizations.

## Prerequisites

Before you begin, ensure you have the following software and tools installed:

- **Python**: You'll need Python along with Flask and SQLite3. You can download Python from the [official website](https://www.python.org/) and install Flask using `pip install flask flask-cors pandas numpy`.
- **Node.js**: The frontend of the application is built using React, which requires Node.js and npm (Node Package Manager). You can install Node.js from the [official website](https://nodejs.org/en/download/), which also comes with npm.

## Steps to Run the Application

Follow these steps to set up and run the interactive data visualization application:

### 1. Clone the Repository

Clone the repository containing the application source code:
```bash
git clone https://github.com/Freddie-hub/Data-Visualization.git

```

### 2. Setup the Backend (Flask API)

1. **Create Virtual Environment (Optional but Recommended)**

   It's a good practice to create a virtual environment to isolate the application's dependencies. This step is optional but recommended to avoid conflicts with other projects.

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

2. **Install Required Python Packages**

   Install the necessary Python packages for the backend API:

   ```bash
   pip install flask flask-cors pandas numpy
   ```

3. **Run the Flask API**

   Start the Flask API (backend server) that will handle requests from the frontend:

   ```bash
   python app.py
   ```

   The backend will be accessible at `http://127.0.0.1:5000`.

### 3. Setup the Frontend (React App)

1. **Install Required npm Packages**

   Navigate to the frontend directory and install the required npm packages for the React app:

   ```bash
   cd frontend
   npm install
   ```

2. **Start the React App**

   Run the React app, which will open a new browser window/tab with the application:

   ```bash
   npm start
   ```

   The React app will start at `http://localhost:3000`.

## Data Visualizations

The interactive data visualization application provides various types of visualizations to explore and analyze the dataset. Each visualization corresponds to a specific route in the Flask API and is accompanied by a React component for rendering.


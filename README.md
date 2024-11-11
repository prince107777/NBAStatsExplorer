# NBA Player Stats Analysis

This project is an NBA Player Stats Analysis application built using Python, Pandas, Matplotlib, and Seaborn. It allows you to load, clean, analyze, and visualize NBA player statistics data from the 2023-2024 NBA Playoffs. The application provides insights into player and team performance through various charts and statistical analysis.

## Project Overview

### NBADataLoader
The `NBADataLoader` class is responsible for loading and preprocessing the NBA player stats data. It allows you to:
- Load the data from a CSV file.
- Check for missing values and data types.
- Fill missing percentage values with zeros.
- Add a new column for rebounds per game (RPG) by summing offensive and defensive rebounds.

### NBADataAnalysis
The `NBADataAnalysis` class is the core of the analysis and visualization module. It offers several functionalities for analyzing and visualizing the data:
- Display data summaries and column descriptions.
- Visualize the top players based on specific stats (e.g., points per game).
- Create bar charts for categorical data, like player positions.
- Generate average stats (e.g., points, assists, rebounds) by team or age group.
- Create a heatmap for the correlation matrix of the stats.
- Visualize shooting efficiency with scatter plots.
- Display team performance summaries and stat leaderboards.

### Project Flow
1. **NBADataloader.py**: First, run the `NBADataloader.py` file to load and preprocess the data.
2. **NBADataAnalysis.py**: Once the data is loaded and processed, the analysis can be performed by running the `NBADataAnalysis.py` file.
3. **project.py**: This file serves as the main entry point for the project. It will allow you to interact with the program and choose the various analysis and visualization options.

## Features

- **Data Loading and Preprocessing**: 
    - Load data from a CSV file with custom encoding and delimiters.
    - Check for null values and data types.
    - Fill missing values in percentage columns with zeros.
    - Add a new "Rebounds per Game" (RPG) column.

- **Data Analysis and Visualization**: 
    - Display a summary of the data.
    - Plot top players based on a specific stat (e.g., points, assists).
    - Visualize the distribution of categorical columns (e.g., player position).
    - Display average stats (e.g., points, assists, rebounds) by team, age, and other categories.
    - Generate a correlation matrix heatmap for numerical stats.
    - Visualize shooting efficiency with scatter plots.

- **Team and Player Performance**:
    - Display team performance summary based on various stats.
    - Show top players' stat leader tables.


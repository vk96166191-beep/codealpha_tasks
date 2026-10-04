# Netflix Movies and TV Shows — Exploratory Data Analysis

## 📌 Project Overview

This project performs Exploratory Data Analysis (EDA) on the Netflix Movies and TV Shows dataset.

The objective is to understand the distribution, trends, ratings, genres, countries, movie durations, TV show seasons, and content addition patterns in the Netflix dataset.

## 🎯 Objectives

- Analyze Movies vs TV Shows distribution
- Explore release year trends
- Identify top countries associated with Netflix titles
- Analyze popular genres
- Study rating distribution
- Analyze movie duration
- Analyze TV show seasons
- Study Netflix content addition trends
- Identify and handle data quality issues

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## 📂 Dataset

The dataset contains information about Netflix titles, including:

- Title
- Content Type
- Director
- Cast
- Country
- Date Added
- Release Year
- Rating
- Duration
- Genre
- Description

Dataset size: **8,807 titles**

## 📊 Analysis Performed

### 1. Movies vs TV Shows

Movies represent the majority of titles in the dataset, while TV Shows form a smaller portion.

### 2. Release Year Analysis

The analysis explores how Netflix titles are distributed across their original release years.

### 3. Country Analysis

The United States has the highest number of associated titles, followed by India.

### 4. Genre Analysis

International Movies, Dramas, and Comedies are among the most common categories.

### 5. Rating Analysis

TV-MA is the most common rating, followed by TV-14.

### 6. Movie Duration

The average movie duration is approximately 99.6 minutes, while the median is approximately 98 minutes.

### 7. TV Show Seasons

Most TV Shows in the dataset have one season.

### 8. Content Addition Trends

The number of titles added to Netflix increased significantly after 2015, with 2019 having the highest number of additions in this dataset.

## 🧹 Data Cleaning

During the analysis, the following data quality issues were identified:

- No duplicate rows were found.
- Missing values were identified in several columns.
- Three records contained duration values incorrectly stored in the rating column.
- These values were corrected by moving them to the duration column.
- The original dataset was preserved, while a cleaned copy was created for further analysis.

## 📁 Project Structure

```text
CodeAlpha_EDA_Netflix/
│
├── Dataset/
│   └── netflix_titles.csv
│
├── Charts/
│   ├── movies_vs_tv_shows.png
│   ├── release_year_trend.png
│   ├── top_10_countries.png
│   ├── top_10_genres.png
│   ├── movie_duration_distribution.png
│   ├── tv_show_seasons.png
│   ├── titles_added_by_year.png
│   ├── movies_vs_tv_added_by_year.png
│   ├── rating_distribution.png
│   ├── rating_by_type.png
│   ├── release_year_by_type.png
│   └── top_10_genres_by_type.png
│
├── Notebooks/
│   └── Netflix_EDA.ipynb
│
└── README.md
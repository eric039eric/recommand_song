# recommand_song# 🎧 Simple Music Recommender

A lightweight content-based music recommendation system based on user preferences and audio feature vectors. This project demonstrates how to build a basic recommendation engine using cosine similarity, and is ideal for learning the fundamentals of recommender systems.

## 🧠 Overview

This project allows you to input a list of songs you like, and it will recommend similar songs based on their stylistic features (e.g., instrumental, metal, lo-fi, emotional, etc.).  
It uses **content-based filtering** by converting songs into feature vectors and computing **cosine similarity** to rank recommendations.

## 🚀 Features

- Simple and fully interpretable algorithm (no black-box models)
- Easy to customize: add your own songs and features
- Pure Python implementation (no deep learning required)
- CLI interface with straightforward output
- Educational structure for beginners in machine learning or data science

## 📊 How It Works

1. **Song Feature Encoding**  
   Each song is represented by a 7-dimensional vector:
[Instrumental, Metal, Lo-fi, Emotional, Experimental, Electronic, Anthemic]


2. **User Profile Generation**  
The system computes the **average vector** of the songs the user likes.

3. **Similarity Computation**  
Cosine similarity is used to compare the user’s preference vector with all other songs.

4. **Top-k Recommendation**  
The system returns the top N songs with the highest similarity scores.

## 🧪 Example

```bash
推薦給你的歌曲：
- Crush (COVER)              (相似度: 0.98)
- All Falls Apart            (相似度: 0.96)
- Metal in Inappropriate Places (相似度: 0.86)

## 🧰 Requirements
- Python 3.7+

- scikit-learn

- numpy

## Install dependencies:

- pip install -r requirements.txt

If you don’t have requirements.txt, you can manually install:

- pip install numpy scikit-learn


## 📝 How to Use

Clone the repository:

- git clone https://github.com/your_username/simple-music-recommender.git
- cd simple-music-recommender
Edit recommend_song.py and update the user_likes list with your favorite songs.

Run the script:


- python recommend_song.py


## 📁 File Structure

recommend_song.py       # Main script
README.md               # Project documentation


## 🔧 Customization Ideas
Add more songs with different genres

Use real metadata from Spotify, Last.fm, etc.

Replace CLI with a web interface (e.g., Flask, Streamlit)

Add logging, testing, or packaging for production

## 📚 Educational Value
This project is ideal for:

Students learning recommendation systems

Developers prototyping music or media apps

Anyone curious about how YouTube/Spotify-like algorithms work

##📄 License
This project is released under the MIT License.

Created by [eric039eric], inspired by real-world music discovery logic.
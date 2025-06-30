import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# 建立歌曲資料庫，每首歌都有一組風格向量 (Instrumental, Metal, Lo-fi, Emotional, Experimental, Eletronic, Anthemic)
songs = {
    "Neurotica":                [1.0, 0.5, 0, 0.3, 0.7, 0.2, 0.1],
    "All Falls Apart":          [1.0, 0.8, 0, 0.4, 0.5, 0.1, 0.1],
    "Up From the Bottom":       [0, 0.6, 0, 0.7, 0.3, 0.5, 0.7],
    "In My Remains":            [0, 0.7, 0, 0.8, 0.2, 0.3, 1.0],
    "Metal in Inappropriate Places": [0.5, 1.0, 0, 0.2, 1.0, 0.1, 0],
    "You inspire me (lofi)":    [0, 0, 1.0, 0.5, 0.1, 0, 0],
    "Heavy Is the Crown":       [0, 0.6, 0, 0.7, 0.2, 0.2, 0.8],
    "From the Inside":          [0, 0.7, 0, 0.9, 0.1, 0.2, 0.9],
    "Crush (COVER)":            [1.0, 0.6, 0, 0.3, 0.6, 0, 0.1],
}

# 使用者喜歡的歌曲清單 (可自行更改)
user_likes = ["Neurotica", "From the inside"]

# 建立使用者的平均偏好向量
def get_user_profile(song_db, like_songs):
    vectors = [song_db[song] for song in like_songs if song in song_db]
    return np.mean(vectors, axis=0).reshape(1, -1)

user_profile = get_user_profile(songs, user_likes)

# 計算推薦結果
def recommand_songs(user_vector, song_db, liked_songs, top_k=3):
    results = []
    for song, vector in song_db.items():
        if song in liked_songs:
            continue
        sim = cosine_similarity(user_vector, np.array(vector).reshape(1, -1))[0][0]
        results.append((song, sim))
    return sorted(results, key=lambda x:x[1], reverse=True)[:top_k]

# 取得推薦歌曲
recommandations = recommand_songs(user_profile, songs, user_likes)

# 顯示結果
print("推薦給你的歌曲:")
for song, score in recommandations:
    print(f"- {song} (相似度: {score:.2f})")
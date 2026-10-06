import pandas as pd
import numpy as np
df = pd.read_csv("day02_usage.csv")
chat_usage = df["Chat"].to_numpy()
video_usage = df["Video"].to_numpy()
study_usage = df["Study"].to_numpy()
games_usage = df["Games"].to_numpy()
print("Chat Usage:", len(chat_usage))
print("Total Chat Usage", np.sum(chat_usage))

print("Total Video Usage", np.sum(video_usage))

print("Total Study Usage", np.sum(study_usage))

print("Total Games Usage", np.sum(games_usage))

print(f"Average Chat Usage: {np.mean(chat_usage):.1f}")
print(f"Average Video Usage: {np.mean(video_usage):.1f}")
print(f"Average Study Usage: {np.mean(study_usage):.1f}")
print(f"Average Games Usage: {np.mean(games_usage):.1f}")
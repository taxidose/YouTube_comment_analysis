import pandas as pd
import os


PATH = "C:\\Users\\taxi\\PycharmProjects\\youtube\\scraped_comments"


def csv_to_df(path):
    return pd.read_csv(path)
    
    
def folder_to_df(path=None):
    if path is None:
        path = "./scraped_comments"

    files = os.listdir(path)
    print(f"{files=}")
    df = pd.DataFrame(columns=["Datetime", "Comment", "Authorname", "Author-ID", "Video-ID"])
    for file in files:
        print(f"reading {file}...")
        df_new = csv_to_df(f"{path}/{file}")
        video_id = file[:len(file)-11]
        df_new["Video-ID"] = video_id
        df = df.append(df_new, ignore_index=True)
        print(f"{file} finished...")

    print("all files read... returning df...")

    return df
    
    
df = folder_to_df(PATH)
print(df.columns)

df["Authorname"].value_counts()

df["Authorname"].value_counts().head(50)

author_group = df.groupby(["Authorname"])

filt = df["Authorname"] == "Demolition Man"
df.loc[filt]["Video-ID"].value_counts()

author_group["Video-ID"].value_counts().sort_values(ascending=False).head(50)

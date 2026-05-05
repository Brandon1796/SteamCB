
from pathlib import Path
import requests
import pandas as pd
from datetime import datetime


def fetch_steamspy_data(versioned=False):

    # ------------------------
    # Detect project root
    # ------------------------
    base_path = Path().resolve().parent

    raw_path = base_path / "data" / "raw"
    processed_path = base_path / "data" / "processed"

    raw_path.mkdir(parents=True, exist_ok=True)
    processed_path.mkdir(parents=True, exist_ok=True)

    # ------------------------
    # API request
    # ------------------------
    url = "https://steamspy.com/api.php?request=all"
    response = requests.get(url)
    data = response.json()

    # ------------------------
    # DataFrame
    # ------------------------
    df = pd.DataFrame.from_dict(data, orient="index")

    # ------------------------
    # Save file
    # ------------------------
    if versioned:
        date = datetime.now().strftime("%Y_%m_%d")
        output_file = raw_path / f"steamspy_games_{date}.csv"
    else:
        output_file = raw_path / "steamspy_games.csv"

    df.to_csv(output_file, index=False)

    print(f"Data saved at: {output_file}")

    return df

if __name__ == "__main__":
    df = fetch_steamspy_data(versioned=True)
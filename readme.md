
# Visual Analysis of Steam Games: Engagement, Pricing & Genre Trends

Tableau public dashboard link: https://public.tableau.com/app/profile/sakibur.rahman5899/viz/GameDataVisualization_17644487283440/Dashboard2

I have used 35357 rows of game data for the analysis

The goal of this dashboard is to analyze video-game market trends using scraped game-level data from [SteamDB](https://steamdb.info/).
It focuses on highlighting:

    1. Which genres have the highest revenue potential
    2. How game revenue and pricing evolved over time
    3. Which individual games achieved the highest peak player counts
    4. How online activity relates to genre and pricing patterns

The dashboard acts as a centralized visual tool for identifying what types of games perform well, what trends dominate the industry, and how players engage with different genres.

## Key Findings:
1. Certain Genres Show Significantly Higher Revenue Potential
Genres like Action RPG, FPS, Action-Adventure, and Sandbox show exceptionally high average revenue.
These genres also tend to have high average online presence, indicating strong ongoing engagement.

2. Online Activity & Revenue Tend to Move Together
Genres with high revenue also typically have high average current online players.
This suggests that engaged communities directly contribute to long-term sales performance.

3. Revenue Peaked in Modern Gaming Eras
Revenue per game saw a rise from mid-2000s to late 2010s, peaking around 2015–2019.
Recent years show a slight decline.

4. Average Game Price Has Been Slowly Increasing
Prices climbed steadily from the 1990s onward.
From around $5–15 historically → to $20–60 in the modern era.

## Prerequisites
- Python 3.8 or higher
- pip package manager
- Git

## Setup Steps

1. **Clone the repository**
    ```bash
    git clone <repository-url>
    cd <Folder_name>
    ```

2. **Create virtual environment**
    ```bash
    python -m venv venv
    ```

3. **Activate virtual environment**
    ```bash
    # On Windows
    venv\Scripts\activate
    
    # On macOS/Linux
    source venv/bin/activate
    ```

4. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## Troubleshooting
For issues, check the documentation or open an issue on GitHub.

## Additional Resources
- [Python Virtual Environment Guide](https://docs.python.org/3/tutorial/venv.html)
- [pip Documentation](https://pip.pypa.io/en/stable/documentation/)
- [Python Dependencies Guide](https://packaging.python.org/en/tutorials/managing-dependencies/)


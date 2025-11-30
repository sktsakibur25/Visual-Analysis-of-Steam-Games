from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Initialize the driver
driver = webdriver.Chrome()

try:
    # Navigate to your target website
    driver.get("https://steamdb.info/tags/")
    
    # Wait for the element to be present
    wait = WebDriverWait(driver, 10)
    taglist_element = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "taglist-wrap"))
    )
    
    # Scrape all tags within the taglist-wrap class
    tags = taglist_element.find_elements(By.TAG_NAME, "a")

    genre = [
        'Puzzle', 'Action-Adventure', 'Arcade', 'Shooter', 'Platformer',
        'Visual Novel', 'Roguelike', 'Sandbox', 'Action RPG', 'Point & Click',
        'Action Roguelike', 'Interactive Fiction', 'Turn-Based Strategy', 'Tabletop',
        'Dating Sim', 'Walking Simulator', 'JRPG', 'Education', 'Party-Based RPG',
        'Card Game', 'Life Sim', 'Design & Illustration', 'Strategy RPG', 'Utilities',
        'Board Game', 'RTS', 'Tower Defense', 'City Builder', 'Web Publishing',
        "Beat 'em up", 'Automobile Sim', '2D Fighter', 'Rhythm', 'Farming Sim',
        '3D Fighter', 'Auto Battler', 'Word Game', 'eSports', 'Colony Sim',
        'Grand Strategy', 'Space Sim', 'Animation & Modeling', 'MMORPG',
        'Battle Royale', 'Audio Production', 'God Game', 'Party Game',
        'Video Production', '4X', 'MOBA', 'Photo Editing'
    ]

    desired = ['Name', 'Price', 'Rating', 'Release', 'Follows', 'Online', 'Peak']
    games_data = []

    # Extract and print tag data
    for tag in tags:
        tag_text = tag.text.split()[-1]
        tag_link = tag.get_attribute("href")
        if tag_text in genre:
            driver.get(tag_link)
            genre_games_tr = wait.until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "app"))
            )
            # games_data is now a global variable, no initialization needed here
            for game in genre_games_tr:
                try:
                    tds = game.find_elements(By.TAG_NAME, "td")
                    name = tds[2].find_element(By.TAG_NAME, "a").text
                    price = tds[4].text
                    rating = tds[5].text
                    release = tds[6].text
                    follows = tds[7].text
                    online = tds[8].text
                    peak = tds[9].text
                    
                    games_data.append({
                        'Genre': tag_text,
                        'Name': name,
                        'Price': price,
                        'Rating': rating,
                        'Release': release,
                        'Follows': follows,
                        'Online': online,
                        'Peak': peak
                    })
                    print(f"Scraped {name} from genre {tag_text}")
                except:
                    continue

    df = pd.DataFrame(games_data)
    print(df.head())
    # df.to_csv(f'{tag_text}_games.csv', index=False)
    
finally:
    driver.quit()
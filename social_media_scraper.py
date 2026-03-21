from bs4 import BeautifulSoup
import csv

# Load the HTML file
def load_html(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return content

# Extract Posts
def extract_posts(soup):
    posts = []
    post_elements = soup.find_all("div", class_="post")
    for post in post_elements:
        username = post.find("h2", class_="username").text.strip()
        content = post.find("p", class_="content").text.strip()
        timestamp = post.find("span", class_="timestamp").text.strip()
        posts.append({"username": username, "content": content, "timestamp": timestamp})
    return posts

# Save Posts to CSV
def save_posts_to_csv(posts, output_path):
    with open(output_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["username", "content", "timestamp"])
        writer.writeheader()
        writer.writerows(posts)

# Main Function
def main():
    print("Social Media Scraper")
    html_content = load_html("social_media.html")
    soup = BeautifulSoup(html_content, "html.parser")
    posts = extract_posts(soup)
    save_posts_to_csv(posts, "social_media_posts.csv")
    print("Posts saved to social_media_posts.csv")

if __name__ == "__main__":
    main()











# html_content = load_html("social_media.html")
# soup = BeautifulSoup(html_content, "html.parser")
# posts = extract_posts(soup)
# save_posts_to_csv(posts, "social_media_posts.csv")
# print("Posts saved to social_media_posts.csv")


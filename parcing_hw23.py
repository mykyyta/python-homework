import requests
from bs4 import BeautifulSoup

URL = "https://scipost.org/atom/publications/comp-ai"

def parse_feed(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "xml")  # Використовуємо lxml для XML
    articles = []

    for entry in soup.find_all("entry"):
        title = entry.find("title").text.strip() if entry.find("title") else "No title"
        link = entry.find("link")["href"] if entry.find("link") else "No link"
        summary = entry.find("summary").text.strip() if entry.find("summary") else "No summary"

        articles.append({
            'title': title,
            'link': link,
            'summary': summary
        })

    return articles


def main():
    articles = parse_feed(URL)

    for article in articles:
        print(f"Title: {article['title']}")
        print(f"Link: {article['link']}")
        print(f"Summary: {article['summary']}")
        print("-" * 80)


if __name__ == "__main__":
    main()

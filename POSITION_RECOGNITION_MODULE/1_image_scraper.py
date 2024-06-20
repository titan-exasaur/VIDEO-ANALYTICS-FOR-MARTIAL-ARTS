import requests
from bs4 import BeautifulSoup

def get_image_urls(keyword):
    search_url = f"https://www.google.com/search?hl=en&q={keyword}&tbm=isch"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(search_url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch search results for keyword: {keyword}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all("img")

    urls = []
    for img in img_tags:
        img_url = img.get("src")
        if img_url and any(img_url.endswith(ext) for ext in [".jpg", ".jpeg", ".png"]):
            urls.append(img_url)

    return urls

def save_urls_to_file(urls, filename):
    with open(filename, 'w') as file:
        for url in urls:
            file.write(url + "\n")

def main():
    keyword = input("Enter a keyword to search for images: ")
    image_urls = get_image_urls(keyword)
    
    if image_urls:
        save_urls_to_file(image_urls, f"{keyword}_image_urls.txt")
        print(f"Image URLs saved to {keyword}_image_urls.txt")
    else:
        print("No image URLs found.")

if __name__ == "__main__":
    main()

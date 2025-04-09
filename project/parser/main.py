import requests
from bs4 import BeautifulSoup

url = "https://amazon.com/s?k=smartphones&crid=13O8GM23TWYKS&qid=1744047268&rnid=2491154011&sprefix=smartphone%2Caps%2C349&ref=sr_nr_p_36_0_0&low-price=530&high-price="

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Connection": "keep-alive",
}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, "html.parser")
title_element = soup.find_all("h2", class_=["a-size-medium", "a-spacing-none", "a-color-base", "a-text-normal"])
titles = []
'''for elem in title_element:
    if elem:
        if elem.text != "More results":
            titles.append(elem.text.strip())
        else:
            continue
    else:
        print("Title not found")

clean_titles = titles[2:len(titles)-2]
print(clean_titles)
print(len(clean_titles))'''

pr = []
prices = soup.find_all("span", class_=["a-price-whole"])
for price in prices:
    if price:
        pr.append(price.text)
    else:
        print("Price not found")

'''images = soup.find_all("img", class_=["s-image"])
for i, image in enumerate(images):
    if image and image.get("src"):

        try:
            img_response = requests.get(image["src"], stream=True)
            img_response.raise_for_status()

            image_path = "C:\Coding\Python\OOP\parser\imgs\image_" + str(i) + ".jpg"
            with open(image_path, "wb") as file:
                for chunk in img_response.iter_content(1024):
                    file.write(chunk)

            print(f"Downloaded: {image_path}")
        except Exception as e:
            print(f"Failed to download {image['src']}: {e}")
    else:
        print("Image not found")'''

print(pr)
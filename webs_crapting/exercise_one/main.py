from bs4 import BeautifulSoup

with open("index.html", encoding="utf8") as file:
    all_data = file.read()

soup = BeautifulSoup(all_data, "html.parser")
# print(soup.prettify())
# print(soup.title)
# print(soup.title.string)
# print(soup.title.name)

all_anchor_tags = soup.find_all("a")
# print(all_anchor_tags)
# for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.get(text))

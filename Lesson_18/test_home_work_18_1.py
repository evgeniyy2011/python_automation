import requests

BASE_URL = "https://images-api.nasa.gov"

# Пошук зображень
search_url = f"{BASE_URL}/search"
search_params = {
    "q": "Curiosity rover Mars",  # пошуковий запит
    "media_type": "image",  # тільки зображення
    "page_size": 20  # щоб було з чого вибрати
}

# Отримання файлів по nasa_id
asset_url_template = f"{BASE_URL}/asset/{{nasa_id}}"

def test_status_code():
   response = requests.get(BASE_URL)
   print(response.status_code)
   assert response.status_code == 200, f"Sended request to {BASE_URL}, Status code is {response.status_code}"

def test_rover():
    search = search_params
    response = requests.get(search_url, params=search)
    json_searach = response.json()
    photo_number = 1
    for i in json_searach["collection"]["items"][:2]:
        id = i["data"][0]["nasa_id"]
        end_point_id= asset_url_template.format(nasa_id = id)
        get_list_links = requests.get(end_point_id)
        links_json = get_list_links.json()
        jpg_link = links_json["collection"]["items"]
        for links in jpg_link:
            href = links["href"]
            if href.lower().endswith(".jpg"):
                download = requests.get(href)
                file = f"mars_photo{photo_number}.jpg"
                with open(file, mode="wb") as f:
                     f.write(download.content)
                photo_number +=1
                break
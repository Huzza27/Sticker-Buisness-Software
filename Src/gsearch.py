import os
import requests
from bs4 import BeautifulSoup
from PIL import Image
import io
import time
from new import select_image

# Specify the User-Agent to mimic a browser
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

def save_image_from_content(content, path, format='JPEG'):
    try:
        image = Image.open(io.BytesIO(content))
        image.save(path)
        print(f"Image successfully saved to {path}")
        return True
    except IOError as e:
        print(f"Cannot convert and save the image: {e}")
        return False

def download_image(url, folder_path, image_number):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    try:
        response = requests.get(url, stream=True, headers=HEADERS)
        if response.status_code == 200:
            content_type = response.headers.get('content-type')
            extension = {
                'image/jpeg': '.jpg',
                'image/png': '.png',
                'image/gif': '.gif'
            }.get(content_type, '.jpg')  # Default to .jpg if content type is not known

            # Generate a filename using image_number
            filename = f"image{image_number}{extension}"
            filepath = os.path.join(folder_path, filename)

            # Save the image using PIL
            if save_image_from_content(response.content, filepath, extension):
                print(f"Image successfully saved to {filepath}")
                return True
        else:
            print(f"Failed to download image {url}: Status code {response.status_code}")
        return False
    except Exception as e:
        print(f"Failed to save image {url}: {e}")
        return False

def search_and_download_images(term, folder_path, num_images=50):
    url = 'https://www.google.com/search?tbm=isch'
    escaped_term = term.replace(' ', '+')
    images = []
    image_counter = 1  # Initialize image counter

    response = requests.get(url, headers=HEADERS, params={'q': escaped_term, 'num': num_images})
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        for img in soup.find_all('img'):
            img_url = img.get('src')  # Adjust attribute if needed based on Google's HTML structure
            if img_url and download_image(img_url, folder_path, image_counter):
                images.append(img_url)
                image_counter += 1  # Increment the counter with each successful download
            if len(images) >= num_images:
                break
    else:
        print(f"Failed to retrieve images. Status code: {response.status_code}")
    return images

if __name__ == "__main__":
    search_term = "go be awesome"
    target_directory = r"D:\Scott Project\Sticker Buisness\Stickers\Stickers\Web Scraper Images"
    downloaded_images = search_and_download_images(search_term, target_directory, 50)
    print(f"Downloaded {len(downloaded_images)} images to '{target_directory}' for the search term '{search_term}'.")

    #select_image()

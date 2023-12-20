import unittest
import os
from main import download_image, crawl_vitamin_c_products
import config

class TestWebScraper(unittest.TestCase):

    def test_download_image_success(self):
        # Čia naudojamas realus vaizdo URL testavimui
        test_url = "https://example.com/test.jpg"  # Pakeiskite šį URL realiu vaizdo URL
        test_folder = config.IMAGE_FOLDER
        test_file_name = "test.jpg"

        if not os.path.exists(test_folder):
            os.makedirs(test_folder)

        result = download_image(test_url, test_folder, test_file_name)

        # Patikrinama, ar funkcija grąžina kelio į failą reikšmę
        self.assertIsNotNone(result)

        # Patikrinama, ar failas buvo sukurtas
        self.assertTrue(os.path.exists(os.path.join(test_folder, test_file_name)))

        # Išvaloma testavimo aplinka
        os.remove(os.path.join(test_folder, test_file_name))
        os.rmdir(test_folder)

    def test_download_image_failure(self):
        # Testas su neteisingu URL
        test_url = "https://example.com/nonexistent.jpg"
        test_folder = config.IMAGE_FOLDER
        test_file_name = "test.jpg"

        result = download_image(test_url, test_folder, test_file_name)

        # Tikimasi, kad rezultatas bus None
        self.assertIsNone(result)

    def test_crawl_vitamin_c_products(self):
        # Testas priklauso nuo išorinio šaltinio, todėl jis gali būti nestabilus
        time_limit = config.TIME_LIMIT
        source = config.SOURCE_URL
        return_format = config.RETURN_FORMAT
        download_images = config.DOWNLOAD_IMAGES

        result = crawl_vitamin_c_products(time_limit, source, return_format, download_images)

        # Tikrinama, ar grąžinamas rezultatas yra tikėtinas
        # Priklauso nuo funkcijos išėjimo formatų
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
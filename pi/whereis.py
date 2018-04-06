import epd2in13
import time
import Image
import ImageDraw
import ImageFont

try:
    import requests
except ImportError:
    exit("This script requires the requests module\nInstall with: sudo pip install requests")

def get_location():
    url = 'https://where.example.com/api/location.json?auth_token=xxxxxxxxxxx'
    res = requests.get(url)
    if(res.status_code == 200):
        json_data = json.loads(res.text)
        return json_data
    return {}


def main():
    epd = epd2in13.EPD()
    epd.init(epd.lut_full_update)

    image = Image.new('1', (epd2in13.EPD_HEIGHT, epd2in13.EPD_WIDTH), 255)  # clear the frame

    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('/usr/share/fonts/AmaticSC-Bold.ttf', 40)
    draw.rectangle((0, 0, 250, 60), fill = 0)
    draw.text((30, 10), 'WHERE IS FOO?', font = font, fill = 255)

    data = get_location()
    ds = "unknown"
    print(data)

    if(u'description' in data):
       print(data["description"])
       ds = data["description"]

    draw.text((30, 60), ds, font = font, fill = 0)
    img = image.rotate(90,expand=True)
    epd.set_frame_memory(img, 0, 0)
    epd.display_frame()
    epd.set_frame_memory(img, 0, 0)

    epd.display_frame()

if __name__ == '__main__':
    main()


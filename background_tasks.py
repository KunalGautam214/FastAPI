from fastapi import FastAPI, BackgroundTasks, status
import requests
import time

app = FastAPI()

image_url = [
    "https://images.unsplash.com/photo-1729608462362-21193b628e56",
    "https://images.unsplash.com/photo-1730829382600-331831cfa0e4",
    "https://images.unsplash.com/photo-1730724583278-151efd042e16",
    "https://images.unsplash.com/photo-1730463825700-89c6523d6f19",
    "https://images.unsplash.com/photo-1731084901083-cabdd7f51f91",
    "https://images.unsplash.com/photo-1730544531296-ea17ddc154fd",
    "https://images.unsplash.com/photo-1730918404452-af022c11f4a4",
    "https://images.unsplash.com/photo-1730882884953-378e5349a0a8",
    "https://images.unsplash.com/photo-1730801477851-abbfe1873fa5",
    "https://images.unsplash.com/photo-1730724742886-b0e36d1eb067",
    "https://images.unsplash.com/photo-1731000891359-b430173e8491"
]


async def download_images(image_urls):
    start = time.time()
    for img_url in image_urls:
        img_name = img_url.split('/')[3]
        img_name = f'{img_name}.jpg'
        byte_img = requests.get(img_url).content
        with open(img_name, 'wb') as img_file:
            img_file.write(byte_img)
            print(f'{img_name} downloaded')
    end = time.time() - start
    print('Total time taken', end)


@app.post('/download', status_code=status.HTTP_202_ACCEPTED)
async def download(image_urls: list[str], background_task: BackgroundTasks):
    background_task.add_task(download_images, image_urls)
    return {'message': 'Images has been downloaded'}

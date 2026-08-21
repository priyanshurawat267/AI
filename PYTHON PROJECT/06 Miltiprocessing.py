
import multiprocessing
import requests
import os

def downloadFile(url, name):
    print(f"Started downloading: {name}")
    response = requests.get(url)
    with open(f"files/file{name}.jpg", "wb") as f:
        f.write(response.content)
    print(f"Finished downloading: {name}")
if __name__ == "__main__":
    # Create files folder if it doesn't exist
    os.makedirs("files", exist_ok=True)
    url = "https://picsum.photos/2000/3000"
    process = []
    # Create 3000 processes
    for i in range(1000):
        p = multiprocessing.Process(
            target=downloadFile,
            args=(url, i)
        )
        p.start()
        process.append(p)
    # Wait for all processes to finish
    for p in process:
        p.join()
    print("Download file successful!")

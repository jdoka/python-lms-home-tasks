import requests
import time

# поместить проверяемый файл в директорию со скриптом, подставить пароль архива и ключ апи
filename = "protected_archive.zip"
url = "https://www.virustotal.com/api/v3/files"
api_key = "fix"
password = "fix"


def check_anti_viruses():
    files = {"file": (filename, open(filename, "rb"), "application/zip")}
    payload = {"password": password}
    headers = {
        "accept": "application/json",
        "x-apikey": api_key
    }
    uploaded_file = requests.post(url, data=payload, files=files, headers=headers)

    response = requests.get(uploaded_file.json()["data"]["links"]["self"], headers=headers)
    while response.json()["data"]["attributes"]["status"] == "queued":
        time.sleep(5)
        response = requests.get(uploaded_file.json()["data"]["links"]["self"], headers=headers)

    for i, anti_virus in enumerate(["McAfee", "Fortinet", "Yandex", "Sophos"]):
        detected = response.json()["data"]["attributes"]["results"][anti_virus]["category"]
        print(f"{i + 1}. {anti_virus}:  {detected}")


check_anti_viruses()

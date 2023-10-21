import requests
import json

def SendMessageWhatsapp(data):
    try:
        token = "EABa9LgZCfMOIBO0PVfDBgiyqpRUCtfunZAr0MUZB3FfZBDfPTps0d9Go2YYf85oFdZBXZBD5pTSei5BJIrHGolZCTjzslGEGkyvbqNeAfrv20ZCXHMAFDvMrKUtrvtE12pWYqTZBFjh6nUNhI9NPfnnbzduGIOp1Kps9k7O9AaFSEgyE9JxfyGZCaO6WocOXmmkUon8CSpVNEYCegtZBifo"
        api_url = "https://graph.facebook.com/v17.0/128396703696550/messages"
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        response = requests.post(api_url, data = json.dumps(data), headers = headers)
        if response.status_code == 200:
            return True
        
        return False
    except Exception as exception:
        print(exception)
        return False
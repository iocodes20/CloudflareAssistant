import sys
import requests

def SSLTLS_enable(email, AUTH_TOKEN, hostname):

    url = "https://api.cloudflare.com/client/v4/zones?name=" + hostname
    headers = {
        "X-Auth-Email": email,
        "X-Auth-Key": AUTH_TOKEN,
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)
    zone_id = None

    if response.status_code == 200:
        data = response.json()
        if data.get("success"):
            zones = data.get("result")
            if zones:
                zone_id = zones[0].get("id")

    if zone_id:
        url = "https://api.cloudflare.com/client/v4/zones/" + zone_id + "/settings/ssl"
        params = {"value": "full"}
        response = requests.patch(url, headers=headers, json=params)

        if response.status_code == 200:
            print("SSL/TLS enabled for", hostname)
            return True
        else:
            print("Error enabling SSL/TLS for", hostname)
            return False
    else:
        print("Could not find zone ID for", hostname)
        return False

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 ssltls.py <hostname>")
        sys.exit(1)

    email = "limitedhighspeed@gmail.com"
    api_token = "cbac2627c4d21e32be6cb73d1935aaceb1567"
    hostname = sys.argv[1]

    SSLTLS_enable(email, api_token, hostname)

import requests


def search_sploitus(cve_query):
    url = "https://sploitus.com/search"
    params = {
        'query': cve_query,
        'type': 'exploits',
        'sort': 'default',
        'offset': 0
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        exploits = data.get('exploits', [])
        if not exploits:
            print(f"No exploits found for {cve_query}")
            return

        for exploit in exploits:
            print(f"Title: {exploit.get('title')}")
            print(f"Link: {exploit.get('url')}")
            print(f"Type: {exploit.get('type')}")
            print("")
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    cve = input("Enter CVE ID: ")
    print(f"Searching for {cve}")

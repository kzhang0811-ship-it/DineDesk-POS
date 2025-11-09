import requests

def test_dummyjson_api():
    # Example endpoint: fetch a sample product to simulate data retrieval
    url = "https://dummyjson.com/products/1"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            print("✅ Web API call successful!")
            print("Product Title:", data["title"])
            print("Price:", data["price"])
        else:
            print("❌ API call failed with status:", response.status_code)
    except Exception as e:
        print("Error occurred:", e)

# Run test
if __name__ == "__main__":
    test_dummyjson_api()

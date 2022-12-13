import requests
from random_user_agent.params import OperatingSystem, SoftwareName
from random_user_agent.user_agent import UserAgent


class Request:
    # Class attribute

    # Constructor
    def __init__(self):
        pass

    def make_request(self, url, headers, body):
        if body is None:
            response = requests.get(url, headers=headers)
        else:
            response = requests.post(url, headers=headers, data=body)

        if response.status_code != 200 and response.status_code != 204:
            print("\nRequest was invalid: \n"
                  "status code: " + str(response.status_code) + "\n"
                  "url: " + url + "\n"
                  "response: " + response.text + "\n"
                  )
            quit()
        else:
            print(
                "response: " + response.text + "\n"
            )
        return response

    def create_user_agent(self):
        software_names = [SoftwareName.CHROME.value]
        operating_systems = [
            OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]

        user_agent_rotator = UserAgent(
            software_names=software_names, operating_systems=operating_systems, limit=100)

        return user_agent_rotator.get_random_user_agent()

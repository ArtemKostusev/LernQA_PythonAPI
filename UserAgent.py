import requests

class TestUserAgent:
   def test_user_agent(self):
       response = requests.get ("https://playground.learnqa.ru/ajax/api/user_agent_check", headers={"User-Agent":"Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"})
       print(response.text)
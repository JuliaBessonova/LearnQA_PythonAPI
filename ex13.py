import requests
import pytest

class TestUserAgent:

    user_agents = [
        ('Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30', 'Mobile', 'No', 'Android'),
        ('Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1', 'Mobile', 'Chrome', 'iOS'),
        ('Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)', 'Googlebot', 'Unknown', 'Unknown'),
        ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0', 'Web', 'Chrome', 'No'),
        ('Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1', 'Mobile', 'No', 'iPhone')
    ]

    @pytest.mark.parametrize('user_agent', user_agents)
    def test_user_agent_check(self, user_agent):
        url = "https://playground.learnqa.ru/ajax/api/user_agent_check"

        response = requests.get(url, headers={"User-Agent": user_agent[0]})
        response_dict = response.json()
        actual_platform = response_dict['platform']
        actual_browser = response_dict['browser']
        actual_device = response_dict['device']

        assert actual_platform == user_agent[1], f"Platform {actual_platform} in response doesn't match {user_agent[1]}"
        assert actual_browser == user_agent[2], f"Browser {actual_browser} in response doesn't match {user_agent[2]}"
        assert actual_device == user_agent[3], f"Device {actual_device} in response doesn't match {user_agent[3]}"


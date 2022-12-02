import requests
import allure_pytest
class TestDemo:
    def test_get(self):
        r=requests.get("http://139.159.185.228/get")
        print(r.status_code,r.text)
        print(r.json())
        assert r.status_code==200
    def test_query(self):
        payload={
            "level":1,
            "name":"hhh"
        }
        r=requests.get('http://139.159.185.228/get', params=payload)
        print(r.json())
        assert r.status_code==200

    def test_post_query(self):
        payload={
            "level":1,
            "name":"hhh"
        }
        r=requests.post("http://139.159.185.228/post",data=payload)
        print(r.text)
        assert r.status_code==200
    def test_header(self):
        r=requests.post("http://139.159.185.228/post",headers={"myheader":"header demo"})
        print(r.json())
        assert r.status_code==200
        assert r.json()["headers"]["Myheader"]=="header demo"

    def test_post_json(self):
        payload={
            "name":"xiaoming",
            "id":1
        }
        r=requests.post("http://139.159.185.228/post",json=payload)
        print(r.json())
        assert r.status_code==200
        assert r.json()["json"]["id"]==1
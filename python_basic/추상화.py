# 추상화란? 실체화가 되지 않는 부모로부터 상속받는 것
# 부모 클래스 내에 이름만 선언되고 구현부가 없는 추상 메서드를 포함
# 상속 받은 클래스는 반드시 추상 메서드에 대해서 구현 해줘야 함
from abc import *  # 추상클래스를 사용하기 위해 import
from abd import ABC

class NetworkAdapter(metaclass=ABCMeta):  # 해당 클래스를 추상클래스로 만듦
    @abstractmethod
    def connect(self):
        pass

class WiFi(NetworkAdapter):
    def __init__(self, company):
        self.company = company
    def connect(self):
        print(f"{self.company}")

class FiveG(NetworkAdapter):
    def __init__(self, company):
        self.company = company
    def connect(self):
        print(f"{self.company}")

class Lte(NetworkAdapter):
    def __init__(self, company):
        self.company = company
    def connect(self):
        print(f"{self.company}")

net = input("연결할 네트워크 [1]WiFi [2]5G [3]Lte : ")

if net == "1":
    adapter = WiFi("KT Megapass")
elif net == "2":
    adapter = FiveG("SK Telecom")
elif net == "3":
    adapter = Lte("LG U+")
else:
    print("연결할 네트워크가 없습니다.")

adapter.connect()
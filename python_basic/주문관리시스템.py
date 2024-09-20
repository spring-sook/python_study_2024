from decimal import Decimal

class Product:  # 제품의 이름과 가격을 관리
    def __init__(self, name, price):
        self.__name = name  # 제품 이름
        self.__price = price  # 제품 가격

    def get_name(self):
        return self.__name  # 제품명 가져오기

    def get_price(self):
        return self.__price  # 가격 가져오기

class Order:  # 여러 개의 Product 객체를 관리하고, 주문의 총합과 판매세를 계산하는 역할
    def __init__(self):
        self.products = []
        self.total = Decimal('0')

    def add_item(self, product):
        self.products.append(product)  # [제품명, 가격] 객체를 products 리스트에 추가
        self.total += Decimal(product.get_price())  # 제품 가격을 total 변수에 합산

    def get_item(self, name):
        for product in self.products:  # self.products = [[제품명, 가격], [제품명, 가격], ...]
            if product.get_name() == name: return product  # product = [제품명, 가격] / product.get_name()을 이용해 제품명 가져와서 비교
            else: return None

    def remove_item(self, name):
        for idx, product in enumerate(self.products):  # idx = 해당 [제품명, 가격]의 인덱스
            if name == product.get_name():
                self.total -= Decimal(product.get_price())  # 제거할 상품의 가격을 total에서 빼주기
                self.products.pop(idx)  # 제거할 상품의 인덱스를 이용해서 삭제
                return True
        return False

    def calculate_final_price(self, tax_rate):
        return round(self.total * (1 + Decimal(tax_rate)), 2)



if __name__ == "__main__":
    my_order = Order()

    while True:
        print("=" * 60)
        menu_num = input("번호를 선택해주세요.\n"
                         "[1]제품 추가  [2]제품 제거  [3]제품 목록 보기  [4]제품 상세 보기  \n"
                         "[5]최종 가격 계산(세금 포함)  [6]프로그램 종료 : ")
        try:
            if menu_num == "1":
                item_name = input("제품명을 입력하세요 : ")
                item_price = input("제품 가격을 입력하세요 : ")
                my_order.add_item(Product(item_name, item_price))
            elif menu_num == "2":
                item = input("제거할 제품명 : ")
                if my_order.remove_item(item):
                    print(f"==> {item}을 제거하였습니다.")
                else:
                    print("==> 해당 제품이 존재하지 않습니다.")
            elif menu_num == "3":
                for product in my_order.products:
                    print(f"- {product.get_name()}")
            elif menu_num == "4":
                for product in my_order.products:
                    print(f"- {product.get_name()}, {product.get_price()}원")
            elif menu_num == "5":
                print(f"==> {my_order.calculate_final_price(Decimal("0.06"))}원")
            elif menu_num == "6":
                print("==> 프로그램을 종료합니다.")
                break
            else:
                print("==> 번호를 잘못 선택하셨습니다.")
        except:
            print("==> 잘못 입력하셨습니다.")
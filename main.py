MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1500,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2500,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3000,
    }
}

all_money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# 재료 체크
def is_resource_check(order_ingredients):
    """Ingredients Check"""
    # 반복문으로 주문한것과 재료를 비교
    for item in order_ingredients:
        # 만약 주문한것의 재료가 재고보다 많다면 제공 불가
        if order_ingredients[item] >= resources[item]:
            print(f"죄송합니다 재료인 {item}가 부족합니다 ㅠ")
            return False
    return True

def process_money():
    """Return total Money Calculated"""
    print("insert Money!!!")
    total = int(input("백원 개수: ")) * 100
    total += int(input("오백원 개수: ")) * 500
    total += int(input("천원 개수: ")) * 1000
    total += int(input("오천원 개수: ")) * 5000
    return total

def is_transaction_check(money_recive, drink_cost):
    """Return True when the Payment is accept!!! but False no serveing to drink"""
    # 입력받은 금액이 커피 금액보다 크다면
    if money_recive >= drink_cost:
        # 잔돈 체크
        change = round(money_recive - drink_cost)
        # 지역함수에서 외부 변수를 사용하기 위한 글로벌 변수 호출
        global all_money
        # 수익 체크
        all_money += drink_cost
        print("구매 해주셔서 감사합니다.")
        print(f"잔돈은 {change}원 입니다.")
        return True
    else:
        # 돈이 부족할경우 주문을 취소하고 그대로 잔돈 반환.
        print("돈이 충분하지 않습니다 돈을 반환합니다")
        print(f"반환된 금액은 {money_recive}원 입니다.")
        return False

def make_coffee(order_ingredients):
    """주문한 제품의 재료 차감 함수"""
    # order_ingredients = 주문한 음료의 재료
    # 하나씩 반복함 보유 재고 와 주문한 음료의 재료는 동일한 구조로 구성되어있기에 비교하며 연산가능.
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"주문하신 {order} ☺️ 나왔습니다.")


def show_resource():
    # 현재 재고와 수익 출력
    print(resources)
    print(all_money)



is_on = True

while is_on:
    # 주문 받기 Dict형 이기에 키값을 비교하며 인식
    order = input("order Plz!!!\n"
              "(espresso/ latte/ cappuccino)\n"
                  " : ")
    # 종료 코드
    if order == "off":
        is_on = False
    # 재고 및 수익 코드
    elif order == 'report':
        print(show_resource())
    else:
        # drink 변수에 order에서 입력받은 문자열을 menu 에서 찾고 이를 대입
        drink = MENU[order]
        # drink = 제품 이름 -> 내부에 존재하는 재료 키 : 값 받아오며 함수 호출
        if is_resource_check(drink["ingredients"]):
            # 금액 입력받기
            payment = process_money()
            # 금액 비교하기 -> 잔돈 반환 함수 호출
            if is_transaction_check(payment,drink["cost"]):
                make_coffee(drink["ingredients"])




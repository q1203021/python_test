"""
practice1.py - 簡易問候系統
"""

import datetime


class Greeter:
    """負責產生問候訊息的類別"""

    GREETINGS = {
        "morning":   "早安",
        "afternoon": "午安",
        "evening":   "晚安",
    }

    def __init__(self, name: str):
        self.name = name
        self.visit_count = 0

    def get_time_period(self) -> str:
        """根據目前小時數回傳時段字串"""
        hour = datetime.datetime.now().hour
        if 5 <= hour < 12:
            return "morning"
        elif 12 <= hour < 18:
            return "afternoon"
        else:
            return "evening"

    def greet(self) -> str:
        """產生個人化問候語並累計造訪次數"""
        self.visit_count += 1
        period = self.get_time_period()
        greeting = self.GREETINGS[period]
        return f"{greeting}，{self.name}！這是你第 {self.visit_count} 次打招呼。"

    def farewell(self) -> str:
        """產生告別語"""
        return f"再見，{self.name}！今天共問候了 {self.visit_count} 次，掰掰！"


def get_valid_name() -> str:
    """提示使用者輸入名字，直到輸入非空白字串為止"""
    while True:
        name = input("請輸入你的名字：").strip()
        if name:
            return name
        print("名字不能為空，請再試一次。")


def main():
    print("=" * 40)
    print("      歡迎使用簡易問候系統")
    print("=" * 40)

    name = get_valid_name()
    greeter = Greeter(name)

    while True:
        print("\n請選擇操作：")
        print("  1. 打招呼")
        print("  2. 查看目前時段")
        print("  3. 離開")

        choice = input("輸入選項 (1/2/3)：").strip()

        if choice == "1":
            print(greeter.greet())
        elif choice == "2":
            period_map = {"morning": "早上", "afternoon": "下午", "evening": "晚上"}
            period = greeter.get_time_period()
            now = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"現在時間是 {now}，屬於「{period_map[period]}」時段。")
        elif choice == "3":
            print(greeter.farewell())
            break
        else:
            print("無效的選項，請輸入 1、2 或 3。")


if __name__ == "__main__":
    main()

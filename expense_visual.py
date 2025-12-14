import csv
import matplotlib.pyplot as plt
from collections import defaultdict

# 定義要讀取的檔案名稱
DATA_FILE = "expenses.csv"

def load_data():
    """
    讀取 CSV 檔案並回傳資料列表
    """
    expenses = []
    try:
        with open(DATA_FILE, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # TODO: 將讀取到的每一行資料加入 expenses 列表
                # 提示: 你可能需要將 amount 轉為整數或浮點數
                pass # 請在此填寫程式碼
    except FileNotFoundError:
        print("找不到資料檔，請先執行輸入模組 (Member A)！")
    
    return expenses

def generate_pie_chart(expenses):
    """
    根據類別 (Category) 統計金額並繪製圓餅圖
    """
    if not expenses:
        print("沒有資料可繪製！")
        return

    # TODO: 統計每個 Category 的總金額
    # 提示: 可以使用 defaultdict(float) 或普通的 dict
    category_totals = defaultdict(float)
    
    # ... 實作統計邏輯 ...

    # 準備繪圖資料
    labels = list(category_totals.keys())
    sizes = list(category_totals.values())

    # TODO: 使用 matplotlib 繪製圓餅圖
    # plt.pie(...)
    # plt.title("Expense by Category")
    # plt.show()
    print("圓餅圖已生成！")

if __name__ == "__main__":
    data = load_data()
    generate_pie_chart(data)
import csv
import matplotlib.pyplot as plt
from collections import defaultdict
import os

# 定義要讀取的檔案名稱
DATA_FILE = "expenses.csv"

def load_data():
    """
    讀取 CSV 檔案並回傳資料列表
    """
    expenses = []
    
    if not os.path.exists(DATA_FILE):
        print("❌ 找不到資料檔 'expenses.csv'。")
        print("請先執行 Member A 的輸入程式 (expense_input.py) 來建立資料！")
        return []

    try:
        with open(DATA_FILE, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    expenses.append({
                        'date': row['Date'],
                        'amount': float(row['Amount']), # 將金額轉為浮點數
                        'category': row['Category'],
                        'notes': row['Notes']
                    })
                except ValueError:
                    print(f"⚠️ 跳過格式錯誤的資料行: {row}")
                    
    except Exception as e:
        print(f"❌ 讀取檔案時發生錯誤: {e}")
    
    return expenses

def generate_pie_chart(expenses):
    """
    根據類別 (Category) 統計金額並繪製圓餅圖
    """
    if not expenses:
        print("⚠️ 沒有有效的資料可供繪圖。")
        return

    # 1. 統計每個 Category 的總金額
    category_totals = defaultdict(float)
    for expense in expenses:
        category_totals[expense['category']] += expense['amount']

    # 2. 準備繪圖資料
    labels = list(category_totals.keys())
    sizes = list(category_totals.values())

    # 3. 繪製圓餅圖
    plt.figure(figsize=(8, 6)) # 設定圖表大小
    
    # autopct='%1.1f%%' 會顯示百分比
    # startangle=140 讓圖表起始角度轉一下，比較美觀
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    
    plt.title("Expense Analysis by Category") # 圖表標題
    plt.axis('equal') # 確保圓餅圖是正圓形
    
    print("📊 正在開啟圓餅圖視窗...")
    plt.show() # 顯示圖表視窗

if __name__ == "__main__":
    data = load_data()
    if data:
        print(f"成功讀取 {len(data)} 筆資料，準備繪圖...")
        generate_pie_chart(data)
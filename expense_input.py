import csv
import os

# 定義資料儲存的檔案名稱
DATA_FILE = "expenses.csv"

def save_expense(date, amount, category, notes):
    """
    將單筆消費記錄存入 CSV 檔案
    """
    # 檢查檔案是否存在，如果不存在則先寫入標頭 (Header)
    file_exists = os.path.isfile(DATA_FILE)

    with open(DATA_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # TODO: 如果是新檔案，先寫入欄位名稱 (例如: Date, Amount, Category, Notes)
        if not file_exists:
            pass # 請在此填寫程式碼
            
        # TODO: 將使用者輸入的資料寫入檔案
        pass # 請在此填寫程式碼
    
    print(f"已儲存: {date} - ${amount} - {category}")

def get_user_input():
    """
    與使用者互動，獲取消費資訊
    """
    print("=== 記帳小工具 (Member A) ===")
    
    # TODO: 使用 input() 獲取使用者輸入
    # 需求: Date, Amount, Category 是必須的，Notes 是選填的 [cite: 8]
    date = input("請輸入日期 (YYYY-MM-DD): ")
    amount = input("請輸入金額: ")
    # ... 請繼續完成剩下的輸入 ...

    # 呼叫存檔函式
    # save_expense(date, amount, category, notes)

if __name__ == "__main__":
    while True:
        get_user_input()
        cont = input("要繼續輸入嗎？(y/n): ")
        if cont.lower() != 'y':
            break
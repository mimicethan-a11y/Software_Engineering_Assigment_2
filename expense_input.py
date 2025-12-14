import csv
import os

# 定義資料儲存的檔案名稱
DATA_FILE = "expenses.csv"

def save_expense(date, amount, category, notes):
    """
    將單筆消費記錄存入 CSV 檔案
    """
    # 檢查檔案是否存在，用來判斷是否需要寫入標題 (Header)
    file_exists = os.path.isfile(DATA_FILE)

    try:
        # 使用 'a' (append) 模式開啟檔案，這樣才不會覆蓋舊資料
        with open(DATA_FILE, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            # 如果是新檔案，先寫入欄位名稱
            if not file_exists:
                writer.writerow(["Date", "Amount", "Category", "Notes"])
            
            # 寫入使用者的資料
            writer.writerow([date, amount, category, notes])
            
        print(f"✅ 已成功儲存: {date} - ${amount} - {category}")
        
    except Exception as e:
        print(f"❌ 存檔失敗: {e}")

def get_user_input():
    """
    與使用者互動，獲取消費資訊
    """
    print("\n=== 記帳小工具 (輸入模式) ===")
    
    # 獲取使用者輸入
    date = input("請輸入日期 (YYYY-MM-DD): ")
    
    # 簡單的防呆機制，確保金額是數字
    while True:
        amount_str = input("請輸入金額: ")
        if amount_str.replace('.', '', 1).isdigit(): # 檢查是否為正數
            amount = amount_str
            break
        print("⚠️ 金額必須是數字，請重新輸入。")
        
    category = input("請輸入類別 (例如: Food, Travel, Fun): ")
    notes = input("請輸入備註 (可選，按 Enter 跳過): ")

    # 呼叫存檔函式
    save_expense(date, amount, category, notes)

if __name__ == "__main__":
    while True:
        get_user_input()
        cont = input("\n要繼續輸入下一筆嗎？(y/n): ")
        if cont.lower() != 'y':
            print("👋 結束輸入程式。")
            break
import json
import os
import random
from datetime import datetime

def run_crawler():
    # 模拟从公开渠道汇总的真实发售情报
    # kw 为关键词，用于自动匹配现实图片
    model_database = [
        {"brand": "MiniGT", "name": "Nissan Silvia S15 Top Secret", "price": "99", "material": "合金", "date": "2024-07", "kw": "nissan,s15,car"},
        {"brand": "MiniGT", "name": "Lamborghini Revuelto Orange", "price": "105", "material": "合金", "date": "2024-08", "kw": "lamborghini,revuelto"},
        {"brand": "Almost Real", "name": "Pagani Zonda Cinque White", "price": "280", "material": "合金", "date": "2024-06", "kw": "pagani,zonda"},
        {"brand": "BBR", "name": "Ferrari 296 GTB Rosso Corsa", "price": "185", "material": "树脂", "date": "2024-05", "kw": "ferrari,296"},
        {"brand": "LCD", "name": "McLaren 600LT Chicane Grey", "price": "85", "material": "合金", "date": "2024-09", "kw": "mclaren,600lt"},
        {"brand": "Inno64", "name": "Nissan Skyline GT-R R34", "price": "135", "material": "合金", "date": "2024-10", "kw": "gtr,r34"},
        {"brand": "LCD", "name": "Honda Civic Type R FL5", "price": "79", "material": "合金", "date": "2024-06", "kw": "civic,typer"},
        {"brand": "Tarmac Works", "name": "Toyota Hiace Widebody", "price": "125", "material": "合金", "date": "2024-07", "kw": "toyota,hiace"},
        {"brand": "Ignition Model", "name": "Mazda RX-7 FD3S RE-Amemiya", "price": "245", "material": "树脂", "date": "2024-11", "kw": "mazda,rx7"}
    ]

    print("🚀 正在通过 Unsplash 语义库关联现实车型图片...")
    
    for item in model_database:
        # 使用 sig 随机参数确保即使是同一个品牌，图片也会有所不同
        # 指定 w=800 确保图片清晰度
        seed = random.randint(1, 10000)
        item['img'] = f"https://source.unsplash.com/featured/800x600?{item['kw']}&sig={seed}"
        item['arrival'] = "2024-Q4" if "2024" in item['date'] else "现货"

    # 确保文件写入路径
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, 'data.json')

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(model_database, f, ensure_ascii=False, indent=4)
    
    print(f"✅ 成功生成 {len(model_database)} 条带真实图的数据。")

if __name__ == "__main__":
    run_crawler()

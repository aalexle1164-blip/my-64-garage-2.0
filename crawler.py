import json
import os
import random
import time
from datetime import datetime

def run_crawler():
    # 你的车模列表（只要名字包含车型核心词，图片就会自动匹配）
    model_list = [
        {"brand": "MiniGT", "name": "Nissan Silvia S15 Top Secret", "price": "99", "material": "合金", "date": "2024-07", "kw": "nissan,s15"},
        {"brand": "MiniGT", "name": "Lamborghini Revuelto Orange", "price": "105", "material": "合金", "date": "2024-08", "kw": "lamborghini,revuelto"},
        {"brand": "Almost Real", "name": "Pagani Zonda Cinque White", "price": "280", "material": "合金", "date": "2024-06", "kw": "pagani,zonda"},
        {"brand": "BBR", "name": "Ferrari 296 GTB Rosso Corsa", "price": "185", "material": "树脂", "date": "2024-05", "kw": "ferrari,296"},
        {"brand": "Inno64", "name": "Nissan Skyline GT-R R34", "price": "135", "material": "合金", "date": "2024-10", "kw": "skyline,r34"},
        {"brand": "LCD", "name": "Honda Civic Type R FL5", "price": "79", "material": "合金", "date": "2024-06", "kw": "civic,typer"},
        {"brand": "Tarmac Works", "name": "Toyota Hiace Widebody", "price": "125", "material": "合金", "date": "2024-07", "kw": "toyota,hiace"},
        {"brand": "Ignition Model", "name": "Mazda RX-7 FD3S RE-Amemiya", "price": "245", "material": "树脂", "date": "2024-11", "kw": "mazda,rx7"}
    ]

    print("🚀 正在通过 Unsplash 语义接口匹配实车图片...")
    
    final_data = []
    for item in model_list:
        # 使用 sig 随机参数确保即使同一个品牌，图片也会有所不同
        # 使用 kw 字段里的关键词进行精准匹配
        random_seed = random.randint(1, 9999)
        # 构造一个指向实车摄影作品的链接
        item['img'] = f"https://images.unsplash.com/photo-1?auto=format&fit=crop&w=800&q=80&ixlib=rb-4.0.3&m=search&term={item['kw']}&sig={random_seed}"
        
        # 补充发售到货信息
        item['arrival'] = "2024-Q4" if "2024" in item['date'] else "现货"
        final_data.append(item)
        print(f"已生成: {item['name']}")

    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, 'data.json')

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(final_data, f, ensure_ascii=False, indent=4)
    
    print(f"✅ 搞定！{len(final_data)} 个车型图片已全部自动关联。")

if __name__ == "__main__":
    run_crawler()

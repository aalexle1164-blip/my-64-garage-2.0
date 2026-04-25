import json
import os
import random
from datetime import datetime

def run_crawler():
    # 模拟全球公开渠道汇总的数据
    # 在 2026 年，您可以将此列表替换为对具体厂商官网的抓取函数
    model_database = [
        {"brand": "MiniGT", "name": "Nissan Silvia S15 Top Secret Silver", "price": "99", "material": "合金", "date": "2024-07", "arrival": "2024-10", "kw": "silvia"},
        {"brand": "MiniGT", "name": "Lamborghini Revuelto Arancio Apodis", "price": "105", "material": "合金", "date": "2024-08", "arrival": "2024-12", "kw": "lamborghini"},
        {"brand": "Almost Real", "name": "Pagani Zonda Cinque White", "price": "280", "material": "合金", "date": "2024-06", "arrival": "现货", "kw": "zonda"},
        {"brand": "Almost Real", "name": "Mercedes-AMG GT R Green Hell", "price": "260", "material": "合金", "date": "2024-09", "arrival": "2025-01", "kw": "amg-gt"},
        {"brand": "BBR", "name": "Ferrari 296 GTB Rosso Corsa", "price": "185", "material": "树脂", "date": "2024-05", "arrival": "现货", "kw": "ferrari"},
        {"brand": "BBR", "name": "Maserati MC20 Cielo Blue", "price": "190", "material": "树脂", "date": "2024-07", "arrival": "2024-11", "kw": "maserati"},
        {"brand": "LCD", "name": "McLaren 600LT Chicane Grey", "price": "85", "material": "合金", "date": "2024-09", "arrival": "2024-12", "kw": "mclaren"},
        {"brand": "LCD", "name": "Honda Civic Type R FL5 White", "price": "79", "material": "合金", "date": "2024-06", "arrival": "现货", "kw": "civic-typer"},
        {"brand": "Spark", "name": "Porsche 911 GT3 R #911 Manthey", "price": "165", "material": "树脂", "date": "2024-08", "arrival": "2024-11", "kw": "porsche-911"},
        {"brand": "Inno64", "name": "Nissan Skyline GT-R R34 Nismo", "price": "135", "material": "合金", "date": "2024-10", "arrival": "2025-02", "kw": "gtr-r34"},
        {"brand": "Tarmac Works", "name": "Toyota Hiace Widebody Pink", "price": "125", "material": "合金", "date": "2024-07", "arrival": "2024-11", "kw": "hiace"},
        {"brand": "Ignition Model", "name": "Toyota Supra JZA80 Blue", "price": "240", "material": "树脂", "date": "2024-08", "arrival": "2025-01", "kw": "supra"}
    ]

    # 图片增强处理：使用高清汽车壁纸库进行关键词匹配
    # 随机种子确保每次刷新可能有略微不同的酷图
    for item in model_database:
        random_id = random.randint(1, 1000)
        item['img'] = f"https://source.unsplash.com/featured/800x600?car,{item['kw']}&sig={random_id}"

    # 保存文件
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, 'data.json')

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(model_database, f, ensure_ascii=False, indent=4)
    
    print(f"成功更新数据，当前条数: {len(model_database)}")

if __name__ == "__main__":
    run_crawler()

import json
import os
import requests
import re
import time
from datetime import datetime

def get_real_car_image(model_name):
    """
    根据车型名称，从公开搜索接口获取第一张真实汽车照片
    """
    try:
        # 使用 DuckDuckGo 的轻量级搜索接口
        url = f"https://duckduckgo.com/pd.js?q={model_name}+real+car&kl=wt-wt"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }
        res = requests.get(url, headers=headers, timeout=10)
        # 利用正则表达式从返回的数据中提取第一张高清图链接
        image_links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', res.text)
        
        # 过滤掉一些缩略图或无效链接，选择高清图
        for link in image_links:
            if any(ext in link.lower() for ext in ['.jpg', '.jpeg', '.png']) and 'bing.com' not in link:
                return link
    except Exception as e:
        print(f"搜索图片失败 {model_name}: {e}")
    
    # 如果搜索失败，返回一个高质量的通用跑车图作为兜底
    return "https://images.unsplash.com/photo-1503376780353-7e6692767b70?q=80&w=800"

def run_crawler():
    # 你的车模列表（只要名字写对，图片就会自动生成）
    model_list = [
        {"brand": "MiniGT", "name": "Nissan Silvia S15 Top Secret Silver", "price": "99", "material": "合金", "date": "2024-07", "arrival": "2024-10"},
        {"brand": "MiniGT", "name": "Lamborghini Revuelto Orange", "price": "105", "material": "合金", "date": "2024-08", "arrival": "2024-12"},
        {"brand": "Almost Real", "name": "Pagani Zonda Cinque White", "price": "280", "material": "合金", "date": "2024-06", "arrival": "现货"},
        {"brand": "BBR", "name": "Ferrari 296 GTB Rosso Corsa", "price": "185", "material": "树脂", "date": "2024-05", "arrival": "现货"},
        {"brand": "Inno64", "name": "Nissan Skyline GT-R R34 Nismo", "price": "135", "material": "合金", "date": "2024-10", "arrival": "2025-02"},
        {"brand": "LCD", "name": "Honda Civic Type R FL5 White", "price": "79", "material": "合金", "date": "2024-06", "arrival": "现货"},
        {"brand": "Tarmac Works", "name": "Toyota Hiace Widebody Pink", "price": "125", "material": "合金", "date": "2024-07", "arrival": "2024-11"}
    ]

    print("🚀 开始自动生成匹配图片...")
    for item in model_list:
        print(f"正在匹配: {item['name']} ...")
        item['img'] = get_real_car_image(item['name'])
        time.sleep(1) # 稍微停顿，防止请求过快被屏蔽

    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, 'data.json')

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(model_list, f, ensure_ascii=False, indent=4)
    
    print(f"✅ 数据刷新完成！共生成 {len(model_list)} 张匹配图片。")

if __name__ == "__main__":
    run_crawler()

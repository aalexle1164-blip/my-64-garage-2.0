import json
import os
import requests
import urllib.parse
from datetime import datetime

def get_wikimedia_image(car_name):
    """
    通过维基百科 API 自动获取现实车型的公开图片
    """
    try:
        # 编码车型名称用于 URL
        encoded_name = urllib.parse.quote(car_name)
        # 搜索维基百科相关的页面
        search_url = f"https://en.wikipedia.org/w/api.php?action=query&format=json&prop=pageimages&titles={encoded_name}&pithumbsize=800&redirects=1"
        
        response = requests.get(search_url, timeout=10)
        data = response.json()
        
        pages = data.get("query", {}).get("pages", {})
        for page_id in pages:
            if "thumbnail" in pages[page_id]:
                return pages[page_id]["thumbnail"]["source"]
    except Exception as e:
        print(f"抓取 {car_name} 失败: {e}")
    
    # 如果抓取失败，使用一个高质量的超跑占位图
    return f"https://images.unsplash.com/photo-1542281286-9e0a16bb7366?auto=format&fit=crop&q=80&w=800"

def run_crawler():
    # 只要这里的名字写得准确（现实中存在的名字），就能抓到图
    model_list = [
        {"brand": "MiniGT", "name": "Nissan Silvia S15", "price": "99", "material": "合金", "date": "2024-07"},
        {"brand": "MiniGT", "name": "Lamborghini Revuelto", "price": "105", "material": "合金", "date": "2024-08"},
        {"brand": "Almost Real", "name": "Pagani Zonda", "price": "280", "material": "合金", "date": "2024-06"},
        {"brand": "BBR", "name": "Ferrari 296 GTB", "price": "185", "material": "树脂", "date": "2024-05"},
        {"brand": "Inno64", "name": "Nissan Skyline GT-R R34", "price": "135", "material": "合金", "date": "2024-10"},
        {"brand": "LCD", "name": "Honda Civic Type R", "price": "79", "material": "合金", "date": "2024-06"},
        {"brand": "Tarmac Works", "name": "Toyota HiAce", "price": "125", "material": "合金", "date": "2024-07"},
        {"brand": "Spark", "name": "Porsche 911 GT3", "price": "165", "material": "树脂", "date": "2024-08"}
    ]

    print("🚀 正在从维基百科开放库抓取真实车型图片...")
    
    for item in model_list:
        print(f"正在匹配真实图片: {item['name']}...")
        item['img'] = get_wikimedia_image(item['name'])
        item['arrival'] = "现货" if "2024" in item['date'] else "预订"

    # 保存路径
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, 'data.json')

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(model_list, f, ensure_ascii=False, indent=4)
    
    print(f"✅ 抓取完成！共生成 {len(model_list)} 张真实车型匹配图。")

if __name__ == "__main__":
    run_crawler()

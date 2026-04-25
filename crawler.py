import json
import os

def generate_data():
    # 模拟从公开信息源（厂商列表）获取的数据
    # 在实际应用中，这里会替换为 requests.get() 抓取网页的代码
    models = [
        {
            "brand": "MiniGT",
            "name": "Lamborghini Revuelto Arancio Apodis",
            "price": "99",
            "material": "合金",
            "date": "2024-07",
            "arrival": "2024-10",
            "img": "https://via.placeholder.com/400x250?text=MiniGT+Revuelto"
        },
        {
            "brand": "BBR",
            "name": "Maserati MC20 Cielo",
            "price": "180",
            "material": "树脂",
            "date": "2024-05",
            "arrival": "现货",
            "img": "https://via.placeholder.com/400x250?text=BBR+MC20"
        }
    ]

    # 获取当前脚本所在路径，确保 data.json 生成在同级目录
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, 'data.json')

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(models, f, ensure_ascii=False, indent=4)
    
    print(f"成功更新！文件已保存至: {file_path}")

if __name__ == "__main__":
    generate_data()

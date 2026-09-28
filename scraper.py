import requests
import json

def get_gold_and_forex_prices():
    gold_url = "https://api.exchangerate-api.com/v4/latest/USD"
    
    try:
        response = requests.get(gold_url)
        data = response.json()
        
        usd_to_egp = data['rates'].get('EGP', 0)
        
        gold_api = "https://api.gold-api.com/price/XAU"
        gold_response = requests.get(gold_api).json()
        gold_price_usd = gold_response.get('price', 0)
        
        gram_24_usd = gold_price_usd / 31.1035
        gram_21_usd = gram_24_usd * (21 / 24)
        
        gram_24_egp = round(gram_24_usd * usd_to_egp, 2)
        gram_21_egp = round(gram_21_usd * usd_to_egp, 2)
        
        result = {
            "gold_usd_ounce": gold_price_usd,
            "usd_to_egp": usd_to_egp,
            "gold_gram_24_egp": gram_24_egp,
            "gold_gram_21_egp": gram_21_egp
        }
        
        print("تم جلب البيانات بنجاح:")
        print(json.dumps(result, ensure_ascii=False, indent=2))
        
        with open("gold_data.json", "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)

    except Exception as e:
        print(f"حدث خطأ أثناء جلب البيانات: {e}")

if __name__ == "__main__":
    get_gold_and_forex_prices()
  

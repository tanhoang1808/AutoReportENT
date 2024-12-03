import requests
from datetime import datetime
import re



def get_facebook_data(url, access_token):
    url = url + f"&access_token={access_token}"
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        print("success")
        return response.json()
    else:
        print("Failed to get data from Facebook.")
        return None


def get_data_from_json(data,employee):
    json_list = []
    for d in data.get("data", []):
        # if int(d["spend"]) >= 0:
        json_list.append({
            "account_name" : d["account_name"],
            "campaign_name": d["campaign_name"],
            "date_start": d["date_start"],
            "date_stop": d["date_stop"],
            "spend": d["spend"]
        })

  
    return transform_jsonlist(json_list) if json_list else None


def transform_jsonlist(data):
    weekly_info_data = {}
    campaign_patterns = {
    'FACEBOOK HCM': re.compile(r'\b(FACEBOOK HCM|FB HCM|FBHCM)\b', re.IGNORECASE),
    'TIKTOK': re.compile(r'\b(TIKTOK|TIKTOKHCM|TIKTOK HCM|TIKTOK HOCHIMINH)\b', re.IGNORECASE),
    'FACEBOOK ZOOM': re.compile(r'\b(FACEBOOK ZOOM|facebook zoom|fb zoom|zoom|FB ZOOM|FBZOOM)\b', re.IGNORECASE),
    'SHOPEE ZOOM': re.compile(r'\b(SHOPEE ZOOM|SHOPEE|SHOPEEZOOM)\b', re.IGNORECASE),
    'CPTRUYENTHONG': re.compile(r'\b(CP TRUYENTHONG|CP TT|CPTRUYENTHONG|CP Truyen Thong|CP TThong)\b', re.IGNORECASE),
    'QCFB': re.compile(r'\b(QCFB|quang cao facebook|QC Facebook|DVFB|Dich Vu Facebook|DV Facebook|dvqcfb|DVQCFB)\b', re.IGNORECASE),
    'DVTT': re.compile(r'\b(DVTT|Dich Vu Tiktok|DV Tiktok)\b', re.IGNORECASE),
}


    def get_campaign_group(campaign_name):
        for key, pattern in campaign_patterns.items():
            print(f"Original campaign name: {campaign_name}")
            if pattern.search(campaign_name):
                print(f"key {key} is found")
                return key
        return None

    for item in data:
        week_start = datetime.strptime(item["date_start"], '%Y-%m-%d').strftime('%m/%d')
        week_stop = datetime.strptime(item["date_stop"], '%Y-%m-%d').strftime('%m/%d')
        spend = float(item["spend"])
        camp_name = item["campaign_name"]
        account_name = item["account_name"]
        camp_group = get_campaign_group(camp_name)
        if not camp_group:
            continue

        if week_start not in weekly_info_data:
            weekly_info_data[week_start] = {}
        if camp_group not in weekly_info_data[week_start]:
            weekly_info_data[week_start][camp_group] = {'total_spend': 0, 'date_stop': week_stop,"account_name":account_name}
        
        weekly_info_data[week_start][camp_group]['total_spend'] += spend

    return weekly_info_data

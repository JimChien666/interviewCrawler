import requests
import json
from bs4 import BeautifulSoup

if __name__ == '__main__':
    headers = {
        'content-length': '192',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    payload = {
        'curr_id': '6408',
        'smlID': '1159963',
        'header': 'AAPL历史数据',
        'st_date': '2021/01/26',
        'end_date': '2022/01/25',
        'interval_sec': 'Weekly',
        'sort_col': 'date',
        'sort_ord': 'DESC',
        'action': 'historical_data'
    }
    res = requests.post(
            'https://cn.investing.com/instruments/HistoricalDataAjax',
            data=payload, 
            headers=headers)
    parse_html = BeautifulSoup(res.text, 'html.parser')
    curr_table = parse_html.find('table', id = 'curr_table')
    trs = curr_table.find_all('tr')
    keys = trs[0].find_all('th')
    
    check_list = []
    for tr in trs:
        tds = tr.find_all('td')
        dist = {}
        for index, td in enumerate(tds):
            dist[keys[index].text] = td.text
        check_list.append(dist)
    print(json.dumps(check_list))
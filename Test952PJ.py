import datetime
import os
import re
import time
import requests
import bs4
import math
import random
# 获取关注的所有贴吧链接
def get_tieba_link():
    url = 'http://tieba.baidu.com/f/like/mylike?&pn='
    page = 1
    links = []
    while True:
        response = requests.get(url + str(page), headers=headers)
        bs = bs4.BeautifulSoup(response.text, 'lxml')
        for a in bs.select('table tr>td:first-child>a'):
            links.append({'href': a.get('href'), 'name': a.string})
        if '下一页' not in str(bs):
            break
        page += 1
    return links


# 从贴吧链接中获取贴吧签到参数
def tieba_batch_sign():
    links = get_tieba_link()
    for link in links:
        response = requests.get('https://tieba.baidu.com/' + link['href'], headers=headers)
        tbs_reg = re.compile(r'\'tbs\':\s"(.*?)"')
        time.sleep(random.randint(3,5))
        tbs = tbs_reg.search(response.text).group(1)
        if not tbs:  # 如果tbs不存在则跳过本次循环
            continue
        param = {'ie': 'utf-8', 'kw': link['name'], 'tbs': tbs}
        response = requests.post('https://tieba.baidu.com/sign/add', data=param, headers=headers)
        result = response.json()
        if result['no'] == 0:
            msg = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + ' ' + link['name'] + ' 签到成功\n'
        else:
            msg = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + ' ' + link['name'] + ' ' + result[
                'error'] + '\n'
        print(msg)
        with open(os.path.join(os.getcwd(), 'sign.log'), 'a+') as loghandle:
            loghandle.write(msg)


if __name__ == '__main__':
    headers = {
        'cookie': 'IDUPSID=434B76AC4C98285BBCE35970C1F850D7; PSTM=1586866907; bdshare_firstime=1586939172256; rpln_guide=1; SEENKW=steam%23%E4%B8%89%E5%92%8C%E5%A4%A7%E7%A5%9E; __yjs_duid=1_ec83e1938ec710747f47e7a3536745dc1621345304820; BAIDUID=2EC805F8913C1D80A03F6027EBFC3DCB:FG=1; MCITY=-%3A; BDUSS=HVZYmNKV2VjM1FhdXYxc3Y1c2oyRHVOSktTY0N1dlU5aDk3cHVRN0VHdkkzRXBoRVFBQUFBJCQAAAAAAAAAAAEAAACg4JBavdDO0s7EuOdPUrDWsNYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMhPI2HITyNha; BDUSS_BFESS=HVZYmNKV2VjM1FhdXYxc3Y1c2oyRHVOSktTY0N1dlU5aDk3cHVRN0VHdkkzRXBoRVFBQUFBJCQAAAAAAAAAAAEAAACg4JBavdDO0s7EuOdPUrDWsNYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMhPI2HITyNha; STOKEN=ae69d82dfa6190b3c097cbfc8c2708c5c41c40f4a3d258eb937f693563bcee74; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; wise_device=0; st_key_id=17; USER_JUMP=-1; 1519444128_FRSVideoUploadTip=1; video_bubble1519444128=1; delPer=0; PSINO=3; BAIDUID_BFESS=2EC805F8913C1D80A03F6027EBFC3DCB:FG=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; ZD_ENTRY=baidu; BAIDU_WISE_UID=wapp_1629863462494_720; H_PS_PSSID=34436_31660_33848_34092_34106_26350_34415_34388; BA_HECTOR=a1800l8l2485ak0h561giblup0q; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1629859858,1629863437,1629863886,1629870045; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1629870045; ab_sr=1.0.1_MThhODgzOTAyOTM5NjExNDNiNWI5YTk2NTA3ZjQwY2NhNmNjYWEzZTJlNTVkZDk0MTFkMmE4M2QwMzA5NWMyYWY2NTQ4ZDQyM2M3YzgwNzUzNTIyODZjMDQzNmJhODQ4OTYxNjc1MDg2ODNlODg0ZDhlZDI2ZWY3YmFlYWI5MGFhOWJhY2JiMGM2MmRhYTI5NGUwNzllMmM1YzNiN2ExNWMzNjI0ZDc3MGU5MDgyYjMzOTU2OGFkMTVlN2E5Y2U4; st_data=32af49ffbd233b4a4220b0bf2eae55e95fcbee219829d657b11bc95c856e255a6f46fd0109de69ce337ac708a691931e6ba2cb3bc3067d8411731e2f01a70e9006935a985e587c0ba22829832a27f4e1c38c7b33ebc6d926a554ef32294298f8aca57668e4b1c912fd44e9b4673bae572e17d9e7b580c64c72ca593af9efe825; st_sign=89abe025'
    ,"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",

    }
    tieba_batch_sign()

    # https: // tieba.baidu.com / f?kw = % CF % C9 % BD % A3 % C6 % E6 % CF % C0 % B4 % AB

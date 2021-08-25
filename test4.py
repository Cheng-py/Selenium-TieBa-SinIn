# import requests
#
# url = "https://blog.csdn.net/weixin_45986798"
#
# headers = {"User_Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
#     # "Cookie" : 'uuid_tt_dd=10_18740448650-1586913181989-915645; __gads=ID=0330a19343fb9853:T=1586913183:S=ALNI_MaUr3OH9TGK6oSMLE5gXgU09LXmWQ; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_18740448650-1586913181989-915645!5744*1*weixin_45986798; ssxmod_itna=GqfxgiDQo7qCqGKGHiiQR3qYwqEGQi8Q7KmaDlarYxA5D8D6DQeGTb2iqob8o83KBDp4DuGx4meAQ6jbRpP7G8oN=bDCPGnDBF2LqmDYA8Dt4DTD34DYDirQGIDieDFF5H/8DbxYQDmxiODlKH6xDa0xi3LxGaD40Ol69DLaKDR25D0Z+FDQKDu6IC8OoG14D1PoHPajKD9ZoDsrijojFIRbk49ovfjKq5DB+NqMT4aelT5Hr+AWIG4/YDjxB8DmeH1KjkBp7NiG+KT7a7PPzPtlwxqjTg=QDqAX4oPphxPpirLuRPlnNDiahwhxVoD=; ssxmod_itna2=GqfxgiDQo7qCqGKGHiiQR3qYwqEGQi8Q7KQD61tAax0yiY038C2NDu7n4Pvev6LyN56Uoj4rw/DSBYrzdo9CowFQC98S0FKtFZ3GFnjpD9RWqK=dFAVf9URGFwrH2MCjnyf5AzF6jko4DlYYYW=08SfxUE32KTwpQejB+gI2ifp56g3GDu+se2Ro=bxynjQz+Wq=MfL3KWjO9bFwleb86ut=IQ0sbiTQNPjR0mY0j17aE1GOulusKUQkNI51Ntgkw/Ohg/tOrjuC5u85kI8=k9Swvz7cEZ3wcCyha3HjACMff0t2jPoqPE7GjRWxGaxwYI4Fpk0q+16gWK2WUgeK=l3+DLx+06mi=zwCjK3aiHBrkZI=+U/ERxFi+Bwlxe7UUFDT1aP73NkzXlrGkB+lPTGPWMAqm=inPWQgA/xr+tQsg67/R=4ajjuvPajZ=Lrd=W0ptNkpW/=mCgq8BITDG2DrPQmxwrx8KXQ+khL1IMQGGrUr4nrCdDmepK7eGRdxKQm+eGl23FCTexGuk8ErTA2/lhoUlHV2P2kQ9lQSQd7aC1i=7i40mPmTOr6+FZQUeDFqD+pDxD==; UserName=weixin_45986798; UserInfo=0f2d3ab507f64c9ea026e68a94b55a7a; UserToken=0f2d3ab507f64c9ea026e68a94b55a7a; UserNick=Cheng.+py; AU=C16; UN=weixin_45986798; BT=1627955098018; p_uid=U010000; Hm_up_6bcd52f51e9b3dce32bec4a3997715ac={"uid_":{"value":"weixin_45986798","scope":1},"islogin":{"value":"1","scope":1},"isonline":{"value":"1","scope":1},"isvip":{"value":"0","scope":1}}; Hm_lvt_e5ef47b9f471504959267fd614d579cd=1629275661,1629353008,1629363438; firstDie=1; is_advert=1; dc_sid=7f1f20ebf1f76a044b830aa69a40e00e; c_first_ref=www.baidu.com; c_segment=13; c_first_page=https://blog.csdn.net/williamgavin/article/details/81390014; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1629689145,1629690124,1629691176,1629691219; dc_session_id=10_1629697045559.143630; c_ref=https://blog.csdn.net/weixin_45986798?spm=1001.2101.3001.5343; c_pref=https://blog.csdn.net/weixin_45986798?spm=1001.2101.3001.5343; c_page_id=default; dc_tos=qya2ar; log_Id_pv=1211; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1629697060; log_Id_view=2613; log_Id_click=669'
# }
# response = requests.get(url=url, headers = headers ).text
# # with open("csdn.html", "w", encoding="utf-8") as f:
# #     f.write(.decode())
# print(response)

# import requests
# url = 'https://www.baidu.com'
#
# res = requests.get(url=url)
# print(res.text)

# from selenium import webdriver
# from selenium.webdriver.common import keys
#
# url = "http://www.baidu.com"
# driver = webdriver.Chrome()
# driver.get(url)
# driver.find_element_by_xpath('//*[@id="s-top-left"]/a[6]').click()
# res = driver.window_handles[1]
# driver.switch_to.window(driver.window_handles[0])
# driver.switch_to.window(driver.window_handles[1])

import requests

headers ={
    'cookie':'BIDUPSID=434B76AC4C98285BBCE35970C1F850D7; PSTM=1586866907; bdshare_firstime=1586939172256; rpln_guide=1; SEENKW=steam#三和大神; __yjs_duid=1_ec83e1938ec710747f47e7a3536745dc1621345304820; BAIDUID=2EC805F8913C1D80A03F6027EBFC3DCB:FG=1; MCITY=-:; st_key_id=17; USER_JUMP=-1; baidu_broswer_setup_å«æˆ‘æ–‡å“¥ORçˆ¸çˆ¸=0; video_bubble0=1; delPer=0; PSINO=3; BAIDUID_BFESS=2EC805F8913C1D80A03F6027EBFC3DCB:FG=1; BDRCVFR[0idcJUX_hP6]=mk3SLVN4HKm; BAIDU_WISE_UID=wapp_1629704111843_898; BDUSS=HVZYmNKV2VjM1FhdXYxc3Y1c2oyRHVOSktTY0N1dlU5aDk3cHVRN0VHdkkzRXBoRVFBQUFBJCQAAAAAAAAAAAEAAACg4JBavdDO0s7EuOdPUrDWsNYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMhPI2HITyNha; BDUSS_BFESS=HVZYmNKV2VjM1FhdXYxc3Y1c2oyRHVOSktTY0N1dlU5aDk3cHVRN0VHdkkzRXBoRVFBQUFBJCQAAAAAAAAAAAEAAACg4JBavdDO0s7EuOdPUrDWsNYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMhPI2HITyNha; STOKEN=ae69d82dfa6190b3c097cbfc8c2708c5c41c40f4a3d258eb937f693563bcee74; 1519444128_FRSVideoUploadTip=1; video_bubble1519444128=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_PSSID=31660_26350; BA_HECTOR=0galag81ah84a185121gi6kbt0r; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; wise_device=0; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1629699714,1629699723,1629704098,1629704943; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1629705450; ab_sr=1.0.1_N2Q5OGU5NmU2MmFkZDQyMTUyZDFiNTJiNDA4NGVlN2Q2MzMxMjY5ZmY3NzY1ZmU3NTIzMjM3NDRjYWRkYmUxNzIwZmMyZDY1MDU1MWZhYjEyN2Y1ZmE0NjMxNTNiMGNhMjYxMzFkNTI5Y2NlODk3NThkOTc4ODM2Y2Y3ZWFjYWMyZTQzNWU1MjcyZWIwMzVlNzQ1YmQ2NGI1N2U2ZWM0ZTZjMjNiMGIzMWVlNTg3ZjIyYWY0OTcwMDlmYjRiYTcx; st_data=29c5297b7d4d0e16af49f66d9c4a0ca4a3a9557a38fe1b995e1705fc5c470a032915d276fe9aa544394b20ee16dc9d0e2c38bede1bdb7404dbed2d6684da2f2fbd725dce164ab5dfe48003c033a89b533922ad8a239f4b408eb7405de8236bda3f5f77e35aa7b98339a5b47c62dc308de2f325c3b554bd7bb4d0cdc80fec9b32; st_sign=dbc875c5'.encode('UTF-8').decode('latin-1')

}
url = "https://tieba.baidu.com/"

res = requests.get(url=url,headers=headers).text
print(res)





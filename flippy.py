import requests



#one does not simply 61579
#payload = {'template_id': '61579','text0':'LOL'}
#r = requests.post(CaptionImageApi,params=payload)
#data = r.json()
#print(data)


class Flippy:
	GetMemesApi = "https://api.imgflip.com/get_memes"
	CaptionImageApi = "https://api.imgflip.com/caption_image"
	data = {}
	def genMeme(template_id, username, password, text0, text1, font="impact", max_font_size="50", boxes={}):
		payload=dict([('template_id',template_id), ('username',username),
				('password',password),('text0',text0),('text1',text1),
				('font',font),('max_font_size',max_font_size),
				('boxes',boxes)])
		print(payload)

flippy = Flippy()
flippy.genMeme("Template","Username","Password","Text0","Text1","Font")


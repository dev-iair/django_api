import requests

file_path = '/app/sample.jpg'
host = 'http://api' # local
external_host = 'http://192.168.1.1:8000' # external
save_path = '/app'
data = {'type': 'image', 'option':'save'}
files = {'file': (open(file_path, 'rb'))}

res = requests.post(host + '/file', data=data, files=files)

#write return file
with open(save_path+'/res.json', 'wb') as f:
    f.write(res.content)
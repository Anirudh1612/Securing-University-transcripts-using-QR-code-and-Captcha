from captcha.image import ImageCaptcha
import matplotlib.pyplot as plt
import random
import pyqrcode
from PIL import Image
from pyzbar.pyzbar import decode
import socket
import webbrowser
if __name__ == '__main__':

	
	
	server_ip ='127.0.0.1'
	port = 5214
    
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((server_ip , port))
	s.listen(1)
	c , addr = s.accept()
	print ("Connection from:" + str(addr))
    
	while (True):
		data = c.recv(1024)
		captcha_text = str(data.decode('utf-8'))
		if not data:
			break
		#print ("From connected User -- "+ str(data))
		data = str(data).upper()
		#print ("Sending:"+str(data))
		c.sendall(data.encode('utf-8'))

		c.close()
		break
	im = Image.open('captcha.png')
	im.show()
	
	
	
	print(str(data))
	input2 = input("Enter the displayed captcha ")
	set1 = set(captcha_text.split(' '))
	set2 = set(input2.split(' '))
	new=1;
	flag=0
	for i in range(3):
		print("Attemtpt Number = ",i+1) 
		if(set1 == set2):
			print("Captcha matched")
			flag = 0
			data = decode(Image.open('qr.png'))
			#print(data[0][0])
			print(data[0][0].decode("utf-8") )
			#print(len(data))
			webbrowser.open(str(data[0][0].decode("utf-8")),new=new);
			break
		else:
			flag = 1
			#print("Captcha not matched")
	if(flag==1):
		print("Captcha not matched")

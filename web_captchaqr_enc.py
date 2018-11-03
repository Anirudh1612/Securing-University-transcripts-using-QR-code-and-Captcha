from captcha.image import ImageCaptcha
import matplotlib.pyplot as plt
import random
import pyqrcode
from PIL import Image
from pyzbar.pyzbar import decode
import socket
# The number list, lower case character list and upper case character list are used to generate captcha text.
number_list = ['0','1','2','3','4','5','6','7','8','9']

alphabet_lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

alphabet_uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# This function will create a random captcha string text based on above three list.
# The input parameter is the captcha text length.
def create_random_captcha_text(captcha_string_size=8):

    captcha_string_list = []

    base_char = alphabet_lowercase + alphabet_uppercase + number_list

    for i in range(captcha_string_size):

        # Select one character randomly.
        char = random.choice(base_char)

        # Append the character to the list.
        captcha_string_list.append(char)

    captcha_string = ''

    # Change the character list to string.    
    for item in captcha_string_list:
        captcha_string += str(item)

    return captcha_string

# This function will create a fully digital captcha string text.
def create_random_digital_text(captcha_string_size=10):

    captcha_string_list = []
    # Loop in the number list and return a digital captcha string list
    for i in range(captcha_string_size):
        char = random.choice(number_list)
        captcha_string_list.append(char)
        
    captcha_string = ''

    # Convert the digital list to string.    
    for item in captcha_string_list:
        captcha_string += str(item)

    return captcha_string

# Create an image captcha with special text.
def create_image_captcha(captcha_text):
    image_captcha = ImageCaptcha()
    # Create the captcha image.
    image = image_captcha.generate_image(captcha_text)

    # Add noise curve for the image.
    image_captcha.create_noise_curve(image, image.getcolors())

    # Add noise dots for the image.
    image_captcha.create_noise_dots(image, image.getcolors())

    # Save the image to a png file.
    image_file = "./captcha.png"
    image_captcha.write(captcha_text, image_file)
    print("Generating a random captcha ...")

    # Display the image in a matplotlib viewer.
    plt.imshow(image)
    plt.show()

    print(image_file + " has been created.")
    return

if __name__ == '__main__':
    # Create random text.
    captcha_text = create_random_captcha_text()
    #print(captcha_text)
    #input1 = input( u"https://www.geeksforgeeks.org/")
    qr = pyqrcode.create(u"file:///C:/Users/Vijaya%20Sharma/Desktop/text_captcha/result.html")
    print("Generating the qr code ...")	

    qr.png("qr.png",scale=10)

    # Create image captcha.
    create_image_captcha(captcha_text)
	# tcp server
    host = '127.0.0.1'
    port = 5214
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port)) 
    message = captcha_text

    

    s.sendall(message.encode('utf-8'))
    data = s.recv(1024)
    

    s.close
	
    #input2 = input("Enter the displayed captcha ")
    #set1 = set(captcha_text.split(' '))
    #set2 = set(input2.split(' '))
    #if(set1 == set2):
       
        #data = decode(Image.open('qr.png'))
        #print(data)
		
    #else:
	   # print("Captcha not matched")
	

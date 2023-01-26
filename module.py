import cv2
import numpy as np
import matplotlib.pyplot as plt
import random
def gaussian_noise(image, mean = 0, sigma = 1):
	img = np.copy(image)
	noise = np.random.normal(mean, sigma, img.shape)
	return np.clip(img + noise, 0, 255).astype('uint8')

def salt_pepper_noise(image, fraction, salt_vs_pepper):
	img = np.copy(image)
	size = img.size
	num_salt = np.ceil(fraction * size * salt_vs_pepper).astype('int')
	num_pepper = np.ceil(fraction * size * (1 - salt_vs_pepper)).astype('int')
	row, column,_ = img.shape

	x = np.random.randint(0, column - 1, num_pepper)
	y = np.random.randint(0, row - 1, num_pepper)
	img[y, x] = 0  

	x = np.random.randint(0, column - 1, num_salt)
	y = np.random.randint(0, row - 1, num_salt)
	img[y, x] = 255 
	return img
	
def show_img(img):
	cv2.imshow('My Image',img/255)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def showFilter(mask):
	cv2.imshow('My Image',mask)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def Transform(img):
	img = img.astype(int)
	p,q,r = img.shape
	for i in range(p):
		for j in range(q):
			if((i+j)%2)==1:
				img[i,j,:] *= -1
	return img
	
def Fourier(img):
	FFt_img = np.zeros(img.shape,dtype=np.complex)
	for i in range(img.shape[2]):
		FFt_img[:,:,i] = np.fft.fft2(img[:,:,i])
	return FFt_img

def Inv_Fourier(img):
	iFFt_img = np.zeros(img.shape,dtype=np.complex)
	for i in range(img.shape[2]):
		iFFt_img[:,:,i] = np.fft.ifft2(img[:,:,i])
	return iFFt_img

def idealHighPassfilter(img,D_0):
	row,col = img.shape[0],img.shape[1]
	center_x,center_y = int(row/2),int(col/2)
	res = np.zeros((row,col))
	for i in range(row):
		for j in range(col):
			x = (i-center_x)**2
			y = (j-center_y)**2
			if (x + y)**0.5 <= D_0:
				res[i,j] = 0
			else:
				res[i,j] = 1 
	return res

def ButterworthHighPassfilter(img,D_0,n = 2):
	row,col = img.shape[0],img.shape[1]
	center_x,center_y = int(row/2),int(col/2)
	res = np.zeros((row,col))
	for i in range(row):
		for j in range(col):
			x = (i-center_x)**2
			y = (j-center_y)**2
			D_uv = (x+y)**0.5
			res[i,j] = 1 - 1/(1 + ((D_uv/D_0)**(n*2)))
	return res

def GassuianHighPassfilter(img,D_0):
	row,col = img.shape[0],img.shape[1]
	center_x,center_y = int(row/2),int(col/2)
	res = np.zeros((row,col))
	for i in range(row):
		for j in range(col):
			x = (i-center_x)**2
			y = (j-center_y)**2
			res[i,j] = 1 - np.exp(-(x+y)/(2*D_0*D_0))
	return res

def idealLowPassfilter(img,D_0):
	row,col = img.shape[0],img.shape[1]
	center_x,center_y = int(row/2),int(col/2)
	res = np.zeros((row,col))
	for i in range(row):
		for j in range(col):
			x = (i-center_x)**2
			y = (j-center_y)**2
			if (x + y)**0.5 <= D_0:
				res[i,j] = 1
			else:
				res[i,j] = 0 
	return res
	
def ButterworthLowPassfilter(img,D_0,n = 2):
	row,col = img.shape[0],img.shape[1]
	center_x,center_y = int(row/2),int(col/2)
	res = np.zeros((row,col))
	for i in range(row):
		for j in range(col):
			x = (i-center_x)**2
			y = (j-center_y)**2
			D_uv = (x+y)**0.5
			res[i,j] = 1/(1 + ((D_uv/D_0)**(n*2)))
	return res	
		
def GassuianLowPassfilter(img,D_0):
	row,col = img.shape[0],img.shape[1]
	center_x,center_y = int(row/2),int(col/2)
	res = np.zeros((row,col))
	for i in range(row):
		for j in range(col):
			x = (i-center_x)**2
			y = (j-center_y)**2
			res[i,j] = np.exp(-(x+y)/(2*D_0*D_0))
	return res

def Dot(img,kernel):
	res = np.zeros(img.shape,dtype=np.complex)
	for i in range(img.shape[2]):
		res[:,:,i] = img[:,:,i]*kernel
	return res
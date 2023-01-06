import cv2
import numpy as np
import matplotlib.pyplot as plt
from module import Dot,GassuianLowPassfilter,ButterworthLowPassfilter,idealLowPassfilter,GassuianHighPassfilter,ButterworthHighPassfilter,idealHighPassfilter,Inv_Fourier,Fourier,Transform,showFilter,show,salt_pepper_noise,gaussian_noise

def concat_imgh(imgList):
	if len(imgList) >= 2:
		res = np.hstack((imgList[0],imgList[1]))
		for i in range(2,len(imgList)):
			res = np.hstack((res,imgList[i]))
		return res
	elif len(imgList) == 1:
		return imgList[0]
	else:
		return []
def concat_imgv(imgList):
	if len(imgList) >= 2:
		res = np.vstack((imgList[0],imgList[1]))
		for i in range(2,len(imgList)):
			res = np.vstack((res,imgList[i]))
		return res
	elif len(imgList) == 1:
		return imgList[0]
	else:
		return []
def LowPassFilter(img,D_0,tp = 'Gassiuan',n = 2):	
	transimg = Transform(img)
	FFt_img = Fourier(transimg)
	
	if tp == 'ideal':
		lowPassFilter = idealLowPassfilter(img,D_0)
	elif tp == 'Butterworth':
		lowPassFilter = ButterworthLowPassfilter(img,D_0,n = n) 
	else:
		lowPassFilter = GassuianLowPassfilter(img,D_0)
		
	res = Dot(FFt_img,lowPassFilter)
	res = Inv_Fourier(res)
	res = np.real(res)
	res = Transform(res)
	return res

def HighPassFilter(img,D_0,tp = 'Gassiuan',n = 2):	
	transimg = Transform(img)
	FFt_img = Fourier(transimg)
	
	if tp == 'ideal':
		HighPassFilter = idealHighPassfilter(img,D_0)
	elif tp == 'Butterworth':
		HighPassFilter = ButterworthHighPassfilter(img,D_0,n = n)
	else:
		HighPassFilter = GassuianHighPassfilter(img,D_0)
		
	res = Dot(FFt_img,HighPassFilter)
	res = Inv_Fourier(res)
	res = np.real(res)
	res = Transform(res)
	return res+img,res

def Hybrid(img1,img2,kernel_type,D_0_value,idx,sigma1 = 25,sigma2 = 10):
	HighresImg = []
	HighresEdge = []
	LowresImg = []
	
	for tp in kernel_type:
		HighresimgList = []
		EdgeimgList = []
		LowresimgList = []
		
		for D_0 in D_0_value:
			highPassres,Edge = HighPassFilter(img1,D_0,tp = tp)
			lowPassres = LowPassFilter(img2,D_0,tp = tp)
			HighresimgList.append(highPassres)
			EdgeimgList.append(Edge)
			LowresimgList.append(lowPassres)

		HighresImg.append(concat_imgh(HighresimgList))
		HighresEdge.append(concat_imgh(EdgeimgList))
		LowresImg.append(concat_imgh(LowresimgList))
		
	highPassres = concat_imgv(HighresImg)
	Edges = concat_imgv(HighresEdge)
	lowPassres = concat_imgv(LowresImg)
	#show(highPassres)
	#show(lowPassres)
	#show(lowPassres+Edges)
	
	cv2.imwrite('result/highres/'+str(idx)+'.jpg', highPassres) 
	cv2.imwrite('result/lowres/'+str(idx)+'.jpg', lowPassres)
	cv2.imwrite('result/hybrid_1/'+str(idx)+'.jpg', lowPassres+Edges) 
	
	HybridImg = []
	for tp in kernel_type:
		highPassres,Edge = HighPassFilter(img1,sigma1,tp = tp)
		lowPassres = LowPassFilter(img2,sigma2,tp = tp)
		HybridImg.append(Edge+lowPassres)

	hybridres = concat_imgh(HybridImg)
	return hybridres

if __name__ == '__main__':
	img = cv2.imread('einstein.bmp', cv2.IMREAD_COLOR)
	img = cv2.resize(img,(225,265))
	row,col,channel = img.shape
	#show(gaussian_noise(img,0,15))
	#show(salt_pepper_noise(img, 0.1, 0.5))
	
	kernel_type = ['ideal','Butterworth','Gassiuan']
	D_0_value = [10,50,100]
	
	imgL1 = ['Afghan_girl_after.jpg','1_bicycle.bmp','2_bird.bmp','3_cat.bmp','5_fish.bmp','6_makeup_before.jpg','a_1.png','b_1.png','einstein.bmp']
	imgL2 = ['Afghan_girl_before.jpg','1_motorcycle.bmp','2_plane.bmp','3_dog.bmp','5_submarine.bmp','6_makeup_after.jpg','a_2.png','b_2.png','marilyn.bmp']

	hybrids = []
	idx,idx2 = 0,0

	for im1,im2 in zip(imgL1,imgL2):
		img1 = cv2.imread('input/'+im1, cv2.IMREAD_COLOR)
		img1 = cv2.resize(img1,(225,265))
		
		img2 = cv2.imread('input/'+im2, cv2.IMREAD_COLOR)
		img2 = cv2.resize(img2,(225,265))
		hybrid = Hybrid(img1,img2,kernel_type,D_0_value,idx,sigma1 = 25,sigma2 = 10)
		hybrids.append(hybrid)
		idx += 1
		
		if idx % 3 == 0:
			hybridsres = concat_imgv(hybrids)
			cv2.imwrite('result/hybrid_2/'+str(idx2)+'.jpg', hybridsres) 
			hybrids = []
			idx2 += 1
			
	print('Done.')
	#show(hybridsres)
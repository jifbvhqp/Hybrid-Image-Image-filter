import os
import cv2
import tkinter as tk
from tkinter import Variable, filedialog,ttk
from PIL import Image, ImageTk
from module import Dot,GassuianLowPassfilter,ButterworthLowPassfilter,idealLowPassfilter,GassuianHighPassfilter,ButterworthHighPassfilter,idealHighPassfilter,Inv_Fourier,Fourier,Transform,showFilter,show_img,salt_pepper_noise,gaussian_noise
from main import LowPassFilter,HighPassFilter
import numpy as np

init_d_0 = 30
init_n = 2
width = 225*2
height = 265*2
window_size = (width,height)
subwindow_size = (90,90)

root = tk.Tk()
root.title('頻率域不同濾波器不同參數之比較')
root.geometry('1200x600')
left_image = None
right_image = None
left_filter_mask_image = None
right_filter_mask_image = None
left_filter = 'low_pass'
left_filter_type = 'ideal'
right_filter = 'low_pass'
right_filter_type = 'ideal'

def set_canvas_image(canvas,img,channel,edges_img = False):
    if channel == 3:
        if edges_img == True:
            img = cv2.resize(img,subwindow_size)  
        b,g,r = cv2.split(img)
        img = cv2.merge((r,g,b))
    else:
        img = cv2.resize(img,subwindow_size)  
        img *= 255

    im = Image.fromarray(np.clip(img, 0, 255).astype('uint8'))    

    w,h = img.shape[0],img.shape[1]                         # 取得圖片長寬
    tk_img = ImageTk.PhotoImage(im)                         # 轉換成 tk 圖片物件
    canvas.delete('all')                                    # 清空 Canvas 原本內容
    #canvas.config(scrollregion=(0,0,w,h))                  # 改變捲動區域
    canvas.create_image(0, 0, anchor='nw', image=tk_img)    # 建立圖片
    canvas.tk_img = tk_img                                  # 修改屬性更新畫面

def update(img,canvas,subcanvas,subedgesCanvas,side,d_0 = init_d_0,n = init_n): 
    if side == 'left':
        if left_filter_type == 'ideal':
            if left_filter == 'low_pass':
                img,filter_image = LowPassFilter(img,d_0,'ideal')
            else:
                img,Edge,filter_image  = HighPassFilter(img,d_0,'ideal')
                img = img + Edge

        elif left_filter_type == 'Butterworth':
            if left_filter == 'low_pass':
                img,filter_image  = LowPassFilter(img,d_0,'Butterworth',n = n)
            else:
                img,Edge,filter_image  = HighPassFilter(img,d_0,'Butterworth',n = n)
                img = img + Edge

        elif left_filter_type == 'Gassiuan':
            if left_filter == 'low_pass':
                img,filter_image  = LowPassFilter(img,d_0,'Gassiuan')
            else:
                img,Edge,filter_image = HighPassFilter(img,d_0,'Gassiuan')
                img = img + Edge

    else:
        if right_filter_type == 'ideal':
            if right_filter == 'low_pass':
                img,filter_image = LowPassFilter(img,d_0,'ideal')
            else:
                img,Edge,filter_image = HighPassFilter(img,d_0,'ideal')
                img = img + Edge

        elif right_filter_type == 'Butterworth':
            if right_filter == 'low_pass':
                img,filter_image = LowPassFilter(img,d_0,'Butterworth',n = n)
            else:
                img,Edge,filter_image = HighPassFilter(img,d_0,'Butterworth',n = n)
                img = img + Edge

        elif right_filter_type == 'Gassiuan':
            if right_filter == 'low_pass':
                img,filter_image = LowPassFilter(img,d_0,'Gassiuan')
            else:
                img,Edge,filter_image = HighPassFilter(img,d_0,'Gassiuan')
                img = img + Edge

    global left_filter_mask_image
    global right_filter_mask_image
    
    if side == 'left':
        left_filter_mask_image = filter_image
    else:
        right_filter_mask_image = filter_image
     
    set_canvas_image(canvas,img,3,edges_img = False)
    set_canvas_image(subcanvas,filter_image,1)
    if side == 'right' and right_filter == 'high_pass':
        set_canvas_image(subedgesCanvas,np.clip(Edge, 0, 255).astype('uint8'),3,edges_img = True)
    if side == 'left' and left_filter == 'high_pass':
        set_canvas_image(subedgesCanvas,np.clip(Edge, 0, 255).astype('uint8'),3,edges_img = True)

def show(canvas,subcanvas,subedgesCanvas,side):
    img_path = filedialog.askopenfilename(filetypes=[('png', '*.png'),('jpg', '*.jpg'),('bmp', '*.bmp'),('BMP', '*.BMP'),("All Files", "*.*")])  # 指定開啟檔案格式
    img = cv2.imread(img_path)
    img = cv2.resize(img,window_size)
    global left_image
    global right_image
    if side == 'left':
        left_image = img
    else:
        right_image = img
    update(img,canvas,subcanvas,subedgesCanvas,side)

def set_filter(filter_num,canvas,subcanvas,subedgesCanvas,filterlabel,stringText,side):
    global left_filter
    global right_filter
    if side == 'left':
        if left_filter_type == 'ideal':
            tx = '理想'
        elif left_filter_type == 'Butterworth':
            tx = '巴特沃斯'
        else:
            tx = '高斯'

        if filter_num == 1:
            left_filter = 'low_pass'
            filterlabel.set(tx+'低通濾波器')
        elif filter_num == 2:   
            left_filter = 'high_pass'
            filterlabel.set(tx+'高通濾波器')
    else:
        if right_filter_type == 'ideal':
            tx = '理想'
        elif right_filter_type == 'Butterworth':
            tx = '巴特沃斯'
        else:
            tx = '高斯'
        if filter_num == 1:
            right_filter = 'low_pass'
            filterlabel.set(tx+'低通濾波器')
        elif filter_num == 2:   
            right_filter = 'high_pass'
            filterlabel.set(tx+'高通濾波器')

    image = left_image if side == 'left' else right_image
    update(image,canvas,subcanvas,subedgesCanvas,side,d_0 = int(stringText.get()))

def set_filter_type(filter_type_num,canvas,subcanvas,subedgesCanvas,filterlabel,stringText,side):
    global left_filter_type
    global right_filter_type

    if side == 'left':
        tx = '高通' if left_filter == 'high_pass' else '低通'
        if filter_type_num == 1:
            left_filter_type = 'ideal'
            filterlabel.set('理想'+tx+'濾波器')
        elif filter_type_num == 2:   
            left_filter_type = 'Butterworth'
            filterlabel.set('巴特沃斯'+tx+'濾波器')
        elif filter_type_num == 3:
            left_filter_type = 'Gassiuan'
            filterlabel.set('高斯'+tx+'濾波器')
    else:
        tx = '高通' if right_filter == 'high_pass' else '低通'
        if filter_type_num == 1:
            right_filter_type = 'ideal'
            filterlabel.set('理想'+tx+'濾波器')
        elif filter_type_num == 2:   
            right_filter_type = 'Butterworth'
            filterlabel.set('巴特沃斯'+tx+'濾波器')
        elif filter_type_num == 3:
            right_filter_type = 'Gassiuan'
            filterlabel.set('高斯'+tx+'濾波器')
    image = left_image if side == 'left' else right_image
    update(image,canvas,subcanvas,subedgesCanvas,side,d_0 = int(stringText.get()))


# 定義顯示函式，注意一定要有一個參數
def update_value(canvas,subcanvas,subedgesCanvas,scale_h,side,stringText):
    image = left_image if side == 'left' else right_image
    update(image,canvas,subcanvas,subedgesCanvas,side,d_0 = int(scale_h.get()))
    stringText.set(f'{int(scale_h.get())}')

def update_n(canvas,subcanvas,subedgesCanvas,scale_h,scale_n,side,stringText):
    image = left_image if side == 'left' else right_image
    update(image,canvas,subcanvas,subedgesCanvas,side,d_0 = int(scale_h.get()), n = int(scale_n.get()))
    stringText.set(f'{int(scale_n.get())}')


frame = tk.Frame(root, width=window_size[0], height=window_size[1])
frame.place(x=0,y=0,height=600,width=1200)



canvas_left = tk.Canvas(frame, width=window_size[0], height=window_size[1], bg='#fff')
canvas_left.place(x=100,y=5,height=window_size[1],width=window_size[0])

sub_canvas_left = tk.Canvas(frame, width=90, height=90, bg='#fff')
sub_canvas_left.place(x=0,y=480,height=90,width=90)

sub_edgesCanvas_left = tk.Canvas(frame, width=90, height=90, bg='#fff')
sub_edgesCanvas_left.place(x=0,y=380,height=90,width=90)

left_value = tk.StringVar()   # 定義文字變數
#left_value.set('d₀='+str(init_d_0))
left_value.set(str(init_d_0))

scale_h_left = ttk.Scale(root, from_=30, to=150, orient='horizontal', command=lambda e: update_value(canvas_left,sub_canvas_left,sub_edgesCanvas_left,scale_h_left,'left',left_value))  # 改變時執行 show
scale_h_left.set(init_d_0)
scale_h_left.place(x=255,y=560)

low_filter_button_left = tk.Button(root, text='低通濾波器',command=lambda: set_filter(1,canvas_left,sub_canvas_left,sub_edgesCanvas_left,left_filterlabel,left_value,'left'))
low_filter_button_left.place(x=2,y=50,height=20,width=70)

high_filter_button_left = tk.Button(root, text='高通濾波器',command=lambda: set_filter(2,canvas_left,sub_canvas_left,sub_edgesCanvas_left,left_filterlabel,left_value,'left'))
high_filter_button_left.place(x=2,y=70,height=20,width=70)

ideal_filter_button_left = tk.Button(root, text='理想濾波器',command=lambda: set_filter_type(1,canvas_left,sub_canvas_left,sub_edgesCanvas_left,left_filterlabel,left_value,'left'))
ideal_filter_button_left.place(x=2,y=110,height=20,width=70)

Butterworth_filter_button_left = tk.Button(root, text='巴斯沃特濾波',command=lambda: set_filter_type(2,canvas_left,sub_canvas_left,sub_edgesCanvas_left,left_filterlabel,left_value,'left'))
Butterworth_filter_button_left.place(x=2,y=130,height=20,width=70)

Gassuian_filter_button_left = tk.Button(root, text='高斯濾波器',command=lambda: set_filter_type(3,canvas_left,sub_canvas_left,sub_edgesCanvas_left,left_filterlabel,left_value,'left'))
Gassuian_filter_button_left.place(x=2,y=150,height=20,width=70)

button_left = tk.Button(root, text='開啟圖片', command=lambda: show(canvas_left,sub_canvas_left,sub_edgesCanvas_left,'left'))
button_left.place(x=280,y=540,height=20,width=50)

label_left = tk.Label(root, textvariable=left_value)
label_left.place(x=290,y=585,height=15,width=50)

left_n = tk.StringVar() 
#left_n.set('n='+str(init_n))
left_n.set(str(init_n))

scale_h_left_n = ttk.Scale(root, from_=2, to=20, orient='horizontal', command=lambda e: update_n(canvas_left,sub_canvas_left,sub_edgesCanvas_left,scale_h_left,scale_h_left_n,'left',left_n))  # 改變時執行 show
scale_h_left_n.set(init_n)
scale_h_left_n.place(x=380,y=560)

label_left_n = tk.Label(root, textvariable=left_n)
label_left_n.place(x=415,y=585,height=15,width=50)

left_filterlabel = tk.StringVar() 
left_filterlabel.set(str('理想低通濾波器'))

label_filter_left = tk.Label(root, textvariable=left_filterlabel)
label_filter_left.place(x=80,y=570,height=15,width=150)

canvas_right = tk.Canvas(frame, width=window_size[0], height=window_size[1], bg='#fff')
canvas_right.place(x=650,y=5,height=window_size[1],width=window_size[0])

sub_canvas_right = tk.Canvas(frame, width=90, height=90, bg='#fff')
sub_canvas_right.place(x=1110,y=480,height=90,width=90)

sub_edgesCanvas_right = tk.Canvas(frame, width=90, height=90, bg='#fff')
sub_edgesCanvas_right.place(x=1110,y=380,height=90,width=90)

button_right = tk.Button(root, text='開啟圖片', command=lambda: show(canvas_right,sub_canvas_right,sub_edgesCanvas_right,'right'))
button_right.place(x=850,y=540,height=20,width=50)

right_value = tk.StringVar()   # 定義文字變數
#right_value.set('d₀='+str(init_d_0))
right_value.set(str(init_d_0))

scale_h_right = ttk.Scale(root, from_=30, to=150, orient='horizontal', command=lambda e: update_value(canvas_right,sub_canvas_right,sub_edgesCanvas_right,scale_h_right,'right',right_value))  # 改變時執行 show
scale_h_right.set(init_d_0)
scale_h_right.place(x=825,y=560)

label_right = tk.Label(root, textvariable=right_value)
label_right.place(x=860,y=585,height=15,width=50)

right_n = tk.StringVar() 
#right_n.set('n='+str(init_n))
right_n.set(str(init_n))

scale_h_right_n = ttk.Scale(root, from_=2, to=20, orient='horizontal', command=lambda e: update_n(canvas_right,sub_canvas_right,sub_edgesCanvas_right,scale_h_right,scale_h_right_n,'right',right_n))  # 改變時執行 show
scale_h_right_n.set(init_n)
scale_h_right_n.place(x=950,y=560)

label_right_n = tk.Label(root, textvariable=right_n)
label_right_n.place(x=985,y=585,height=15,width=50)

right_filterlabel = tk.StringVar() 
right_filterlabel.set(str('理想低通濾波器'))

label_filter_right = tk.Label(root, textvariable=right_filterlabel)
label_filter_right.place(x=650,y=570,height=15,width=150)

low_filter_button_right = tk.Button(root, text='低通濾波器',command=lambda: set_filter(1,canvas_right,sub_canvas_right,sub_edgesCanvas_right,right_filterlabel,right_value,'right'))
low_filter_button_right.place(x=1125,y=50,height=20,width=70)

high_filter_button_right = tk.Button(root, text='高通濾波器',command=lambda: set_filter(2,canvas_right,sub_canvas_right,sub_edgesCanvas_right,right_filterlabel,right_value,'right'))
high_filter_button_right.place(x=1125,y=70,height=20,width=70)

ideal_filter_button_right = tk.Button(root, text='理想濾波器',command=lambda: set_filter_type(1,canvas_right,sub_canvas_right,sub_edgesCanvas_right,right_filterlabel,right_value,'right'))
ideal_filter_button_right.place(x=1125,y=110,height=20,width=70)

Butterworth_filter_button_right = tk.Button(root, text='巴斯沃特濾波',command=lambda: set_filter_type(2,canvas_right,sub_canvas_right,sub_edgesCanvas_right,right_filterlabel,right_value,'right'))
Butterworth_filter_button_right.place(x=1125,y=130,height=20,width=70)

Gassuian_filter_button_right = tk.Button(root, text='高斯濾波器',command=lambda: set_filter_type(3,canvas_right,sub_canvas_right,sub_edgesCanvas_right,right_filterlabel,right_value,'right'))
Gassuian_filter_button_right.place(x=1125,y=150,height=20,width=70)


root.mainloop()
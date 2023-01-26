# Hybrid-Image-Image-filter

Hybrid Image & 不同頻率域濾波器不同參數之比較 <br>
## Result (Hybrid Image)
每Col代表不同濾波器
第一Col 使用理想濾波器,第二Col 使用巴特沃斯濾波器 $n=2$,第三Col 使用高斯濾波器<br>
高通濾波參數 $D_0 = 25$, 低通濾波參數 $D_0 = 10$<br>
![1](https://user-images.githubusercontent.com/49235533/210938177-5ec01e41-6ea0-4b56-840b-53ab1817d268.jpg)

## Install requirements
```C
pip install -r requirements.txt
```

## Exeucte
```C
python main.py
```
## 2維影像離散Fourier轉換公式:
### Fourier轉換:
$$F(u,v) = \sum_{x=0}^{m-1} \sum_{y=0}^{n-1} f(x,y)e^{-j2\pi(ux/m + vy/n)} $$ <br>
### 反Fourier轉換:
$$f(x,y) = \frac{1}{mn} \sum_{u=0}^{m-1} \sum_{v=0}^{n-1} F(u,v)e^{j2\pi(ux/m + vy/n)}$$

## 濾波器:
### 理想低通濾波器:
  $$
  H(u,v) =
  \begin{cases}
  1,  & \text{if $D(u,v) \le D_0$} \\
  0, & \text{if $D(u,v) \gt D_0$}
  \end{cases}
  $$<br>

### 巴特沃斯低通濾波器:
  $$
  H(u,v) = \frac{1}{1 + \left[ D(u,v)/D_0  \right]^{2n} }
  $$<br>

### 高斯低通濾波器:
  $$
  H(u,v) = e^{-D^2(u,v)/2D_{0}^{2}}
  $$<br>
  <br>
  
### 理想高通濾波器:
  $$
  H(u,v) =
  \begin{cases}
  0,  & \text{if $D(u,v) \le D_0$} \\
  1, & \text{if $D(u,v) \gt D_0$}
  \end{cases}
  $$<br>

### 巴特沃斯高通濾波器:
  $$
  H(u,v) = 1 - \frac{1}{1 + \left[ D(u,v)/D_0  \right]^{2n} }
  $$<br>

### 高斯高通濾波器:
  $$
  H(u,v) = 1 - e^{-D^2(u,v)/2D_{0}^{2}}
  $$<br>
  
### 頻率矩形起算的距離:
  $$ D(u,v)= \sqrt{(u - \frac{P}{2})^2 + (v - \frac{Q}{2})^2}　$$

## Full Result
第一Row使用理想濾波器<br>
第二Row使用巴特沃斯濾波器 $n=2$<br>
第三Row使用高斯濾波器<br>
每Col代表不同參數<br>
第一Col $D_0 = 10$,第二Col $D_0 = 50$,第三Col $D_0 = 100$<br>

### 高通濾波(濾波結果與原圖疊加)
![5](https://user-images.githubusercontent.com/49235533/210935655-c08e88ac-bd3f-4ba3-a66c-7318e133de1b.jpg)<br>

### 低通濾波
![5](https://user-images.githubusercontent.com/49235533/210935724-05615d30-43d8-4863-a988-5b59c006003d.jpg)<br>

### Hybrid Image
![5](https://user-images.githubusercontent.com/49235533/210935797-ff75aa64-97b0-47c1-ab0d-fa87aa7bd927.jpg)<br>

其他結果可參考result資料夾內

## excute UI_ReadImage
```C
python read_img_UI_main.py
```

## Result

### 低通濾波
$D_0 = 30$,                                                            $D_0 = 150$<br>
![ideal1](https://user-images.githubusercontent.com/49235533/214922513-17da2639-b24b-4c2e-aee7-5ab8464ed388.JPG)

![ba_2](https://user-images.githubusercontent.com/49235533/214922557-4d9239ba-4f18-4ec2-8814-b17f6dbb1338.JPG)

![ba_3](https://user-images.githubusercontent.com/49235533/214922573-10af3bc1-67d9-4ea1-8027-75eebc12d210.JPG)

![ba_5](https://user-images.githubusercontent.com/49235533/214922582-ba7bc8c8-7d29-42b6-a29c-85f249bb4262.JPG)

![ba_6](https://user-images.githubusercontent.com/49235533/214922589-4d6184fc-b709-40db-a79d-91707215f9be.JPG)

![ga_1](https://user-images.githubusercontent.com/49235533/214922602-11a8a57d-6194-4329-b1f8-c96d44fb24f2.JPG)

### 高通濾波(濾波結果與原圖疊加)
![ideal_1](https://user-images.githubusercontent.com/49235533/214922625-d6259109-1e3d-4f0b-a921-800e29ba32de.JPG)

![ba_2 5](https://user-images.githubusercontent.com/49235533/214922635-55f5aa47-2d40-4a19-9fb6-a191a6960ab0.JPG)

![ba_3 5](https://user-images.githubusercontent.com/49235533/214922644-0f3a2e7b-5ada-41b7-a98d-59581455919b.JPG)

![ba_5 5](https://user-images.githubusercontent.com/49235533/214922660-2f18a028-ccc8-421d-9750-ea94b35388f5.JPG)

![ba_6 5](https://user-images.githubusercontent.com/49235533/214922677-12cfde05-bcba-438b-83cc-ebc1d6cd0c49.JPG)

![ga_2](https://user-images.githubusercontent.com/49235533/214922687-a742bf63-955b-4f16-b246-d1cc10c27e58.JPG)












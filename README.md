# Hybrid-Image-Image-filter

Hybrid Image & 不同頻率域濾波器不同參數之比較 <br>
## Result (Hybrid Image)
每Col代表不同濾波器
第一Col 使用理想濾波器,第二Col 使用巴特沃斯濾波器 $n=2$,第三Col 使用高斯濾波器<br>
高通濾波參數 $d_0 = 25$, 低通濾波參數 $d_0 = 10$<br>
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
$$F(u,v) = \sum_{x=0}^{m-1} \sum_{y=0}^{n-1} f(x,y)e^{-j2\pi(\frac{u x}{m} + \frac{v y}{n})} $$ <br>
### 反Fourier轉換:
$$f(x,y) = \frac{1}{mn} \sum_{u=0}^{m-1} \sum_{v=0}^{n-1} F(u,v)e^{-j2\pi(\frac{u x}{m} + \frac{v y}{n})}$$

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

$$ D(u,v)= \sqrt{(u - \frac{P}{2})^2 + (v - \frac{Q}{2})^2}　$$

## Full Result
第一Row使用理想濾波器<br>
第二Row使用巴特沃斯濾波器 $n=2$<br>
第三Row使用高斯濾波器<br>
每Col代表不同參數<br>
第一Col $d_0 = 10$,第二Col $d_0 = 50$,第三Col $d_0 = 100$<br>

### 高通濾波(濾波結果與原圖疊加)
![5](https://user-images.githubusercontent.com/49235533/210935655-c08e88ac-bd3f-4ba3-a66c-7318e133de1b.jpg)<br>

### 低通濾波
![5](https://user-images.githubusercontent.com/49235533/210935724-05615d30-43d8-4863-a988-5b59c006003d.jpg)<br>

### Hybrid Image
![5](https://user-images.githubusercontent.com/49235533/210935797-ff75aa64-97b0-47c1-ab0d-fa87aa7bd927.jpg)<br>

其他結果可參考result資料夾內


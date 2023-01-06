# Hybrid-Image-Image-filter

Hybrid Image & 不同頻率域濾波器不同參數之比較 <br>
## Result (Hybrid Image)
每Col代表不同濾波器
第一Col 使用理想濾波器
第二Col 使用巴特沃斯高通濾波器 (n=2)
第二Col 使用高斯濾波器
高通濾波參數 d_0a = 25, 低通濾波參數 = 10
![2](https://user-images.githubusercontent.com/49235533/210935900-ca72b6ac-7a74-440b-8048-0e5f46d3d756.jpg)

## Install requirements
```C
pip install -r requirements.txt
```

## Exeucte
```C
python main.py
```

## Full Result
### 經高通濾波過濾後的圖 
每Row代表不同高通濾波器
第一Row使用理想高通濾波器
第二Row使用巴特沃斯高通濾波器 (n=2)
第三Row使用高斯高通濾波器
每Col代表不同參數
第一Col d_0 = 10
第二Col d_0 = 50
第二Col d_0 = 100

![0](https://user-images.githubusercontent.com/49235533/210935622-b9500371-4090-46cb-ba0e-757b31d141b4.jpg)<br>
![1](https://user-images.githubusercontent.com/49235533/210935632-10380e6d-6d00-43b9-9035-3202fa5f3aa7.jpg)<br>
![2](https://user-images.githubusercontent.com/49235533/210935641-85a4003c-14dc-4be9-9305-d3e419238cf0.jpg)<br>
![3](https://user-images.githubusercontent.com/49235533/210935647-4553a447-eaef-4469-af81-2c6580925e26.jpg)<br>
![4](https://user-images.githubusercontent.com/49235533/210935650-f508c73f-ccab-41f9-b1a7-e9879efaf8c1.jpg)<br>
![5](https://user-images.githubusercontent.com/49235533/210935655-c08e88ac-bd3f-4ba3-a66c-7318e133de1b.jpg)<br>
![6](https://user-images.githubusercontent.com/49235533/210935667-9d698f64-e9b1-4a84-96d5-52cf86849011.jpg)<br>
![7](https://user-images.githubusercontent.com/49235533/210935671-e47b04c9-c036-4bb0-83e7-aecd859d3bc1.jpg)<br>
![8](https://user-images.githubusercontent.com/49235533/210935678-9c041d44-02e3-4d3b-9670-b6beeea0cba8.jpg)

### 經低通濾波過濾後的圖
每Row代表不同低通濾波器
第一Row使用理想低通濾波器
第二Row使用巴特沃斯低通濾波器 (n=2)
第三Row使用高斯低通濾波器
每Col代表不同參數
第一Col d_0 = 10
第二Col d_0 = 50
第二Col d_0 = 100
![0](https://user-images.githubusercontent.com/49235533/210935698-469e483a-7a55-463b-8e65-09ae2bee7553.jpg)<br>
![1](https://user-images.githubusercontent.com/49235533/210935709-cae8e518-287b-48ab-9070-b7cc35e9f95b.jpg)<br>
![2](https://user-images.githubusercontent.com/49235533/210935713-54c0b08f-ffa1-47e2-b8ee-cf245240070a.jpg)<br>
![3](https://user-images.githubusercontent.com/49235533/210935718-db21906f-fdde-4607-90e3-79b3e9ec50d8.jpg)<br>
![4](https://user-images.githubusercontent.com/49235533/210935722-d790e7d5-24ee-4caa-bbc6-217cd14d5f9f.jpg)<br>
![5](https://user-images.githubusercontent.com/49235533/210935724-05615d30-43d8-4863-a988-5b59c006003d.jpg)<br>
![6](https://user-images.githubusercontent.com/49235533/210935728-0de18aca-e8e9-46aa-92b9-7b71c4e2b9c6.jpg)<br>
![7](https://user-images.githubusercontent.com/49235533/210935735-325f6b04-e9aa-432e-978e-f29ab60f21bc.jpg)<br>
![8](https://user-images.githubusercontent.com/49235533/210935737-c6f806dd-b9f2-485a-9efb-d3d62e1cb460.jpg)

### Hybrid Image
每Col代表不同參數
第一Col d_0 = 10
第二Col d_0 = 50
第二Col d_0 = 100
![0](https://user-images.githubusercontent.com/49235533/210935768-0d497098-0b16-4f43-ae07-a00e944d1f15.jpg)<br>
![1](https://user-images.githubusercontent.com/49235533/210935779-5e249bf0-8982-4006-a66c-0b1e03aa16b4.jpg)<br>
![2](https://user-images.githubusercontent.com/49235533/210935785-c1e04ab5-74f2-4a1e-85df-c8f0d0621b3c.jpg)<br>
![3](https://user-images.githubusercontent.com/49235533/210935790-a41734e3-aba6-4fc0-aa33-644693a7190e.jpg)<br>
![4](https://user-images.githubusercontent.com/49235533/210935794-79b13ff0-156b-41d2-82d5-0cae7e8e5f5e.jpg)<br>
![5](https://user-images.githubusercontent.com/49235533/210935797-ff75aa64-97b0-47c1-ab0d-fa87aa7bd927.jpg)<br>
![6](https://user-images.githubusercontent.com/49235533/210935803-0b804f7d-b9b7-4889-8c18-9f0b34cd47f6.jpg)<br>
![7](https://user-images.githubusercontent.com/49235533/210935806-12cc9f57-8776-4ba1-b6c0-482c457a28f0.jpg)<br>
![8](https://user-images.githubusercontent.com/49235533/210935832-28600b16-b02e-43d6-b8cf-0389f4d33678.jpg)

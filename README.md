<h1 align="center">E-104 TAARRUZ SİLAHI</h1>

## **PROJE**

### 1. Türkçe 
   - Gelişen dünyada askeri güç çok önemli bir noktaya gelmiştir. Ve bazen ülkeler askeri güçlerini kullanarak dünyaya yön vermeye çalışırlar.
   Bu istenmeyen sonuçlara yol açar ve çatışma kaçınılmaz hale gelir. Bu durumlarda da askeri güç ön plana çıkar.
   Yoğun çatışma alanında askerlerin kafasını dahi kaldıramadığı anlar olur. Ve bu savaş kaderinin değiştiği anlara neden olabilir.   
   Böyle durumlarda __E-104 Taarruz Silahi__ ön plana çıkmaktadır.
   - Silahın en büyük avantajı insana ihtiyaç duymadan, düşmanı tespit edip ateş açmasıdır. Bu durum savaş sahasında size büyük bir avantaj sağlar.
   Silah otomatik olarak __Tank ve Helikopter__'leri algılayarak silahın namlusunu belirlediği hedefe doğru çevirir. Algoritmamız da belirlediğimiz          şartlar sağlanırsa da silah atışa başlar
   - Silahın modüler olması istenildiği zaman __Taaruz Helikopterlerine__ istenildiği zamanda __Kara Kuvvetleri Araçlarına__ takılarak savaş sahasında 
   avantaj sağlar.
### 2. English 
   - Military power has come to a very important point in the developing world. And sometimes countries try to steer the world by using their military 
   power.
   This leads to undesirable consequences and conflict becomes inevitable. In these situations, military power comes to the fore.
   In the field of intense conflict, there are moments when the soldiers cannot even raise their heads. And this war can cause moments when your destiny 
   changes.
   In such cases, the __E-104 Assault Weapon__ comes to the fore.
   - The biggest advantage of the gun is that it detects the enemy and opens fire without the need for people. This gives you a huge advantage on the 
   battlefield.
   The gun automatically detects __Tank and Helicopter__ and turns the gun's barrel towards the target it has determined. Our algorithm also determined
   Even if the conditions are met, the gun starts firing.
   - When the weapon is required to be modular, it can be mounted on __Land Forces Vehicles__ and  __Attack helicopters__
   This gives you an advantage on the battlefield.
   
   
## **ALGORİTMA**   
### 1. Türkçe 
- Algoritma Python programlama dili ile YOLOv5 algoritmasını kullanarak. Arduino ve Python seri haberleşmesini kullanır.
- Algortma 180 derecelik servo açısını işlenen resimin x ve y pikseline bölerek her bir piksel için servoyu kaç derece döndermemiz
gerektiğini hesaplar. Bunları da Arduino mikrodenetleyicisine göndererek servonun hareketini sağlar.
- Algoritma birden fazla nesne algılaması yaparsa aralarından en yüksek doğruluk oranına sahip olan nesneye yönelim yapmaktadır.
![Ekran Görüntüsü - 2022-08-22 15-13-27](https://user-images.githubusercontent.com/84287815/186099152-cd16efff-25fc-4272-bc18-35fc6d03d313.png)


### 2. English 
- Algorithm using the YOLOv5 algorithm with the Python programming language. Arduino and Python use serial communication.
- The algorithm divides the x and y pixels of the generated image by the 180 degree servo angle and calculates how many degrees we need to rotate 
   the servo for each pixel. By sending them to the Arduino microcontroller, it provides the movement of the servo.
- If the algorithm detects more than one object, it tends to the object with the highest accuracy rate.

### 3. TEST

![IMG_20220823_172939](https://user-images.githubusercontent.com/84287815/186186527-806dafbd-ea7c-43d7-a78e-60abcfb4547b.jpg)

![Ekran Görüntüsü - 2022-08-23 17-30-08](https://user-images.githubusercontent.com/84287815/186186548-a3e0de9e-b11c-4827-bd8a-733640046dba.png)

## **YOLOV5**

1. ### **YOLO nedir ? // What is YOLO?**
   - #### Türkçe
     - **YOLO konvolüsyonel sinir ağları kullanarak nesne tespiti yapan bir algoritmadır. Açılımı ''You Only Look Once'' demektir.**   
   - #### English
     - **YOLO (“You Look Only Once”) is an efficient real-time object recognition algorithm.**   
2. ### **YOLO nasıl kullanılır ? // How use YOLO?**
   ```Python
   python3 tank_detect.py --source  0              # webcam
                                    img.jpg        # image
                                    vid.mp4        # video
   
   
   ```




> #### **Eğitilen modelin algılama performansı // YoloV5 detection performance of the custom model**


![Tank-Heli](https://user-images.githubusercontent.com/84287815/185233314-82e4ed12-323a-4ffb-8ee8-792d16db133f.png)







#### Helikopter 1 // Helicopter 1

![helikopter](https://user-images.githubusercontent.com/84287815/185920263-c77cf206-adca-44c3-9d8b-53b3178e4cf4.jpg)

#### Helikopter 2 // Helicopter 2

![helikopter1](https://user-images.githubusercontent.com/84287815/185920284-c2c39996-4009-4142-8a9e-5f2119d105bc.jpg)

#### Helikopter 3 // Helicopter 3

![helikopter2](https://user-images.githubusercontent.com/84287815/185920302-f4713dd2-b717-427a-a54a-c36382be8c1b.jpg)

#### Tank 1 

![tank](https://user-images.githubusercontent.com/84287815/185920329-f2c5b96c-14b6-4f6a-b16b-6c760faddbeb.jpg)

#### Tank 2

![tank1](https://user-images.githubusercontent.com/84287815/185920347-1e324746-9b45-4a9e-89d6-8e7d7c94e741.jpg)

#### Tank 3

![tank2](https://user-images.githubusercontent.com/84287815/185920386-95390cdb-e8bb-493e-b33b-4cd8e55d7ded.jpg)

#### Tank 4

![tank3](https://user-images.githubusercontent.com/84287815/185920398-ba26d6f9-197e-440d-b871-0a17bc979698.jpg)

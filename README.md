# 공사 현장 안전 점검 자동화 프로그램 

### INTRODUCTION
<li>공사 현장에서 안전모를 착용하고 있는지 탐지할 수 있는 프로그램입니다.</li>
<li>웹 페이지에 사진을 업로드하면 Detection Model의 결과로 얻은 안전모, 모자, 머리 등의 바운딩 박스가 표시된 이미지를 볼 수 있습니다.

<br>

### DATA
<li><strong>안전모를 착용한 이미지 데이터 people wearing hard hat images from:</strong><br>
kaggle hard-hat-detection data : https://www.kaggle.com/datasets/andrewmvd/hard-hat-detection</li><br>
<li><strong>모자를 착용한 이미지 데이터 for people wearing hat images:</strong><br>
kaggle cricekt-football-baseball : https://www.kaggle.com/datasets/imbikramsaha/cricket-football-baseball<br>
... and images from google</li>

<br>

### Detection Network
YOLO v8 from ultralytics: https://github.com/ultralytics/ultralytics

<br>

### Usage
```
git clone "https://github.com/ghkim1632/helmet_detection.git"
```

"web/main.py"를 실행시키고 웹 페이지를 엽니다. 파일을 누르고 테스트 이미지를 저장합니다. 조금 기다리면 모델 탐지 결과 이미지를 웹 페이지로 볼 수 있습니다.<br>
웹 페이지에서 테스트한 결과 이미지는 "web/statics/image"에 저장됩니다.</p>

Load "web/main.py". Upload the image file you want to test. If you wait for a second, you can see the result image of the detection model.<br>
Result images(images with bounding boxes) that you tested on the web will be stored in "web/statics/image".
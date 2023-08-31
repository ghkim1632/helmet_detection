import glob
import shutil

from flask import Flask, request, render_template
from ultralytics import YOLO

model = YOLO("./model/best_hat_50.pt")

app = Flask( __name__  )

@app.route('/')
def index():
    return render_template('lr_main.html')

@app.route('/fsend', methods=['POST'])
def fsend():
    file = request.files['image']
    print('파일명:', file.filename)
    sName = './downimage/'+file.filename
    file.save(sName)

    if not file:
        return '<h1>파일이 없습니다.</h1>'

    results = model.predict(sName, conf=0.05, iou=0.65, max_det=300, save=True)
    path = sorted(glob.glob("./runs/detect/*"))[-1] + "/" + file.filename
    move = shutil.copy(path, './static/image/result.jpg')

    for result in results:
        label = result.boxes.cls
    warning = ""
    if label.any() == False:
        warning = "안전합니다."
    else:
        warning = "안전모를 착용해주세요"
    return render_template('predict.html', warning=warning)

if __name__ == '__main__':
    app.run( host='0.0.0.0', port =4500, debug=True)
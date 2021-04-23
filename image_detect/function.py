from tensorflow.keras.models import load_model
import cv2
import numpy as np
def readModel(model_path):
    model = load_model(model_path)
    return model
className=["新型冠状肺炎","未见感染","普通肺炎"]
# model.summary()
def processing(img_path):
    data=[]
    for path in img_path:
        image = cv2.imread(path)
        # print(image)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (224, 224))
        data.append(image)
    data = np.array(data)
    return data
def predictImgset(model,predict_dir):
    data = processing(predict_dir)
    pre_y = model.predict(data)
    print(pre_y)
    predIdxs = np.argmax(pre_y, axis=1)
    result = []
    for idxs in predIdxs:
        result.append(className[idxs])
    # print(result)
    return result
predict_dir = ["../imageUnit/078.jpeg","../imageUnit/094.png"] #预测的数组
save_path = r"./model200.h5"
model = readModel(save_path)
result = predictImgset(model,predict_dir)
print(result)
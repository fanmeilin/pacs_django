from tensorflow.keras.models import load_model
import cv2
import numpy as np
from imutils import paths
#读取模型
def readModel(model_path):
    model = load_model(model_path)
    return model
# model.summary()
#图像预处理
def processing(img_path):
    data=[]
    for path in img_path:
        image = cv2.imread(path)
        # print(image)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (224, 224))
        data.append(image)
        # print(image)
    data = np.array(data)
    return data
#模型预测结果写入
def predictImgset(model,predict_dir):
    className = ["新型冠状肺炎", "未见感染", "普通肺炎"]
    data = processing(predict_dir)
    pre_y = model.predict(data)
    # print(pre_y)
    predIdxs = np.argmax(pre_y, axis=1)
    result = []
    i=1#
    for idxs in predIdxs:
        if(idxs==2): print(i,predict_dir[i-1]) #
        i = i+1 #
        result.append(className[idxs])
    # print(result)
    return result
# imagepath = list(paths.list_images("../static/imageUnit"))
# print(imagepath)
# save_path = r"./model200.h5"
# model = readModel(save_path)
# result = predictImgset(model,imagepath)
# print(result)
from django.db import models
import numpy as np
import sys
import tensorflow.compat.v1 as tf
from tensorflow.keras.models import load_model
from PIL import Image
import io,base64

# Create your models here.
graph=tf.get_default_graph()
class Photo(models.Model):
    image=models.ImageField(upload_to="photos")

    IMAGE_SIZE=128 #画像サイズ
    MODEL_PATH="./usbai/ml_models/my_model_epoch45.h5"
    imagename=['Micro-USB-TypeB-2.0', 'Micro-USB-TypeB-3.0', 'Mini-USB-TypeB', 'USB-TypeA', 'USB-TypeC'] #あとで入れろ
    image_len=len(imagename)

    def predict(self):
        model=None
        global graph#毎回同じモデルのセッションに投入して推論可能にする。
        with graph.as_default():
            model=load_model(self.MODEL_PATH)

            img_data=self.image.read()
            img_bin=io.BytesIO(img_data)

            image=Image.open(img_bin)
            image=image.convert("RGB")
            image=image.resize((self.IMAGE_SIZE,self.IMAGE_SIZE))
            data=np.asarray(image)/255.0
            X=[]
            X.append(data)
            X=np.array(X)

            result=model.predict([X])[0]
            predicted=result.argmax()
            percentage=int(result[predicted]*100)

            return self.imagename[predicted],percentage
        
    def image_src(self):
        with self.image.open() as img:
            base64_img=base64.b64encode(img.read()).decode()

            return "data:"+img.file.content_type+";base64,"+base64_img

import keras.models
from flask import Flask, request, render_template

from keras.models import load_model
import numpy as np
import base64
import cv2
from sklearn.preprocessing import StandardScaler

app =app = Flask(__name__, template_folder='templates')
model = keras.models.load_model('finalmodel.h5', compile=True)


@app.route('/')
def index():
    return render_template("index.html")

standard_to = StandardScaler()
@app.route('/predict', methods=["POST"])


def get_image():
    encoded_data = request.form['canvasing'].split(',')[1]
    nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    print(img.shape)

    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_image = cv2.resize(gray_image, (28, 28), interpolation=cv2.INTER_LINEAR)
    gray_image = gray_image / 255.0

    gray_image = np.expand_dims(gray_image, axis=-1)
    img = np.expand_dims(gray_image, axis=0)

    print('Image received: {}'.format(img.shape))
    prediction = model.predict(img)
    print("Prediction : ",prediction)


    return render_template("index.html", value=np.argmax(prediction))



if __name__ == '__main__':
    app.run(debug=True)
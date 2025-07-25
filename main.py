import cv2
import os
import numpy as np
from tensorflow.keras.models import load_model
model = load_model('.venv/my_model.h5')

mode=  ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']



cap= cv2.VideoCapture(0)
ret, frame = cap.read()
while ret:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (48, 48))

    # Normalize and reshape input
    input_image = resized.astype('float32')
    input_image = np.expand_dims(input_image, axis=-1)
    input_image = np.expand_dims(input_image, axis=0)

    prediction = model.predict(input_image)                 # Output: probabilities
    predicted_class = np.argmax(prediction)

    # Show the frame
    print(mode[predicted_class])
    text= mode[predicted_class]
    cv2.putText(frame, text, org=(20, 20), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(0, 0, 255), thickness=2)
    cv2.imshow('frame', frame)


    # Exit on key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break




cap.release()
cv2.destroyAllWindows()



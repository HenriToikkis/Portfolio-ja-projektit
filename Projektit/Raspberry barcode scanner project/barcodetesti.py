import cv2
import pyzbar.pyzbar as pyzbar


cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

while True:
    a, frame = cap.read()

    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        cv2.putText(frame, str(obj.data.decode('utf-8')), (220, 80), font, 2,
                    (0, 255, 0), 3)
       


    cv2.imshow("Bar code raspberry", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break




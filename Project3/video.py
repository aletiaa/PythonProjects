import cv2

# Завантаження класифікатора облич Haar
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Відкриття відеопотоку
video_capture = cv2.VideoCapture('video1.mp4')  # або вказати шлях до відеофайлу, наприклад, 'video.mp4'

while True:
    # Захоплення кадру з відеопотоку
    ret, frame = video_capture.read()

    # Конвертація кадру до відтінків сірого
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Розпізнавання облич
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=6, minSize=(30, 30))

    # Підкреслення облич на відео
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Відображення результату
    cv2.imshow('Video', frame)

    # Вихід з циклу при натисканні клавіші 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Закриття відеопотоку та вікна
video_capture.release()
cv2.destroyAllWindows()

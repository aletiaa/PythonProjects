import cv2
import imutils

# Завантаження зображення
image_path = 'image.png'
image = cv2.imread(image_path)

# Покращення якості зображення
# Застосування фільтра Гаусса для зменшення шуму та плавнішого зображення
image = cv2.GaussianBlur(image, (5, 5), 0)
# Підвищення контрастності зображення
image = cv2.convertScaleAbs(image, alpha=1.2, beta=20)
# Збільшення роздільної здатності зображення
image = imutils.resize(image, width=image.shape[1]*2, height=image.shape[0]*2)

# Конвертація до відтінків сірого для використання в класифікаторі
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Ініціалізація класифікатора Haar для розпізнавання облич
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Знаходження облич на зображенні зі зменшеними параметрами шкали та збільшеною кількістю сусідів
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.05, minNeighbors=8, minSize=(30, 30))

# Відображення областей, на яких розташовані обличчя
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Відображення результату
cv2.imshow('Face Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

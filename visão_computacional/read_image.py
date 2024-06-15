import cv2

img = cv2.imread("tucano.jpeg")

cv2.imshow("Imagem de Exibicao",img)

print(img)


cv2.waitKey(0)

gray_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

cv2.imshow("escala cinza",gray_img)


import cv2
import numpy as np

def matchTemplate(img1,img2,tolerancia = 0.6):
    img_rgb = cv2.imread(img1)
    patch = cv2.imread(img2)

    # Tamaño de la imagen 1.jpg
    w, h = patch.shape[:-1]

    # Función que sirve para detectar si una imagen está contenida en otra
    res = cv2.matchTemplate(img_rgb, patch, cv2.TM_CCOEFF_NORMED)


    # Si está dentro del umbral, crear un cuadrado sobre la imagen contenida en la imagen Todo
    threshold = tolerancia
    loc = np.where( res >= threshold)
    puntoMedio = (0,0)
    if(list(zip(*loc[::-1]))):
        max_loc = list(zip(*loc[::-1]))[0]
        #min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)


    # Guardar el resultado
        puntoMedio = (int((top_left[0]+bottom_right[0])/2),int((top_left[1]+bottom_right[1])/2))
        #cv2.rectangle(img_rgb,top_left, bottom_right, (0,0,255), 1)
        #cv2.rectangle(img_rgb, puntoMedio, (puntoMedio[0]+10,puntoMedio[1]+10),(0,100,255), 5)
        #cv2.imwrite('result.png', img_rgb)

    return puntoMedio

def screenShoot():
    screen_shot = pyautogui.screenshot(region=(1300,750, 0, 0))
    screen_shot.save('screen.jpg')


if __name__ == "__main__":
    img1 = 'Imagenes\\mapa.jpg'
    img2 = 'Imagenes\\1.jpg'
    
    print(matchTemplate(img1,img2))


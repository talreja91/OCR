import cv2

def funcBrightContrast(bright=0):
    bright = cv2.getTrackbarPos('bright', 'Talreja91')
    contrast = cv2.getTrackbarPos('contrast', 'Talreja91')

    effect = apply_brightness_contrast(img,bright,contrast)
    imSE = cv2.resize(effect, (960, 540))
    cv2.imshow('Effect', imSE)
    

def apply_brightness_contrast(input_img, brightness = 255, contrast = 127):
    brightness = map(brightness, 0, 510, -255, 255)
    contrast = map(contrast, 0, 254, -127, 127)

    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            highlight = 255
        else:
            shadow = 0
            highlight = 255 + brightness
        alpha_b = (highlight - shadow)/255
        gamma_b = shadow

        buf = cv2.addWeighted(input_img, alpha_b, input_img, 0, gamma_b)
    else:
        buf = input_img.copy()

    if contrast != 0:
        f = float(131 * (contrast + 127)) / (127 * (131 - contrast))
        alpha_c = f
        gamma_c = 127*(1-f)

        buf = cv2.addWeighted(buf, alpha_c, buf, 0, gamma_c)

    cv2.putText(buf,'B:{},C:{}'.format(brightness,contrast),(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    return buf

def map(x, in_min, in_max, out_min, out_max):
    return int((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)

if __name__ == '__main__':

    original = cv2.imread("./diwali.png", 1)
    img = original.copy()

    cv2.namedWindow('Talreja91',1)

    bright = 255
    contrast = 127

    #Brightness value range -255 to 255
    #Contrast value range -127 to 127

    cv2.createTrackbar('bright', 'Talreja91', bright, 2*255, funcBrightContrast)
    cv2.createTrackbar('contrast', 'Talreja91', contrast, 2*127, funcBrightContrast)
    funcBrightContrast(0)
    imS = cv2.resize(img, (960, 540))
    cv2.imshow('Talreja91', imS)


cv2.waitKey(0)
import cv2
import time
import sys
 
def main(args):
 
    camera_port = 0
  
    nFrames = 30
  
    camera = cv2.VideoCapture(camera_port)
     
    file = "C:\\Users\\irisg\\OneDrive\\Área de Trabalho\\RAS-Teste"
         
    print ("Digite <ESC> para sair / <s> para Salvar")  
     
    emLoop= True
      
    while(emLoop):
     
        retval, img = camera.read()
        cv2.imshow('Foto',img)
     
        k = cv2.waitKey(100)
     
        if k == 27:
            emLoop= False
         
        elif k == ord('s'):
            cv2.imwrite(file,img)
            emLoop= False
     
    cv2.destroyAllWindows()
    camera.release()
    return 0
 
if __name__ == '__main__':
    sys.exit(main(sys.argv))
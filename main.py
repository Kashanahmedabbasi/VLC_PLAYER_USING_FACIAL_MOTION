import vlc
from facemesh import FaceMeshDetector
import cv2
import time

def main():
    cap = cv2.VideoCapture(0)
    pTime=0
    # media_player = vlc.MediaPlayer()
    # media = vlc.Media("v.MP4")
    # media_player.set_media(media)
    detector = FaceMeshDetector()
    # media_player.play()
    while True:
        success , img = cap.read()
        img,faces,res,lf,rf,le,re,fdy,lpy = detector.findFaceMesh(img,draw=False)
        if len(faces)!=0:
            if fdy-lpy > 65:
                # media_player.set_rate(media_player.set_rate(2))
                print('face up')
                cv2.putText(img,"Face Up",(140,70),cv2.FONT_HERSHEY_PLAIN,2,(0,255,212,0),3)
            elif fdy-lpy < 40:
                # media_player.set_rate(media_player.set_rate(0.5))
                print('face down')  
                cv2.putText(img,"Face Down",(140,70),cv2.FONT_HERSHEY_PLAIN,2,(0,255,212,0),3)  
            elif re-lf < 10:
                # value = media_player.get_time()
                # media_player.set_time(value+10000)
                print('video forward')
                cv2.putText(img,"Face Right",(140,70),cv2.FONT_HERSHEY_PLAIN,2,(0,255,212,0),3) 
            elif rf-le < 10:
                # value = media_player.get_time()
                # media_player.set_time(value-10000)
                print('video backward')
                cv2.putText(img,"Face Left",(140,70),cv2.FONT_HERSHEY_PLAIN,2,(0,255,212,0),3) 
            # else:
                # media_player.set_rate(media_player.set_rate(1))
                # media_player.play()
        cTime = time.time()
        fps = 1 / (cTime -  pTime)
        pTime=cTime
        cv2.putText(img,f'FPS {str(int(fps))}',(10,70),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),2)
        cv2.imshow('frame',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            # media_player.stop()
            cv2.destroyAllWindows()
            
            break
    

if __name__=="__main__":
    main()
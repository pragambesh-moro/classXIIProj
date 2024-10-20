from ffpyplayer.player import MediaPlayer
import cv2

def play_video_with_audio(video_path):
    def get_frame_and_audio():
        frame, val = player.get_frame()
        if val != 'eof' and frame is not None:
            image, pts = frame
            return (image, val)
        else:
            return (None, val)
    
    video = cv2.VideoCapture(video_path)
    player = MediaPlayer(video_path)
    
    while True:
        ret, frame = video.read()
        if not ret:
            break
        
        image, val = get_frame_and_audio()
        if image is not None:
            cv2.imshow('Video', frame)
        
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    
    video.release()
    cv2.destroyAllWindows()


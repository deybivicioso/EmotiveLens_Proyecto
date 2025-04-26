import cv2
import mediapipe as mp
import numpy as np
from deepface import DeepFace
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

# Obtener la carpeta principal del proyecto
project_root = Path(__file__).resolve().parent.parent

EMOJIS = {
    "angry": "😡",
    "disgust": "🤢",
    "fear": "😨",
    "happy": "😀",
    "sad": "😟",
    "suprise": "😮",
    "neutral": "😐"
}

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()


mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection()


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

def escaneo():

    detected_emotions = []
    cap= cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break


        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        face_results = face_detection.process(rgb_frame)
        face_mesh_results = face_mesh.process(rgb_frame)

        if face_results.detections:
            for detection in face_results.detections:
                bboxC = detection.location_data.relative_bounding_box
                h, w, _ = frame.shape
                x, y, w_box, h_box = int(bboxC.xmin * w), int(bboxC.ymin * h), int(bboxC.width * w), int(bboxC.height * h)


                face_crop = frame[y:y+ h_box, x:x+ w_box]


                if face_crop.shape[0] > 0 and face_crop.shape[1] > 0:
                    try: 

                        emotion_result = DeepFace.analyze(face_crop, actions=['emotion'], enforce_detection=False)
                        emotion = emotion_result[0]['dominant_emotion']
                        detected_emotions.append(emotion)
                        emoji_face = EMOJIS.get(emotion, "❓")


                        img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                        draw = ImageDraw.Draw(img)


                        try: 
                            font = ImageFont.truetype("seguiemj.ttf", 50)
                            text_font = ImageFont.truetype("arial.ttf", 10)
                        except IOError:
                            font = ImageFont.load_default()
                            text_font = ImageFont.load_default()

                        h, w, _ = frame.shape
                        emoji_x, emoji_y = w - 100, h - 80
                        draw.text((emoji_x, emoji_y), emoji_face, font=font, fill=(255, 255, 255))
                        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

                        cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)


                    except Exception as e:
                        print("Error en el analisis: ", e)

    
        if face_mesh_results.multi_face_landmarks: 
            for face_landmarks in face_mesh_results.multi_face_landmarks:
                mp_drawing.draw_landmarks(
                    frame, face_landmarks, mp_face_mesh.FACEMESH_TESSELATION,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=1 )
                )

    
        cv2.namedWindow("Scanner Facial - Emociones", cv2.WINDOW_NORMAL)
        cv2.imshow("Scanner Facial - Emociones", frame)

        key = cv2.waitKey(1)
        if key == 13:  # Enter
            break

    cap.release()
    cv2.destroyAllWindows()

    return detected_emotions



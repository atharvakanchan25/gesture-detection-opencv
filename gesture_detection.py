import cv2
import mediapipe as mp

# Initialize MediaPipe Hands and Pose modules
mp_hands = mp.solutions.hands
mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Open webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    hand_results = hands.process(rgb_frame)
    pose_results = pose.process(rgb_frame)
    
    if hand_results.multi_hand_landmarks:
        for hand_landmarks in hand_results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Extract finger tip landmarks (index, middle, ring, pinky, thumb)
            finger_tips = [hand_landmarks.landmark[i] for i in [8, 12, 16, 20, 4]]
            palm_base = hand_landmarks.landmark[0]
            
            # Count raised fingers more accurately using y-coordinate thresholding
            raised_fingers = sum([1 for tip in finger_tips if tip.y < palm_base.y - 0.02])
            
            # Display count on screen
            cv2.putText(frame, f'Fingers: {raised_fingers}', (50, 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    
    if pose_results.pose_landmarks:
        mp_draw.draw_landmarks(frame, pose_results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        
        # Example: Detect if arms are raised (shoulder vs wrist y-coordinates)
        left_shoulder = pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
        left_wrist = pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST]
        
        if left_wrist.y < left_shoulder.y:
            cv2.putText(frame, "Left Arm Raised", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    
    cv2.imshow("Gesture & Finger + Body Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


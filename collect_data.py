import os
import cv2

DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 3
dataset_size = 10

# num_cameras = 5  # Try a range of camera indices, e.g., 0 to 5
# for i in range(num_cameras):
#     cap = cv2.VideoCapture(i)
#     if cap.isOpened():
#         print(f"Camera {i}: Available")
#         cap.release()
#     else:
#         print(f"Camera {i}: Not available")

cap = cv2.VideoCapture(0)
for j in range(number_of_classes):
    if not os.path.exists(os.path.join(DATA_DIR, str(j))):
        os.makedirs(os.path.join(DATA_DIR, str(j)))

    print('Collecting data for class {}'.format(j))

    done = False
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture a frame. Check your camera or driver.")
            break  # Exit the loop if there is no valid frame

        cv2.putText(frame, 'Ready? Press "Q" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
        
        # Check if frame dimensions are valid
        if frame.shape[0] > 0 and frame.shape[1] > 0:
            cv2.imshow('frame', frame)
        else:
            print("Invalid frame dimensions. Skipping display.")
        
        if cv2.waitKey(25) == ord('q'):
            break

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture a frame. Check your camera or driver.")
            break  # Exit the loop if there is no valid frame

        # Check if frame dimensions are valid
        if frame.shape[0] > 0 and frame.shape[1] > 0:
            cv2.imshow('frame', frame)
            cv2.waitKey(25)
            cv2.imwrite(os.path.join(DATA_DIR, str(j), '{}.jpg'.format(counter)), frame)
            counter += 1
        else:
            print("Invalid frame dimensions. Skipping capture.")
            

cap.release()
cv2.destroyAllWindows()

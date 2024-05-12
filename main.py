from eye_tracker import eye_on_mask
from head_pose_estimation import head_pose_points

#from face_detector import get_face_detector
from test import MouthOpeningDetector

def main():
    eye_track = eye_on_mask()
    #detect_face = get_face_detector()
    
    head_pose = head_pose_points()
    
    mouth_open = MouthOpeningDetector()
  
    eye_track.some_method()
    #detect_face.some_method()
    head_pose.some_method()
    mouth_open.some_method()
   
if __name__ == "__main__":
    main()
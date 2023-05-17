
#from sensor_msgs.msg import Image
#from camera_pkg.srv import camera_service, camera_serviceResponse

import rospy
import sys


def callback(msg):

	print str(msg)


#def turn_on(request):
#    global Data
#    global ServiceData

#    ServiceData = str(Data)

#    print ServiceData

#    return  ServiceData

if __name__=="__main__":
	rospy.init_node('camera_service')


	rospy.Subscriber('cv_camera/image_raw', Image, callback)

	#service=rospy.Service('camera_service',camera_service,turn_on)

	rospy.spin()

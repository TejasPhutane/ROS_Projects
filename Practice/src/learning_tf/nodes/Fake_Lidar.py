#!/usr/bin/env python  

from sensor_msgs.msg import LaserScan
from std_msgs.msg import Header
from std_msgs.msg import Float32MultiArray

import rospy    
import tf

def fake_laser():
    rospy.init_node("Laser")
    pub = rospy.Publisher("/fake_laser_scan",LaserScan,queue_size=10)
    br = tf.TransformBroadcaster()
    rate = rospy.Rate(20)
    counter = 0

    while not rospy.is_shutdown():
        br.sendTransform((0.0, 2.0, 0.0),
                        (0.0, 0.0, 0.0, 1.0),
                        rospy.Time.now(),"fake_laser","world")
            
        msg = LaserScan()

            # Header
        msg.header.frame_id = "fake_laser"
        msg.header.stamp.secs = counter/20
        msg.header.stamp.nsecs = 0
        msg.header.seq = counter
            # Angle Data
        msg.angle_increment = 0.0071013928391
        msg.time_increment  = 0.0
        msg.scan_time = 0.0
        msg.angle_max = 3.14159
        msg.angle_min = 0
        msg.angle_increment = 0.0872665 
        msg.range_max=  4
        msg.range_min = 0.1

        msg.intensities = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        # msg.intensities = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        msg.ranges = [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 7.8711838722229, 7.690351486206055, 7.6088032722473145, 7.569084167480469, 7.530155181884766, 7.492002010345459, 7.486484527587891, 7.486984729766846, 7.486840724945068, 7.486151695251465, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 7.974135875701904, 7.91775369644165, 7.884276390075684, 7.860017776489258, 7.860008239746094, 7.8603949546813965, 7.867787837982178, 7.884047985076904, 10.0, 8.448713302612305, 8.25976848602295, 8.079486846923828, 7.992792129516602, 8.047738075256348, 8.031656265258789, 8.051841735839844, 8.145171165466309, 8.093746185302734, 2.21284818649292, 2.123079538345337, 2.0404484272003174, 1.9641064405441284, 1.940171241760254, 1.9199113845825195, 1.90016508102417, 1.8809150457382202, 1.8621439933776855, 1.8438355922698975, 1.8259748220443726, 1.8085482120513916, 1.7915432453155518, 1.7749440670013428, 1.7587381601333618, 1.7429121732711792, 1.733558177947998, 1.7302091121673584, 1.7269604206085205, 1.7238097190856934, 1.7207574844360352, 1.717802882194519, 1.7149447202682495, 1.7121821641921997, 1.7095143795013428, 1.7069411277770996, 1.7044612169265747, 1.7020738124847412, 1.6997795104980469, 1.6975761651992798, 1.6954641342163086, 1.693442463874817, 1.6915112733840942, 1.6896692514419556, 1.6879167556762695, 1.6862523555755615, 1.684675931930542, 1.690114140510559, 1.6966747045516968, 1.7033708095550537, 1.7102088928222656, 1.7171869277954102, 1.7243103981018066, 1.7315804958343506, 1.7390007972717285, 1.7461224794387817, 1.753230094909668, 1.7604851722717285, 1.7678905725479126, 1.7754480838775635, 1.7831604480743408, 1.790732979774475, 1.797169804573059, 1.803744912147522, 10.0, 10.0, 10.0, 2.68894362449646, 2.655111074447632, 2.622248888015747, 2.590320110321045, 2.5759801864624023, 2.565824031829834, 2.555875778198242, 2.5461320877075195, 2.536590576171875, 2.527247667312622, 2.518098831176758, 2.510301113128662, 2.5114731788635254, 2.5127735137939453, 2.5142018795013428, 2.515758752822876, 2.517444372177124, 2.519259452819824, 2.521204710006714, 2.523280382156372, 2.529252767562866, 2.5430350303649902, 2.557096481323242, 2.5714449882507324, 2.586087703704834, 2.6010289192199707, 2.6162772178649902, 2.638169288635254, 2.665337085723877, 2.693206787109375, 3.008178472518921, 2.9940686225891113, 2.980238914489746, 2.9666860103607178, 2.9534034729003906, 2.940387725830078, 2.947422742843628, 2.9823710918426514, 3.0732357501983643, 3.0605340003967285, 3.0933399200439453, 3.204174518585205, 3.1915700435638428, 3.214398145675659, 3.3334643840789795, 3.321000337600708, 3.3469011783599854, 3.3938803672790527, 3.4100494384765625, 3.4212565422058105, 3.471940279006958, 3.524326801300049, 3.5785014629364014, 3.6345551013946533, 3.692580223083496, 3.752683162689209, 3.8149685859680176, 3.8795547485351562, 3.946568250656128, 4.016144275665283, 4.088428497314453, 4.163575172424316, 4.241752624511719, 4.323145866394043, 4.4079508781433105, 4.49638032913208, 4.58866548538208, 4.685061454772949, 4.785839557647705, 4.9810309410095215, 6.307420253753662, 6.303204536437988, 6.293107509613037, 6.269116401672363, 6.245624542236328, 6.222626209259033, 6.200109004974365, 6.156846046447754, 6.076683044433594, 5.760989665985107, 5.7620391845703125, 6.810600280761719, 6.801176071166992, 6.849311828613281, 7.083176612854004, 7.33395528793335, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 9.908082008361816, 9.782733917236328, 9.66099739074707, 9.542728424072266, 9.427790641784668, 9.316055297851562, 9.207392692565918, 9.101693153381348, 8.998838424682617, 8.898727416992188, 8.801259994506836, 8.70633602142334, 8.61386775970459, 8.523770332336426, 8.435956954956055, 8.35035228729248, 8.26688003540039, 8.185470581054688, 8.10605239868164, 8.02856159210205, 7.952934741973877, 7.879114151000977, 7.807041168212891, 7.83494234085083, 7.879341125488281, 7.924647808074951, 7.970883846282959, 8.01806354522705, 8.06622314453125, 8.115372657775879, 8.16553783416748, 8.216744422912598, 8.269018173217773, 8.322381973266602, 8.376866340637207, 8.432496070861816, 8.489299774169922, 8.547307968139648, 8.606553077697754, 8.667064666748047, 8.728874206542969, 8.792020797729492, 8.856536865234375, 8.844961166381836, 8.785860061645508, 8.727978706359863, 8.671292304992676, 8.615769386291504, 8.561379432678223, 8.508099555969238, 8.455904006958008, 8.404762268066406, 8.354657173156738, 8.305562973022461, 8.257455825805664, 8.210312843322754, 8.164115905761719, 8.118843078613281, 8.074474334716797, 8.030989646911621, 7.9883713722229, 7.946602821350098, 7.905664920806885, 7.865541458129883, 7.826215744018555, 7.804713249206543, 7.8372697830200195, 7.7998270988464355, 7.763130187988281, 7.727165222167969, 7.69191837310791, 7.657375812530518, 7.6235246658325195, 7.5903520584106445, 7.557847023010254, 7.525997161865234, 7.4947896003723145, 7.464216709136963, 7.43426513671875, 7.4049248695373535, 7.376184463500977, 7.34803581237793, 7.320470333099365, 7.293476581573486, 7.267046928405762, 7.2411699295043945, 7.215841293334961, 7.191049575805664, 7.166788101196289, 7.14304780960083, 7.1198225021362305, 7.097105026245117, 7.074887275695801, 7.053164005279541, 7.03192663192749, 7.011168479919434, 6.990885257720947, 6.9710693359375, 6.874212741851807, 6.855523586273193, 6.837280750274658, 6.819478988647461, 6.802109241485596, 6.785170555114746, 6.768656253814697, 6.752561092376709, 6.73688268661499, 6.721614837646484, 6.706752300262451, 6.692293643951416, 6.678232192993164, 6.664565086364746, 6.651288986206055, 6.638400077819824, 6.625893592834473, 6.613767147064209, 6.602016925811768, 6.590641498565674, 6.579635143280029, 6.568997383117676, 6.558724880218506, 6.548811912536621, 6.539259910583496, 6.530063629150391, 6.521221160888672, 6.512731552124023, 6.504591941833496, 4.860675811767578, 4.855104446411133, 4.849790573120117, 4.844730854034424, 4.839926719665527, 4.835374355316162, 4.831075191497803, 4.827025890350342, 4.823228359222412, 4.819676876068115, 4.816374778747559, 4.813320636749268, 4.810511112213135, 4.807949066162109, 4.805630207061768, 4.803556442260742, 4.801726341247559, 4.800140380859375, 4.798795223236084, 4.797694683074951, 4.796835899353027, 4.796219348907471, 4.795845031738281, 4.795711994171143, 4.795821189880371, 4.796172618865967, 4.7967658042907715, 4.797600746154785, 4.798677921295166, 4.799997806549072, 4.801560878753662, 4.803368091583252, 4.805418014526367, 4.807712554931641, 4.810251712799072, 4.81303596496582, 4.816068172454834, 4.8193464279174805, 4.822871685028076, 4.826646327972412, 4.830670356750488, 4.8349456787109375, 4.839473247528076, 4.844253063201904, 4.849287509918213, 4.854576587677002, 4.860123634338379, 4.865928649902344, 4.8719940185546875, 4.878320693969727, 4.884909152984619, 4.891763210296631, 4.898885250091553, 4.906275272369385, 4.913933753967285, 4.921867370605469, 4.930074214935303, 4.938559055328369, 4.947321891784668, 4.956367015838623, 4.965696334838867, 4.975310802459717, 4.98521614074707, 4.995412826538086, 5.005904674530029, 5.016693115234375, 5.027781963348389, 5.0391764640808105, 5.050876617431641, 5.062888145446777, 5.0752129554748535, 5.087855339050293, 5.100818634033203, 5.114107131958008, 5.127723217010498, 5.141672611236572, 5.15595817565918, 5.170585632324219, 5.185559272766113, 5.200881004333496, 5.216558456420898, 5.232594966888428, 5.248996734619141, 5.265766620635986, 5.282912731170654, 5.30043888092041, 5.3183512687683105, 5.336653709411621, 5.355354309082031, 5.374458312988281, 5.393971920013428, 5.413902282714844, 5.434255123138428, 5.455038070678711, 5.476257801055908, 5.497920036315918, 5.520035743713379, 5.542610168457031, 5.565651893615723, 5.589168548583984, 5.6131696701049805, 5.637662887573242, 5.662657737731934, 5.688163757324219, 5.714189529418945, 5.740744590759277, 5.767841815948486, 5.795488357543945, 5.823697090148926, 5.852477550506592, 5.881843566894531, 5.911802291870117, 5.942370414733887, 5.973560333251953, 6.00538444519043, 6.037852764129639, 6.070981979370117, 6.104787826538086, 6.139285087585449, 6.174485206604004, 6.210407257080078, 6.247066974639893, 6.284480571746826, 6.322665214538574]
        

        counter +=1
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        fake_laser()
    except rospy.ROSInternalException:
        pass

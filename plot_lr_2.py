import pylab

pylab.figure(figsize=(8,4))
pylab.axes((0.11, 0.13, 0.85, 0.79))

color=['k', 'b', 'g', 'r']

pylab.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9],[0.64237972963790013, 0.37858743286669999, 0.35766205088629999, 0.3454534750587, 0.34706729535549996, 0.34533060306010005, 0.34212127074699994, 0.34193807108389995, 0.34143557025740001, 0.33852787706479992], label='bump', color=color[0], linewidth=2)
pylab.errorbar([0, 1, 2, 3, 4, 5, 6, 7, 8, 9],[0.64237972963790013, 0.37858743286669999, 0.35766205088629999, 0.3454534750587, 0.34706729535549996, 0.34533060306010005, 0.34212127074699994, 0.34193807108389995, 0.34143557025740001, 0.33852787706479992],yerr=[[-0.003805427308899767, -0.002045653566899952, -0.0020051391733000301, -0.00092488868160006676, -0.00058106978439997903, -0.00097704548819993464, -0.00070676643900002833, -0.00097756056070003039, -0.00096826979649994316, -0.00066613585550001631],[-0.0034513375184000994, -0.0017965834956999438, -0.001225746531299976, -0.00076970897500000524, -0.00056573698139994466, -0.0009916475936000424, -0.00059110303939990949, -0.00095562788649994346, -0.00087326822130001647, -0.00070820009219990654]], color=color[0])
pylab.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9],[0.51950351814649998, 0.29213562088450001, 0.2716140568673, 0.26930303540799994, 0.24855936025219999, 0.2542161643598001, 0.258417140371, 0.25767210883379998, 0.25739172606299998, 0.25107594849750003], color=color[1], linewidth=2, label='bump, vision')
pylab.errorbar([0, 1, 2, 3, 4, 5, 6, 7, 8, 9],[0.51950351814649998, 0.29213562088450001, 0.2716140568673, 0.26930303540799994, 0.24855936025219999, 0.2542161643598001, 0.258417140371, 0.25767210883379998, 0.25739172606299998, 0.25107594849750003],yerr=[[-0.0090089101690999929, -0.0022531041113000305, -0.0017109800600000336, -0.0014481468048000434, -0.0027505892992999992, -0.0052123670801999533, -0.0057577437850999114, -0.005764876378500039, -0.0052823244469000219, -0.004059800499299937],[-0.0073921579528000159, -0.0022915651561999373, -0.0019466121657999436, -0.0017005734404998973, -0.0027806878521999812, -0.0041159856090001168, -0.0057765400473000494, -0.0040367255679000236, -0.0051432702034999722, -0.0033270729435999902]], color=color[1])
pylab.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9],[0.62574352316570003, 0.40521260441970003, 0.29753481202880006, 0.2955207685888, 0.29310640527860005, 0.2764003036969, 0.26713572267219998, 0.26693489543500004, 0.25730250261169996, 0.2554961796652], color=color[2], linewidth=2, label='bump, movement')
pylab.errorbar([0, 1, 2, 3, 4, 5, 6, 7, 8, 9],[0.62574352316570003, 0.40521260441970003, 0.29753481202880006, 0.2955207685888, 0.29310640527860005, 0.2764003036969, 0.26713572267219998, 0.26693489543500004, 0.25730250261169996, 0.2554961796652],yerr=[[-0.0051021969095000896, -0.0042086518560999764, -0.0021801575123999717, -0.0025679157748999537, -0.0036403135043999169, -0.001886478026400018, -0.0020566585881999777, -0.0018512401813999824, -0.0020750216263000221, -0.0022717616267000085],[-0.0057453391080000138, -0.003233508555600062, -0.00293702702890003, -0.0021400769737000003, -0.0024995528733000594, -0.0014268089595000366, -0.001341606919099958, -0.001181118440700013, -0.0013206661776000161, -0.002140892537200012]], color=color[2])
pylab.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9],[0.52479114766559998, 0.24931791017020002, 0.20683124566119998, 0.19952742875340002, 0.20040496876819999, 0.19906509123620003, 0.19355992227320001, 0.19363706487470003, 0.1890401369353, 0.1873788074105], color=color[3], linewidth=2, label='all three')
pylab.errorbar([0, 1, 2, 3, 4, 5, 6, 7, 8, 9],[0.52479114766559998, 0.24931791017020002, 0.20683124566119998, 0.19952742875340002, 0.20040496876819999, 0.19906509123620003, 0.19355992227320001, 0.19363706487470003, 0.1890401369353, 0.1873788074105],yerr=[[-0.0068185812568000159, -0.0066491519454999481, -0.0021783495782000672, -0.0016501302617999702, -0.0019417648396999887, -0.0038212568181999751, -0.006090389599999968, -0.0045233868554999945, -0.0061448844725999763, -0.0056428624983999587],[-0.0071967568890998201, -0.0047253679685999861, -0.0035676664158999227, -0.0016614987498000111, -0.00186365097970001, -0.0033386425200000458, -0.0034439156011999983, -0.0051354603461000181, -0.0047107442158999813, -0.004157078880499987]], color=color[3])

pylab.xticks([0,1,2,3,4,5,6,7,8,9], [5,10,15,20,25,30,35,40,45,50])
pylab.xlim(0,9)
pylab.title('Collision Response')
pylab.legend(loc='upper right')
pylab.xlabel('amount of training data (seconds)')
pylab.ylabel('error')
pylab.savefig('lr_2.png', dpi=600)
pylab.show()
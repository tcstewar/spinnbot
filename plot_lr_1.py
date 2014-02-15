import pylab

pylab.figure(figsize=(8,4))
pylab.axes((0.11, 0.13, 0.85, 0.8))

color=['k', 'b', 'g', 'r']

pylab.plot([0, 1, 2, 3, 4, 5, 6, 7],[0.45077721721559999, 0.40372168451659995, 0.38063819377489994, 0.36765218894180002, 0.36047701604800009, 0.34854098046839999, 0.33848337337579998, 0.32900642344309999], label='bump', color=color[0], linewidth=2)
pylab.errorbar([0, 1, 2, 3, 4, 5, 6, 7],[0.45077721721559999, 0.40372168451659995, 0.38063819377489994, 0.36765218894180002, 0.36047701604800009, 0.34854098046839999, 0.33848337337579998, 0.32900642344309999],yerr=[[-0.013265381779199947, -0.013437916614800094, -0.0044647911065000545, -0.001681967947199936, -0.0014084514488998945, -0.00077153864980000764, -0.00066725146120005796, -0.00046413902760006343],[-0.012064005172299996, -0.0098137054201999918, -0.0043855462533999301, -0.0016006322225000091, -0.0015216810068000575, -0.0009909929340999879, -0.00078496901829999688, -0.0004114867839999925]], color=color[0])
pylab.plot([0, 1, 2, 3, 4, 5, 6, 7],[0.41341129187800008, 0.37749449837800003, 0.34623771137129999, 0.3111087466461, 0.29583614024819999, 0.27249395370759999, 0.25184347208939994, 0.23262005669969996], color=color[1], linewidth=2, label='bump, vision')
pylab.errorbar([0, 1, 2, 3, 4, 5, 6, 7],[0.41341129187800008, 0.37749449837800003, 0.34623771137129999, 0.3111087466461, 0.29583614024819999, 0.27249395370759999, 0.25184347208939994, 0.23262005669969996],yerr=[[-0.027785266776099937, -0.015515430454699997, -0.0087409518771000005, -0.0054220716469000063, -0.0029500679904999605, -0.0019725006428999992, -0.0024776339118000035, -0.0016884565214000113],[-0.027177436092700125, -0.013854861098000104, -0.0078351510641000432, -0.0044292627604999857, -0.0033514177269999834, -0.0013415376437999615, -0.0019758213936999502, -0.0013266185552999743]], color=color[1])
pylab.plot([0, 1, 2, 3, 4, 5, 6, 7],[0.36044984271919994, 0.32797571307869999, 0.30232267850920003, 0.28995787213160007, 0.27707500186599998, 0.26403148906309992, 0.25519789108169999, 0.24432621429909998], color=color[2], linewidth=2, label='bump, movement')
pylab.errorbar([0, 1, 2, 3, 4, 5, 6, 7],[0.36044984271919994, 0.32797571307869999, 0.30232267850920003, 0.28995787213160007, 0.27707500186599998, 0.26403148906309992, 0.25519789108169999, 0.24432621429909998],yerr=[[-0.027047134775899984, -0.017672144615600016, -0.003892905421899906, -0.0040572456741999607, -0.0032339877449999999, -0.0027035312431000769, -0.0065918208782000387, -0.0028030154090999682],[-0.015704226333299987, -0.011571601761000028, -0.0034103611732000938, -0.0039626564557000421, -0.0047592739836000431, -0.0027847225884999327, -0.0058723607012999834, -0.0027977928138000208]], color=color[2])
pylab.plot([0, 1, 2, 3, 4, 5, 6, 7],[0.35800996797899998, 0.31101486767409997, 0.25402347910849998, 0.23721116673370002, 0.216113753666, 0.19624479101880002, 0.18897807754690002, 0.1771350849686], color=color[3], linewidth=2, label='all three')
pylab.errorbar([0, 1, 2, 3, 4, 5, 6, 7],[0.35800996797899998, 0.31101486767409997, 0.25402347910849998, 0.23721116673370002, 0.216113753666, 0.19624479101880002, 0.18897807754690002, 0.1771350849686],yerr=[[-0.036046588185100037, -0.0074319024362999864, -0.0041195536681000178, -0.0079736550924999761, -0.0037913736615999838, -0.0031418788213999627, -0.0022935152658999647, -0.0039125769192999704],[-0.028557083645299963, -0.0088217753404999932, -0.0043254259892999414, -0.0039052101355000202, -0.0023816627960999981, -0.0026435380838000233, -0.0024196880487000194, -0.0046501691346000074]], color=color[3])

pylab.xticks([0,1,2,3,4,5,6,7], [10,20,50,100,200,500,1000,2000])
pylab.xlim(0,7)
pylab.legend(loc='upper right')
pylab.xlabel('number of neurons')
pylab.ylabel('error')
pylab.savefig('lr_1.png', dpi=600)
pylab.show()
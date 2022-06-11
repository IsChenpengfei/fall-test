# fall-test
fall test
1、收集数据集，在data下新建Annotations和images，一个放标签html，一个放图片
2、运行make_txt.py和voc_label.py可以划分训练集测试集，以及生成类别和框框的坐标
3、修改yaml里面的类别
4、修改train.py，自行设置模型权重格式等
5、运行train.py训练
6、运行detect.py检测
7、export.py权重转换

# Chinese character recognition

Pytorch 实现中文手写汉字识别

## Environment
Ubuntu: 16.04

Python: 3.5.2

PyTorch: 1.0.1 gpu

## Dataset
Divide the data into **train** and **test** folders. In each folder, put the images of the same class in the same sub-folder, and label them with integers. Like this:

![](https://raw.githubusercontent.com/chenyr0021/Chinese_character_recognition/master/pic.png)

In this project, we use a data set from [train_set](http://www.nlpr.ia.ac.cn/databases/download/feature_data/HWDB1.1trn_gnt.zip), [test_set](http://www.nlpr.ia.ac.cn/databases/download/feature_data/HWDB1.1tst_gnt.zip).
Also can download it using:
```
wget http://www.nlpr.ia.ac.cn/databases/download/feature_data/HWDB1.1trn_gnt.zip
wget http://www.nlpr.ia.ac.cn/databases/download/feature_data/HWDB1.1tst_gnt.zip
```
This dataset contains 3755 classes in total.

To process it, we use a python program from a [blog](https://zhuanlan.zhihu.com/p/24698483).

*This blog also implement recognition of this dataset, but using TensorFlow.*

## Usage

Run command:
```
python3 chinese_character_rec.py [option] [param]
```
where options and params are:

options|type|default|help|chiose
-------|----|-------|------|----
--root|type=str|default='/home/XXX/data'|help='path to data set'|
--mode|type=str|default='train'||choices=['train', 'validation', 'inference']      
--log_path|type=str|default=os.path.abspath('.') + '/log.pth'|help='dir of checkpoints'|                                                         
--restore'|type=bool|default=True|help='whether to restore checkpoints'|    
--batch_size'|type=int|default=16|help='size of mini-batch' |
--image_size'|type=int|default=64|help='resize image'|
--epoch'|type=int|default=100||
--num_class'|type=int|default=100||choices=range(10, 3755)

## Specific indroduction
See: 
https://blog.csdn.net/qq_31417941/article/details/97915035

#汉字识别



Pytorch实现中文手写汉字识别

##环境
Ubuntu:16.04
Python：3.5.2
PyTorch:1.0.1 gpu

##数据集

将数据分为**训练**和**测试**文件夹。在每个文件夹中，将同一类的图像放在同一子文件夹中，并用整数标记它们。这样地：
![](https://raw.githubusercontent.com/chenyr0021/Chinese_character_recognition/master/pic.png)

在这个项目中，我们使用[train_set]中的数据集(http://www.nlpr.ia.ac.cn/databases/download/feature_data/HWDB1.1trn_gnt.zip)，[测试集](http://www.nlpr.ia.ac.cn/databases/download/feature_data/HWDB1.1tst_gnt.zip).

也可以使用以下方式下载：

```
wget http://www.nlpr.ia.ac.cn/databases/download/feature_data/HWDB1.1trn_gnt.zip

wget http://www.nlpr.ia.ac.cn/databases/download/feature_data/HWDB1.1tst_gnt.zip

```

该数据集总共包含3755个类。


为了处理它，我们使用[博客]中的python程序(https://zhuanlan.zhihu.com/p/24698483).

*这个博客也实现了对这个数据集的识别，但使用了TensorFlow*


##用法

运行命令：

```
python3 chinese_character_rec.py[选项][参数]

```

其中选项和参数为：

options|type|default|help|chiose

-------|----|-------|------|----

--root|type=str|default='/home/XX/data'|help='数据集的路径'|

--mode|type=str|default='train'||choices=['train'，'validation'，'infraction']

--log_path | type=str | default=os.path.abspath（'.'）+'/log.pth'| help='dir of checkpoints'|

--restore'|type=bool|default=True|help='是否恢复检查点'|

--batch_size'|type=int|default=16|help='小批量的大小'|

--image_size'|type=int|default=64|help='size image'|

--epoch'|type=int|default=100||

--num_class'|type=int|default=100||选项=范围（10，3755）

##具体产量

请参阅：

https://blog.csdn.net/qq_31417941/article/details/97915035
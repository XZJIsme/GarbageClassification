# 基于 ResNet 的垃圾分类系统&nbsp;(Garbage Classification Powered by ResNet)<br>
欢迎提 issue 喔&nbsp;:-O

<div align=center><img width="392" height="215" src="https://user-images.githubusercontent.com/30148847/160409730-d6d6f0fa-55d1-4dd9-894a-ee020b638463.png"/></div>
<div align=center><img src="https://user-images.githubusercontent.com/30148847/160409316-e0b306a7-da75-4503-84cd-9ccd7ffea7c9.png"/></div>

## Get started
```
pip install -r requirements.txt
pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113
```
安装字体“等距更纱黑体 SC”获得最好体验

配置 server_ip.txt、local_ip.txt

先启动 AI_server_listener.py，再启动 main.py

如果要打包为 exe，分别打包 main.py 和 AI_server_listener.py。打包客户端（main.py）时推荐使用 UPX 压缩

```
pyinstaller.exe -F .\main.py [--upx-dir=UPX 路径] [-i 14-garbage-classification-icon.ico]
pyinstaller.exe -F .\AI_server_listener.py [--upx-dir=UPX 路径]
```
## Introduction
当前的体验一般般，模型训练得泛化能力也很不好，但是 anyway，撑过了实训…… 无语的实训…… 不过没有实训，也不会做这个东西，至少算是个项目吧！

AI 文件夹里的是后端，其余都是客户端

前端用的 Qt，基于 [PyDracula](https://github.com/Wanderson-Magalhaes/Modern_GUI_PyDracula_PySide6_or_PyQt6)
，数据库用的 SQLite

后端用的 Socket 进行简单的通信，模型用的 ResNet

主要功能：<br>
· 选择图片进行垃圾分类识别，在识别前可以对图片进行剪裁
<br>· 批量识别
<br>· 用户反馈错误的识别结果后修正模型参数
<br>· 模型训练，可以实时传递回训练的 loss 下降情况

## Screenshots
![image](https://user-images.githubusercontent.com/30148847/160412513-0ab2937b-1798-48db-8327-af01b38021fc.png)
![image](https://user-images.githubusercontent.com/30148847/160412435-8bed7e6d-7856-4e00-a20d-3dad48b80dd6.png)
![image](https://user-images.githubusercontent.com/30148847/160412617-74309ff2-407f-4471-b06e-344b6f498e51.png)

## ToDo
·&nbsp;训练失败的消息回传<br>
·&nbsp;可以自定义图片的&nbsp;resize&nbsp;大小<br>
·&nbsp;加入&nbsp;Transformer 模型<br>
·&nbsp;优化组件布局<br>
·&nbsp;将等距更纱黑体嵌入项目
·&nbsp;不需要配置本地 IP，直接回传

# FROM 指定一个基础镜像，然后这个基础镜像之上安装NodeJS和应用程序，当然也可以直接安装基于NodeJS开发的镜像
# FROM node:14-alpine 这个node是基于Linux开发的一个镜像，alpine是基于alpine这个Linux发行版来的（非常轻量的）
FROM node:14-alpine

# COPY 命令可以复制文件，这里是将某些文件复制到镜像的根目录下
# COPY 命令后面可以跟两个参数，一个源文件路径（相对DOckerfile的路径），一个是目标路径（是相对于镜像的路径）
COPY index.js /index.js

# CMD 可以运行应用程序
# CMD 后面可以加上两个参数，一个是可执行程序的名字，一个是这个可执行程序接受到的参数
# CMD [ "node","/index.js" ]  可以，下面这种写法也可以
CMD node /index.js

# 然后我们可以用以下的Docker命令来制作Docker Image
# docker build -t hello-docker:dev .
# docker build -t [仓库名]:[标签] [路径]


# 接下来使用docker images 查看制作好的Dokcer Image，刚才做好的Docker Image并不会以文件的形式存储而是在Docker中
# PS D:\git_repository\Code_Study\helloDocker> docker images
# REPOSITORY     TAG       IMAGE ID       CREATED              SIZE
# hello-docker   dev       0f42e4904295   About a minute ago   180MB


# 最后如果我们需要这个Docker运行起来只需要使用docker run这个命令就能运行起来了
# PS D:\git_repository\Code_Study\helloDocker> docker run hello-docker:dev
# Hello Docker

# 接下来我们准备开始上传这个Docker Image
# 首先需要登录，通过docker login
# PS D:\git_repository\Code_Study\helloDocker> docker login
# Authenticating with existing credentials...
# Login Succeeded

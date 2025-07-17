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

# 然后我们上传本地的Image到Docker Hub上去
# 首先我们给Image标记一个路径，因为如果直接docker push的话，不知道要推送到哪里去
# docker tag hello-docker:dev cafe_latte/hello-docker:dev
# 另外我们还需要提前在Docker Hub里面先建立好对应的repository才行，而且名字/repository这些都需要一一对应Docker tag里面的路径，否则失败
# PS D:\git_repository\Code_Study\helloDocker> docker tag hello-docker:dev caferate/hello-docker:dev 
# PS D:\git_repository\Code_Study\helloDocker> docker push caferate/hello-docker:dev
# The push refers to repository [docker.io/caferate/hello-docker]
# d1f534147743: Pushed
# 38a733b6f4b5: Pushed
# 8f665685b215: Pushed
# e5fca6c395a6: Pushed
# 561cb69653d5: Pushed
# f56be85fc22e: Pushed
# dev: digest: sha256:0f42e4904295f483c40b6b2927c32e9a0e8304b340069d62921b9692ce1c45cf size: 856

# 因为我们刚才有一个错误的docker tag 命令，所以我们现在将他删除，就是使用下面的这个命令删除
# PS D:\git_repository\Code_Study\helloDocker> docker rmi cafe_latte/hello-docker:dev
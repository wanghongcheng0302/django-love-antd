###### 如何运行

1. pip install -r requirements.txt 安装依赖
2. tests.django_tests，测试用例，生成前端编译代码
3. 安装前端依赖，并npm run start
4. 后端创建超管
5. 目前前端登陆后要刷新再登陆，待修复

###### 待优化

1. 前后端代码格式，前端需通过eslint检查，后端pylint检查
2. 模板中的逻辑还可以优化，原则上把逻辑尽量用python层面
3. 框架自身的mvc层
> 模型（M）：定义生成增删改查的标准，可以兼容model、serializer、以及任何实现了接口的类
> 
> 控制层（C）：区别于django的view，用做后端到前端的映射控制，例如自定义的过滤器，以及一切可以替代jinja模板中逻辑的函数
> 
> 视图层（V）：jinja模板层
4. 前端遵循mvc模式，目前ant design pro采用的是按模块划分
   

###### TODO

1. 粗略完成增删改查，确定思路的可行性，把坑先踩一遍，比如Model解析这部分，并了解ant design pro
2. 学习react全家桶，至少达到当下vue的水平
3. 熟悉设计模式，重新设计框架
4. 以ant design为模板设计后端Field，扩展字段类型
5. 调研redash，设计报表

###### 草稿本
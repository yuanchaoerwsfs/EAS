## 项目需求

```
登录角色：管理员、老师、学生

1、管理员可以创建学校，创建/编辑课程（课程属于学校），添加/编辑老师，冻结学生，给老师发工资，以及查看流水，设置虚拟学习人数，以及设置主页的欢迎语

2、管理员可以查看KPI数据，包含累计付费人次、今日营收、累计营收、累计注册学员、总课程数量、老师人数

3、课程包含价格、学习人数、授课老师

4、学员注册后，可以随意选择学校，并且购买课程，购买课程之后，可以查看授课老师的联系方式

5、老师只能由管理员创建，并且只有当管理员给课程设置授课老师之后，该老师才可以看到对应课程，并且安排已购课学员学习，老师登录之后，可以设置自己的联系方式

6、学员和老师可以查看热销课程数据

7、所有功能必须登录之后才能使用
```

## 1、需求分析

```
管理员
	1、注册功能	-注册页面
	2、登录功能	-登录页面
	3、创建学校功能	-创建学校页面
	4、创建课程功能	-创建课程页面，课程列表页面
	5、编辑课程功能	-编辑课程页面
	6、添加老师功能	-添加老师页面，老师列表页面
	7、编辑老师功能	-编辑老师页面
	8、冻结学生功能	-学生列表页面
	9、给老师发工资	-财务中心-发工资页面
	10、查看流水		-财务中心-查看流水页面
	11、设置虚拟学习人数	-设置页面
	12、设置主页的欢迎语	-设置页面
	13、查看KPI数据	-管理员主页
	14、退出账号功能
学生
	1、注册功能
	2、登录功能
	3、购买课程功能（可以选择学校）
	4、联系老师功能
	5、查看热销课程数据	-学生主页
	6、退出账号功能
老师
	1、登录功能
	2、管理课程功能（安排学生学习）	-管理课程页面
	3、设置联系方式功能	-设置页面
	4、查看热销课程数据
	5、退出账号功能
	
	
	
	
```

## 2、架构设计

```
三层架构
	-用户视图层：与用户交互
		-core
			src.py
	-逻辑接口层：做核心的业务逻辑处理
		-interface
			-admin_interface.py
			-teacher_interface.py
			-student_interface.py
	-数据处理层：用于做数据的增删改查
		-db
			db_handler.py
			models
```


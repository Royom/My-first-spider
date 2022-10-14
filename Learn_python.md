#### 一.准备工作.下了Python和Pycharm

1.pycharm安装requests、re、bs4、scrapy

#### 二.学习Python、爬虫相关知识

对其中部分内容的笔记：

> *在Preview(预览功能)中，控制台会把发送过来的json数据自动转换成javascript的对象格式,而且可以层层展开，方便前端工程师遍历调用。而 Response中的数据是没有进行格式化的.*
>
> *这里所讲的的**格式化**是指:对后台传输过来的json、html、css等数据进行格式上的转换.*
>
> ***Perview**的意思是(response preview)：响应-预览 (响应资源**进行了**格式处理的内容)*
> ***Response**的意思是:(Raw response data)：原始-响应-的数据(响应资源**未进行**格式处理的内容)*
>
> ***在Preview(预览功能)**中，控制台会把**发送过来的json数据自动转换成javascript的对象格式**。*

1 过长可用\提行

2 **.strip()** 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列

3 **f-string**:格式化字符串常量 与**str.format**类似

```
list_ = [1,2,3]
print(list_, f'has a length of {len(list_)}.')

[1,2,3] has a length of 3.

print(list_, f'has a length of {{len(list_)}}.')

[1,2,3] has a length of {len(list_)}.

print(list_, f'has a length of {{{len(list_)}}}.')

[1,2,3] has a length of {3}.
```

4 **str.format**的使用:

```
>>>"{} {}".format("hello", "world")    # 不设置指定位置，按默认顺序`

`'hello world'` 

`"{0} {1}".format("hello", "world")  # 设置指定位置`

`'hello world'` 

`>>> "{1} {0} {1}".format("hello", "world")  # 设置指定位置` 

`'world hello world'
```

```
`print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))`  

`通过字典设置参数` 

`site = {"name": "菜鸟教程", "url": "www.runoob.com"}` 

`print("网站名：{name}, 地址 {url}".format(**site))`   

`通过列表索引设置参数`

`my_list = ['菜鸟教程', 'www.runoob.com']`

`print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的`
```

输出结果：

```
网站名：菜鸟教程, 地址 www.runoob.com
网站名：菜鸟教程, 地址 www.runoob.com
网站名：菜鸟教程, 地址 www.runoob.com
```



5 **range(start, stop[, step])**

6 def 定义函数

7 **str** 字符串类型
byte 二进制

8 **list[]**
**L = ['Apple', 123, True]**
**tuple()**
t = (1,) 表示只有一个元素需要","
**dict**  字典

`**d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}**`
`d['Michael']`
`95`
`d.get('Thomas')`
`d.get('Thomas', -1)`
`-1`

9 **resp.close()** #关闭resp
10 **open(  ,encoding="utf-8")**

-------

11  **re解析 元字符**
**.**匹配除换行符外的任意字符
**\w**字母数字下划线 **\d**数字 \匹配换行符
**^**匹配字符串的开始 **￥**匹配字符串的结束
\W \D \S为小写字母的反义
**|**或者      **()**匹配括号内的表达式，也表示一个组
**[]**匹配字符组里的字符里面可以是[a-zA-Z0-9]
**[^]**匹配除了字符组中字符的所有字符
**量词（放在元字符后）**
 **星号** 重复零次或更多次    **+**重复一次或更多次
**？**重复零次或一次 **{n}**重复n次
**{n,}**重复n次或更多次 **{n,m}**重复n到m次
**".加星号"贪婪匹配  .加星号?惰性匹配（若有多个选择短的）（回溯算法）**
(?P<xxxxx>.星号?) .*星号?匹配到的东西会给<xxxxx> .星号?可以是其他的元字符  用于单独提取正则中的内容
**re,compile** 将一个长的正则进行预加载方便使用
**re.findall** 查找所有 返回list
**re.search** 匹配第一个结果并返回 匹配不上则None
**re.match** 只能从字符串的开头进行匹配
**re.finditer** 和findall差不多 只是返回的是迭代器
如**print(result..group(“abc”))**获取abc里的内容
**re.S** 将字符串作为整体可以跨行匹配

正则表达式前用**r**表示内容的原始含义

12 **open(name[, mode[, buffering]])**

mode类型略多 个人觉得常用的有t,r,w,a,b

**csv.reader()**

**csv.writer()**

**csvwriter.writerow()**

**csvwriter.writerows()**

**csv.register_dialect**

**csv.excel**

.......未完待续

-------

**BS4** 

[这个讲的还可以](https://www.cnblogs.com/gl1573/p/9480022.html)

from bs4 import BeautifulSoup

**BeautifulSoup(resp.text,"html.parser")**指定html解析器
表格内的可以从table开始看
如出现class作为属性（class是python关键字），可以写成class_ 
attrs
html : 行 tr 列 td

#### 三.尝试（问题记录）

##### PART1

##### 找到数据，发送请求

直接请求不行，要加上header

1.*待解决：页面源代码和抓包看element都没找到评论数据 虽然好像在element有？怎么用re？*

*解决：抓包里的productPageComments的源代码里可以找到评论数据，但用.json()转化好像更好做，虽然re应该也没问题*

2.复制url 打印出来数据是一行 不过是各种数据  准备筛选

用chrome的检查发现该url在"preview"里分类的很整齐

3.转为utf-8格式是乱码

gbk格式有一些区别 从31189字符到31211 但不知道具体啥变化 或许都行？

4.为要得到多页的数据：点击下一页发现只有page改变，所以可以用for循环+.format(用url的 page部分)

考虑到一直爬有被封的风险：在网上查到用time.sleep()设置延迟 *犯错:解析数据时用了time导致错误'`str' object has no attribute 'sleep'`*  

----------

##### PART2

***筛选出我需要的数据***

1.百度查询网页源代码和elment的区别：`“查看网页源代码”的代码内容是服务器发送到浏览器的原封不动的源代码，不包括页面动态渲染的内容；“审查元素”包括源代码+js动态渲染的内容，即最终展示的html内容`

2.尝试用正则解析式筛选pagecomment页面里的数据，发现也可以（注: .group('名字'))用于使内容正常显示）

```
page = resp.text
obj = re.compile(r'"content":"(?P<abc>.*?)","vcontent"',re.S)
result = obj.finditer(page)
for it in result:
    print(it.group('abc'))
```

但在上网查询方法时看到因为评论是以JS的格式保存在网页中，可以用.json()直接转换成键值数据来筛选，这样更简单，尝试另一种方法

通过.json()拿到字典型的数据用键-值去筛 *犯错：忘记python对行对齐的重视 在写for循环的时候忘了tab，导致每组数据被上组数据覆盖，排查了半个小时才发现这个问题*    **犯了两次这个错误（第二次在for的再次缩进上）**

3.*犯错:先用两页尝试了一下 结果time函数没有起作用...?*

*解决（？）:当把爬的页码增多后没有这个情况了..?*

----------

##### PART3

##### 保存数据

1.*待解决：数据可以爬，但怎么保存下来呢...?*

*解决:txt或者csv*

2.open()函数用什么mode？

3.用csv模块写入文件以保存数据

4.*待解决：open函数是否要带newline*

暂未解决：网上的有点绕 之后再看，[链接](https://blog.51cto.com/u_15127580/4379959)

5.*用writerrow写入时遇到错误:`TypeError: writerow() takes exactly one argument (3 given)` 解决方案：把3个变量放在一个列表里就可以解决*

6.保存到csv文件，之前encoding ='gbk'是乱码，用utf-8后可以正常浏览了

> python输出的csv文件用excel打开，里面的中文会变成乱码，但用window下的记事本或mac下的numbers打开就正常显示。
>
> 原因是python输出的文件是utf-8编码写入的，excel默认以gbk方式读取，导致乱码发生。

---------------

#### 四.进阶任务：

1.安装**mariadb**（听说可以替代MySQL）

**2.学习一些SQL相关知识**

1  SQL对大小写不敏感

#### 2  创建数据库

```
create database 数据库名;
```

*-- 在建库时指定字符集，避免中文数据乱码的问题*

```
create database 数据库名 default charset='utf8';
```

#### 3  显示数据库结构

```
show create database 数据库名;
```

#### 4  删除数据库

```
drop database 数据库名;
```

#### 5  选择数据库

注意：在创建表之前，需要选择当前操作的数据库

```
Use 数据库名；
```

#### 6  删除表

```
drop table if exists '表名'；
```

#### 7  创建表

```
create table '表名'（

​	字段名（多用ID？) 类型 约束 （主键，非空，唯一，默认值），

​	字段名 类型 约束 （主键，非空，唯一，默认值），

）编码，存储引擎
```

#### 8  编码

```
default charset='utf8';
```

约束：

NOT NULL 表示某列不能存储NULL值

UNIQUE 保证某列的每行有唯一值

PRIMARY KEY 上两者的结合

FOREIGN KEY 保证一个表中的数据匹配另一个表中的值的参照完整性*（建议少用？）*

CHECK 保证列中的值符合制定的条件

DEFAULT 规定没有给列赋值时的默认值

用COMMENT'xxx' 可以加注释xxx

#### 9  插入语句：

```
insert into 表名（字段列表）VALUES （'xxx'）;
```

#### 10  删除语句：

```
delete from 表名 where 字段名 = 原有值;*（？）*
```

#### 11删除字段

```sql
alter table 表名 drop 字段名
```

#### 12添加新字段

```sql
alter table 表名 add 新字段名 新数据类型 [新约束条件]
SQL 复制 全屏
```

#### 13修改字段名

```sql
alter table 表名 change 旧字段名 新字段名 新数据类型
```

#### 14修改数据类型

```sql
alter table 表名 modify 字段名 新数据类型
```

#### 15修改表名

```css
rename table 旧表名 to 新表名
```

#### 16表记录的插入

SQL语句：

```scss
insert into 表名(字段列表) values(值列表);
```

提示：当插入的数据值的个数与表字段个数相同时，可以省略字段列表

```scss
insert 数据库名(id,name) values(1,'newdream');
insert 数据库名 values(2,'newdream1');
```

#### 17一次插入多条记录

```sql
insert into 表名(字段列表) values (值列表1),(值列表2),...（值列表n）;
```

#### 18使用insert...select插入结果

```sql
insert into 目标表名(字段列表1)
select(字段列表2) from 源表 where 条件表达式
 
insert into stu_bak(id,name)
select id,newname from stu where id>2;
```

注意：字段列表1与字段列表2的字段个数必须相同，且对应字段的数据类型尽量保持一致。
如果果源表与目标表的表结构完全相同，“(字段列表1)”可以省略。

update 表名 set 字段名 = 修改的内容 where 

#### 19复制表结构及数据到新表

```sql
create table 新表 select * from 旧表;
```

#### 20只复制表结构到新表

```sql
create table 新表 select * from 旧表 where 1=2;
```

#### 21修改表记录

```sql
update 表名 set 字段名1=值1,字段名2=值2,...,字段名n=值n
[where 条件表达式]
 
update stu set newname='new5' where id=1;
```

where 子句指定了表中的哪些记录需要修改。若省略了where子句，则表示修改表中的所有记录。
set子句指定了要修改的字段以及该字段修改后的值。

#### 22使用delete删除表记录

```sql
delete from 表名 where 条件表达式;
```

说明：如果没有指定where⼦句，那么该表的所有记录都将被删除，但表结构依然存在。

#### 23使用truncate清空表记录

```sql
truncate table 表名;
```

#### 24delete和truncate的区别

Delete不加WHERE条件是删除所有数据
Truncate不能够加WHERE条件
Delete可以加WHERE条件
Truncate会重置AUTO_INCREMENT
Delete可以进⾏回滚操作

#### 25表记录的查询

```csharp
select 字段列表 from 表名 
where条件表达式
```

#### 26表记录的查询—给列取别名

可以为字段列表中的字段名或表达式指定别名，中间使用as关键字分隔即可（as关键字可以省略）。多表查询时，同名字段前必须添加表名前缀，中间使用“.”分
隔。

```python
Select id as ’学⽣学号’,newname ‘学⽣姓名’ from stu；
```

#### 27读取本地文件

```
load data local infile "文件路径" into table 表名
```

---------------

*目前(最后）状况：数据能爬，在mariadb也把对应的列头写了，但不知道怎么把爬下来的数据按数据库的行列格式放进去*

*因为mariadb教程很少 还是又安装了mysql*

*使用mysql创建数据库又出了不知道是什么原因导致的错误...*



end...(for now 2022.10.14.21:00:00)

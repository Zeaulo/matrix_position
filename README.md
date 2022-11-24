
# README
作者 : 张文浩，刘树华\
Python包名 : matrix_position\
最新版本 : 0.0.4

Author : Jinghao, LiuShuhua\
Python package name : matrix_position\
least version : 0.0.4
## English:
Our initial thinking is that we always conduct the algorithmic research or exploration about matrix during lots of subject learning.\
But when we are programming using by Python, we often need to acquire the ongoing point's information(including of position and value) and its surrouding point information\
when we are learning in the algorithm.(Such as Breadth Search First algorithm from matrix, Snake game from matrix, etc.)\
At the same time, we wanna be more acquainted with matrix, and hope to have a deeper understanding of the matrix in programming. 
Therefore, the proposal of this project is very meaningful for us to learn, and we also hope to help people with the similar trouble\
Final introduction : There is a Python package that express the data structure of matrix, and combined with the matrix, it can obtain the position and value around any two-dimensional coordinates.
(**Note: the class objects created in this project are only for the data structure of matrix, which is different from 3D array, 4D array, etc. (of course, one-dimensional array can also be expressed normally)**)\
![matrix 2D coordinate system](https://user-images.githubusercontent.com/106080312/203535754-2fcc0d5e-a132-4250-a8e1-203ea490d3ab.png)\
In this Python project, we defined a matrix class according to the figure above to describe the data mechanism of matrix\
Before use, the input matrix A is instantiated. The following is an example:
```
import matrix_position
list1 = [[1,2,3,4],[5,6,7,8]] # We recommend this way to make the matrix instantiation
A = matrix(list1) # Remember the variable of A,which will transform list1 to the matrix class and instantiate
x,y = 1,1         # Remember the variables of x and y ,those values chosen according to the matrix coordinate
value = 5         # Remember the variable of value, whose value according to the matrix
position = (0,2)  # Remember the variable of position, whose value chosen according to the matrix coordinate
```
Foundational variables and functions:
```
A.matrix                                        -- Variable - return the matrix (Actually,it will return the initial input data)
A.matrix[x][y]                                  -- Value    - return the value about (x,y) coordinate
A.length(=A.columns)                            -- Variable - return the length of the matrix (=the number of rows)
A.width(=A.rows)                                -- Variable - return the width of the matrix (=the number of columns)
A.shape(=A.size)                                -- Variable - return the shape of the matrix (=the size of matrix)
A.matrix_dict                                   -- Variable - return the dictionary of the matrix
A.get_position((x,y),return_first_one=False)    -- Function - input  the value of the matrix, and return the value's position(coordinate) from the matrix
A.get_value(position)                           -- Function - input  position(coordinate) and return its value
...                                             -- ...
```
Related position's variables and functions：
```
A.now                    -- Variable - return the current position and its value.(fault=={(0,0):its value})
A.up()                   -- Function - update A.now's position to its upper position, and its value also change
A.down()                 -- Function - update A.now's position to its under position, and its value also change
A.turnleft()             -- Function - update A.now's position to its left  position, and its value also change
A.turnright()            -- Function - update A.now's position to its right position, and its value also change
A.fourD(position)        -- Function - input position(coordinate) and return its surrounding positions and values including four directions, and the order is ： ← ↑ ↓ →
A.eightD(position)       -- Function - input position(coordinate) and return its surrounding positions and values including eight directions, and the order is ： ← ↖ ↘ ↑ ↓ ↙ ↗ →
...                                             -- ...
```

---For personal reference only


## 中文:
我们最初的想法是：在学习的过程当中，由于经常会碰到涉及矩阵的算法研究或问题，\
而算法在进行的过程当中，我们往往希望能够及时地获知进行点及其周围信息。（*如矩阵的广度优先搜索、矩阵的贪吃蛇游戏等）*\
同时我们希望在编程中能够熟悉并加深对矩阵的了解，因此这个项目的提出对于我们来说很有学习意义，也希望能够帮助到有同样想法的人。\
最后：这是一个Python包，它可以表达矩阵这一数据结构，并且结合该矩阵，能够获取任意二维坐标周围的位置和值。 
（**注意：该项目所创建的类对象仅针对于矩阵这一数据结构，区别于3维数组、4维数组等。（当然，一维数组也能正常表达）**）\
![matrix 2D coordinate system](https://user-images.githubusercontent.com/106080312/203535754-2fcc0d5e-a132-4250-a8e1-203ea490d3ab.png)\
在开发这个Python包之前，我们根据上图定义了一个matrix类，以此来描述矩阵这一数据机构。\
在使用前，先将输入的矩阵A实例化，如：
```
import matrix_position
list1 = [[1,2,3,4],[5,6,7,8]] # 我们推荐这种方式去输入matrix类

A = matrix(list1) # 记住变量A，它将list1转化为matrix类并实例化
x,y = 1,1         # 记住变量x和y，它的值根据坐标选取
value = 5         # 记住变量value，它的值在矩阵中选取
position = (0,2)  # 记住变量position，它的值根据坐标选取
```
基本操作:
```
A.matrix                                        -- 变量 - 返回矩阵
A.matrix[x][y]                                  -- 值   - 返回(x,y)坐标的值
A.length(=A.columns)                            -- 变量 - 返回矩阵的长度（即返回矩阵的行数）
A.width(=A.rows)                                -- 变量 - 返回矩阵的宽度（即返回矩阵的列数）
A.shape(=A.size)                                -- 变量 - 返回矩阵的形状（即返回矩阵的大小）
A.matrix_dict                                   -- 变量 - 返回矩阵字典
A.get_position((x,y),return_first_one=False)    -- 函数 - 输入value返回矩阵内对应的坐标
A.get_value(position)                           -- 函数 - 输入position返回对应的value
...                                             -- ...
```
位置操作：
```
A.now                    -- 变量 - 返回现位置及对应的值,默认为{(0,0):value}
A.up()                   -- 函数 - 更新A.now的位置为其上面的位置，相应的值也同样会发生变化
A.down()                 -- 函数 - 更新A.now的位置为其下面的位置，相应的值也同样会发生变化
A.turnleft()             -- 函数 - 更新A.now的位置为其左边的位置，相应的值也同样会发生变化
A.turnright()            -- 函数 - 更新A.now的位置为其右边的位置，相应的值也同样会发生变化
A.fourD(position)        -- 函数 - 返回position周围上下左右的信息，返回的顺序为：← ↑ ↓ →
A.eightD(position)       -- 函数 - 返回position周围一圈的信息，返回的顺序为：← ↖ ↘ ↑ ↓ ↙ ↗ →
...                                             -- ...
```

---仅供个人学习参考。






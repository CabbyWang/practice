***
这两天朋友毕业设计是用代码实现几个算法, 我听后感觉很有兴趣(对于我这么一个没有接触过算法的人, 简直是看到了新世界啊), 于是想着用python帮他实现, 之后看到什么有意思我又能理解的算法, 我会继续用python去实现然后记录下来, Fighting !!
***
已知n个已知点的坐标(x0, y0, z0)...(xn, yn, zn), m个未知点的一维坐标(x0, y0)...(xm, ym), 推算出这些未知点的z坐标  
<br>
思路: 分解为已知n个点的坐标, 求一个点的z坐标
## 反距离权重插值法
求未知点到各个已知点的距离, 距离越小, 所占权重越大, 距离越大, 所占权重越小(这似乎就是反距离权重的意思)  
公式如下:  
![\frac{\sum_{n}^{0}zn * \frac{1}{sn}}{\sum_{n}^{0}\frac{1}{sn}}](https://github.com/CabbyWang/practice/blob/c89de6b2cfa12f00ae92d891eef2b163fb1cfbd2/images/fanjuliquanzhongchazhifa.png)  
这里sn是未知点(x, y)到已知各个点的一维距离, 即  
![\sqrt{{(x - x0)_{}}^{2} + {(y - y0)_{}}^{2}}](https://github.com/CabbyWang/practice/blob/master/images/distance_between_two_point.png)  
zn是已知点坐标的z坐标, 1/zn相当于第n个点所占的权重, 各个点z坐标与相应权重的乘积之和除以总权数, 即是未知点z坐标的大致位置


## 最邻近插值法
也是求未知点到各个已知点的距离, 取离得最近的已知点的z坐标作为z坐标, 这个就比较简单了, 应该也是误差最大的方法了吧/哭笑  

***
详细见[代码](https://github.com/CabbyWang/practice/blob/c89de6b2cfa12f00ae92d891eef2b163fb1cfbd2/code/IDW.py)

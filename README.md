# frelation
在机器学习中，构造的特征多且乱，这个库用来展示已经构造的特征关系，方便查漏补缺。

往往在构造过程中，淹没在巨量的构造函数中无法自拔。

`frelation`即`feature relation`用来展示已经构造好的特征，非常方便的查看哪些特征已经被构造，哪些特征被多次构造，构造关系如何，一目了然。

# 安装

1. 到https://github.com/pipdax/frelation 中下载文件，

   或者

   ```shell
   git clone 
   ```

   目录结构如下

   ├── frelation
   │   ├── frelation.py
   │   └── \_\_init\_\_.py
   ├── LICENSE
   ├── README.md
   └── setup.py

   2. 使用setup.py安装

```she
cd frelation
python setup.py install
```

# 使用实例

```python
fr = frelation("The Title", "The subtitle")
fr.addNodes(['a', 'b', 'c'], 0)
fr.addNodes(['d', 'e'], 3)
fr.addNodes(['f', 'g', 'h'], 5)
fr.addLink('a', 'd', 'g')
fr.addLink('d', 'h')
fr.addLink('b', 'e', 'h')
fr.addLinks([{'source': 'a', 'target': 'e'}, {'source': 'c', 'target': 'e'}])
fr.show()
```

# 效果展示

![show](/home/dax/my/git/frelation/show.gif)

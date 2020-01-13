# ml-landing

`ml-landing`项目旨在机器学习项目如何工程落地，因此，本项目不会设计算法的原理，算法的具体实现过程等偏理论的一些内容，大部分内容是帮助我们如何将一个机器学习项目工程化和落地，帮助大家在实际项目中如何使机器学习被“应用”。

## 项目概览

`ml-landing`将会分成五个部分

- 数据来源

对于机器学习来说，数据是至关重要的，没有数据，机器学习也无从谈起，因此，第一步我们将讨论如何从数据源中获取数据。

- 数据预处理

机器学习中，有一句常被提起的话：`garbage in, garbage out`，在机器学习中，意思是如果数据清理的不干净，数据质量低下，那么再好的算法，输出的模型也是无用的。因此，数据预处理在整个机器学习过程中，起到了非常大的作用，没有一个好的预处理，往往产出的模型也是无用的。因此，我们将在章节讨论一些常用的数据预处理方法。

- 建模

我们将在本章着重描述建模过程，包括数据划分、如何建立一个`pipeline`等，但是和开头所讲的那样，不会涉及算法的原理等内容。

- 评估

模型训练完成后，如何对模型进行评估是非常重要的，这将保证我们的模型是可用且符合我们预期的。

- 部署

建模完成，如何将模型应用于实际的业务场景是本章所有讨论的内容。

## 关于`Landing`

每章最后都有一个`Landing`的小节，在这一小节中，我们将会从实战角度出发，所有的代码可以在`code`文件夹下查看。

## 涉及的库

本项目主要涉及到的库有

- `pandas`：用于数据读写，清洗等
- `scikit-learn`：用于数据建模和对模型的评估
- `flask`：用于部署机器学习，搭建API服务


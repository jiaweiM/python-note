# MHCflurry

- [MHCflurry](#mhcflurry)
  - [简介](#简介)
  - [命令行使用教程](#命令行使用教程)
    - [下载模型](#下载模型)
    - [预测](#预测)
  - [API](#api)
    - [底层接口](#底层接口)

## 简介

大部分预测任务可以使用 `Class1PresentationPredictor` 类完成，该类提供了 `mhcflurry-predict` 和 `mhcflurry-predict-scan` 命令行工具提供的功能。

`Class1PresentationPredictor` 包含用于生成结合亲和力预测的 `Class1AffinityPredictor`实例和用于生成抗原处理预测的 `Class1ProcessingPredictor` 实例。打分值通过结合亲和力和处理预测的逻辑回归模型计算。

使用 `load` 方法载入预先训练好的预测器，也可以传入模型路径，载入对应的模型：

```py
from mhcflurry import Class1PresentationPredictor
predictor = Class1PresentationPredictor.load()
predictor.supported_alleles[:5]
# ['Atbe-B*01:01', 'Atbe-E*03:01', 'Atbe-G*03:01', 'Atbe-G*03:02', 'Atbe-G*06:01']
```


## 命令行使用教程

### 下载模型

大多数用户会直接使用 MHCflurry 训练好的模型。这些模型单独分发，可以使用 `mhcflurry-downloads` 工具下载；

```
mhcflurry-downloads fetch models_class1_presentation
```

下载文件的位置和使用的系统有关，可以通过如下命令查看路径：

```
mhcflurry-downloads path models_class1_presentation
```

另外还有一些训练数据和实验模型可供下载，可以通过如下命令查看：

```
mhcflurry-downloads info
```

大部分用户只需要 `models_class1_presentation`，该模型包含peptide/MHC-I 亲和力（binding affinity, BA）预测和抗原加工（antigen processing, AP）预测。

### 预测

`mhcflurry-predict` 命令用于预测单个肽段。默认使用预先训练好的模型。使用其它模型可以使用 `--models` 参数指定。

例如：

```
$ mhcflurry-predict
    --alleles HLA-A0201 HLA-A0301
    --peptides SIINFEKL SIINFEKD SIINFEKQ
    --out /tmp/predictions.csv
Forcing tensorflow backend.
Predicting processing.
Predicting affinities.
Wrote: /tmp/predictions.csv
```

输出结果大致如下：

```csv
$ cat /tmp/predictions.csv
allele,peptide,mhcflurry_affinity,mhcflurry_affinity_percentile,mhcflurry_processing_score,mhcflurry_presentation_score,mhcflurry_presentation_percentile
HLA-A0201,SIINFEKL,11927.158941532069,6.296000000000002,0.26470961794257164,0.020690210604074,11.6303260869565
HLA-A0201,SIINFEKD,30039.79614570185,41.398,0.024963302072137594,0.0036743984764636087,99.28660326086957
HLA-A0201,SIINFEKQ,28026.90550690346,30.226250000000004,0.06154933862853795,0.00447008680074548,62.74467391304348
HLA-A0301,SIINFEKL,29871.585202288912,23.19225,0.26470961794257164,0.008586191856042273,27.617391304347805
HLA-A0301,SIINFEKD,33158.802891745494,62.27625,0.024963302072137594,0.0033393306217936363,99.28660326086957
HLA-A0301,SIINFEKQ,29705.412189610724,21.8915,0.06154933862853795,0.004225574919955567,62.74467391304348
```

结合亲和力的预测值在 `mhcflurry_affinity` 列，单位为 nM。值越小结合力越强。对具有免疫原型多肽的阈值一般设置为 500 nM。

`mhcflurry_affinity_percentile` 给出该等位基因和大量随机肽段亲和力中的百分位（0-100）。值越小表示亲和力越强，一般阈值为 2%。

后面给出了抗原处理分数和呈递分数，范围 [0,1]，值越大表示越趋向于处理或呈递。

> 处理预测（processing predictor）是实验性功能。它主要判断肽段是否能够在质谱中检测到，有等位基因无关。呈递打分（presentation score）是亲和打分和处理打分的简单逻辑回归结合得到。

## API

### 底层接口

如果只需要亲和力预测，可以直接使用 `Class1AffinityPredictor`，例如：

```

```
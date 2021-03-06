```text       
   Copyright (c) 2022 LongGengYung Authors. All Rights Reserved
====================================================================
            项 目：【LIC2021 DuIE 关系抽取】
         整理人：LongGengYung
         微 信：superior_god
         邮 箱：yonglonggeng@163.com
         公众号：庚庚体验馆
         知 乎：雍珑庚
====================================================================
```

# 1. 项目概况
## 1.1. 项目概述
基于预训练语言模型ERNIE设计了结构化的标注策略，可以实现多条、交叠的SPO抽取。

## 1.2. 项目目录
```text
DuIE/
├── data_loader.py # 加载数据
├── extract_chinese_and_punct.py # 文本数据预处理
├── README.md # 文档说明
├── re_official_evaluation.py # 比赛评价脚本
├── run_duie.py # 模型训练脚本
├── train.sh # 启动脚本
└── utils.py # 效能函数
```

# 2. 算法原理
针对 DuIE2.0 任务中多条、交叠SPO这一抽取目标，比赛对标准的 'BIO' 标注进行了扩展。
对于每个 token，根据其在实体span中的位置（包括B、I、O三种），我们为其打上三类标签，并且根据其所参与构建
的predicate种类，'将 B 标签进一步区分。给定 schema 集合，对于 N 种不同 predicate，以及头实体/尾实体两种情况，我们设计对应的共 2*N 种 B 标签，再合并 I 和 O 标签，故每个 token 一共有 (2*N+2) 个标签，如下图所示。

# 3. 操作流程

## 3.1. 训练阶段

## 3.2. 验证阶段


## 3.3. 测试阶段

## 3.4. 部署阶段



# 4. 项目总结
## 4.1. 项目陈述

## 4.2. 项目优势

## 4.3. 项目缺陷

## 4.4. 避坑指南

## 4.5. 注意事项


# 5. 参考信息
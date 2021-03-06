#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2022-07-12 14:08
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    load_data.py
# @Project: DuEE
# @Package: 
# @Ref:
import paddle
from utils import load_dict


class DuEventExtraction(paddle.io.Dataset):
    """DuEventExtraction"""

    def __init__(self, data_path, tag_path):
        # 加载触发词标签
        self.label_vocab = load_dict(tag_path)
        self.word_ids = []
        self.label_ids = []
        # 读取数据
        with open(data_path, 'r', encoding='utf-8') as fp:
            # skip the head line
            # 首行不是数据
            next(fp)
            for line in fp.readlines():
                # 按行遍历，窃取换行符，并按TAB分割
                words, labels = line.strip('\n').split('\t')
                # 原始数据是按照进行单个字之间分割的，这里获取一个query的列表
                words = words.split('\002')
                # 同理，对标签列也进行分割
                # TODO 目前没有搞懂 \002 原文是<0x02>具体指哪个字符串
                labels = labels.split('\002')
                # 将每一行的列表拼接到大列表上
                self.word_ids.append(words)
                self.label_ids.append(labels)
        # 获取当前字典值最大的，即为标签个数，记得加1，因为字典里是从0开始的
        self.label_num = max(self.label_vocab.values()) + 1

    def __len__(self):
        """
        获取纵的query个数
        :return:
        """
        return len(self.word_ids)

    def __getitem__(self, index):
        """
        根据索引获取某一行数据，及标签
        :param index:
        :return:
        """
        return self.word_ids[index], self.label_ids[index]


# 加载数据
train_ds = DuEventExtraction('/Users/geng/Documents/data/DuEE-fin/trigger/train.tsv', 'conf/DuEE-Fin/trigger_tag.dict')
dev_ds = DuEventExtraction('/Users/geng/Documents/data/DuEE-fin/trigger/dev.tsv', 'conf/DuEE-Fin/trigger_tag.dict')

count = 0
for text, label in train_ds:
    print(f"text: {text}; label: {label}")
    count += 1
    if count >= 3:
        break

"""
text: ['原', '标', '题', '：', '万', '讯', '自', '控', '(', '7', '.', '4', '9', '0', ',', '-', '0', '.', '1', '0', ',', '-', '1', '.', '3', '2', '%', ')', '：', '傅', '宇', '晨', '解', '除', '部', '分', '股', '份', '质', '押', '、', '累', '计', '质', '押', '比', '例', '为', '3', '9', '.', '5', '5', '%', '，', '，', '，', '，', '来', '源', '：', '每', '日', '经', '济', '新', '闻', '，', '每', '经', 'a', 'i', '快', '讯', '，', '万', '讯', '自', '控', '（', 's', 'z', '，', '3', '0', '0', '1', '1', '2', '，', '收', '盘', '价', '：', '7', '.', '4', '9', '元', '）', '6', '月', '3', '日', '下', '午', '发', '布', '公', '告', '称', '，', '公', '司', '接', '到', '股', '东', '傅', '宇', '晨', '的', '通', '知', '，', '获', '悉', '傅', '宇', '晨', '将', '其', '部', '分', '股', '份', '办', '理', '了', '质', '押', '业', '务', '。', '，', '截', '至', '本', '公', '告', '日', '，', '傅', '宇', '晨', '共', '持', '有', '公', '司', '股', '份', '5', '7', '9', '0', '.', '3', '8', '万', '股', '，', '占', '公', '司', '总', '股', '本', '的', '2', '0', '.', '2', '5', '%', '；', '累', '计', '质', '押', '股', '份', '2', '2', '9', '0', '万', '股', '，', '占', '傅', '宇', '晨', '持', '有', '公', '司', '股', '份', '总', '数', '的', '3', '9', '.', '5', '5', '%', '，', '占', '公', '司', '总', '股', '本', '的', '8', '.', '0', '1', '%', '。']; label: ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-质押', 'I-质押', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
text: ['客', '户', '端', '，', '新', '浪', '港', '股', '讯', '，', '众', '安', '集', '团', '(', '0', '.', '2', '4', '8', ',', '-', '0', '.', '0', '0', ',', '-', '0', '.', '8', '0', '%', ')', '（', '0', '0', '6', '7', '2', '.', 'h', 'k', '）', '发', '布', '公', '告', '，', '于', '2', '0', '1', '9', '年', '1', '0', '月', '1', '5', '日', '，', '公', '司', '耗', '资', '9', '4', '.', '5', '6', '万', '港', '元', '回', '购', '3', '8', '0', '.', '5', '万', '股', '，', '回', '购', '价', '格', '每', '股', '0', '.', '2', '4', '8', '-', '0', '.', '2', '4', '9', '港', '元', '。']; label: ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-股份回购', 'I-股份回购', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
text: ['原', '标', '题', '：', '金', '徽', '酒', '(', '6', '0', '3', '9', '1', '9', '.', 's', 'h', ')', '：', '亚', '特', '集', '团', '解', '除', '质', '押', '1', '9', '8', '0', '万', '股', '，', '，', '，', '，', '来', '源', '：', '格', '隆', '汇', '，', '格', '隆', '汇', '8', '月', '5', '日', '丨', '金', '徽', '酒', '(', '6', '0', '3', '9', '1', '9', '.', 's', 'h', ')', '公', '布', '，', '公', '司', '近', '日', '收', '到', '控', '股', '股', '东', '甘', '肃', '亚', '特', '投', '资', '集', '团', '有', '限', '公', '司', '(', '“', '亚', '特', '集', '团', '”', ')', '将', '其', '持', '有', '的', '公', '司', '部', '分', '股', '份', '解', '除', '质', '押', '的', '通', '知', '。', '，', '2', '0', '1', '8', '年', '4', '月', '9', '日', '，', '亚', '特', '集', '团', '将', '其', '持', '有', '的', '公', '司', '5', '9', '8', '0', '万', '股', '有', '限', '售', '条', '件', '股', '份', '质', '押', '给', '兰', '州', '银', '行', '股', '份', '有', '限', '公', '司', '陇', '南', '分', '行', '。']; label: ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-解除质押', 'I-解除质押', 'I-解除质押', 'I-解除质押', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
"""
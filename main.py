import jieba
from gensim import corpora, models, similarities
import re
import sys
import os


def remove_punctuation(string):
    # 删除标点符号,然后进行结巴分词
    rule = re.compile(u"[^a-zA-Z0-9\u4e00-\u9fa5]")
    string = rule.sub('', string)
    res = jieba.lcut(string)
    return res

# 将文章分句，
def split_sentence(text):
    head = '\u4e00'
    tail = '\u9fa5'
    word = ""
    sentences = []  # 把拆分的句子保存下来
    for each in range(len(text)):
        if head <= text[each] <= tail:  # 中文编码范围
            word += text[each]
        elif text[each] == "，":  
            # 如果是逗号，将句子push，然后将word清空
            sentences.append(word)
            word = ""
        else:
            continue
    if word != '':
        sentences.append(word)
        word = ''

    return sentences

def split_words(text):
    # 利用jieba.luct进行分词，并将其保存在list列表中
    list = [[word for word in jieba.lcut(sentence)] for sentence in text];
    print(list)
    return list

def calc_Similiarity(origin_txt,to_check_txt):
    sim_value = []
    word_lenth = []
    total_sum = 0
    total_size = 0
    ori_list = split_words(origin_txt)
    ori_add_list = split_words(to_check_txt)
    # 生成词典
    dictionary = corpora.Dictionary(ori_list)
    # 通过doc2bow稀疏向量生成语料库
    corpus = [dictionary.doc2bow(word) for word in ori_list]
    # 通过TF模型算法，计算出tf值
    tf = models.TfidfModel(corpus)
    # 通过token2id得到特征数（字典里面键的个数）
    num_features = len(dictionary.token2id.keys())
    # 计算稀疏矩阵相似度，并建立索引
    index = similarities.MatrixSimilarity(tf[corpus], num_features=num_features)
    # 每句长度-单个变量
    word_size = 0
    size = 0
    sim = 0
    for word in range(len(ori_add_list)):
        # 新的稀疏向量
        new_vector = dictionary.doc2bow(ori_add_list[word])
        # 算出文章的相似度
        sim_list = index[tf[new_vector]]
        # 选出最大相似度
        sim = max(sim_list)
        # 加入相似度列表
        sim_value.append(sim)
        # 相似文章每句长度值
        word_size = len(ori_add_list[word])
        # 文章总长度值
        size += word_size
        # 加入长度列表
        word_lenth.append(word_size)
    total_size = size
    for i in range(len(word_lenth)):
        total_sum += word_lenth[i] * sim_value[i]

    # 加权求平均
    ans = total_sum / total_size

    return ans



def get_contents(path):
    string = ''
    f = open(path, 'r', encoding='UTF-8')
    line = f.readline()
    while(line):
        string = string + line
        line = f.readline()
    f.close()
    return string


def test(orig_path, check_path):
    if not os.path.exists(orig_path):
        print("论文原文文件不存在！")
        exit()
    if not os.path.exists(check_path):
        print("抄袭版论文文件不存在！")
        exit()

    str1 = get_contents(orig_path)
    str2 = get_contents(check_path)

    text1 = remove_punctuation(str1)
    text2 = remove_punctuation(str2)

    similarity = calc_similarity(text1, text2)
    # 转化为float，再取小数点后两位
    res = round(similarity.item(), 2)
    return res


if __name__ == '__main__':
    try:
        orig_path, check_path, save_path = sys.argv[1:4]
    except Exception as e:
        print(e)
    similarity = test(orig_path, check_path)
    print("文章的相似度为： %.4f" % similarity)
    f = open(save_path, 'w', encoding="UTF-8")
    f.write("文章的相似度为： %.4f" % similarity)
    f.close()

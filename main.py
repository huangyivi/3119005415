import jieba
from gensim import corpora
from gensim.similarities import Similarity
import re
import sys
import os


def remove_punctuation(string):
    # 删除标点符号,然后进行结巴分词
    rule = re.compile(u"[^a-zA-Z0-9\u4e00-\u9fa5]")
    string = rule.sub('', string)
    res = jieba.lcut(string)
    return res


def calc_similarity(origin, toCheck):
    texts = [origin, toCheck]
    dictionary = corpora.Dictionary(texts)
    # 获取词语库
    corpus = [dictionary.doc2bow(text) for text in texts]
    # j计算余弦相似度
    similarity = Similarity('-Similarity-index', corpus,
                            num_features=len(dictionary))
    test_corpus_1 = dictionary.doc2bow(origin)
    cos_sim = similarity[test_corpus_1][1]
    return cos_sim


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

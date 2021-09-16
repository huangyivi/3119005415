import unittest
from main import get_contents, split_sentence, calc_similiarity


class Test(unittest.TestCase):
    def test_add(self):
        str1 = get_contents(".\\test1\orig.txt")
        str2 = get_contents(".\\test1\orig_0.8_add.txt")

        text1 = split_sentence(str1)
        text2 = split_sentence(str2)

        similarity = calc_similiarity(text1, text2)
        # 转化为float，再取小数点后两位
        res = round(similarity.item(), 2)
        print('测试文本1：orig_0.8_add.txt的查重结果为：', res)

    def test_del(self):
        str1 = get_contents(".\\test1\orig.txt")
        str2 = get_contents(".\\test1\orig_0.8_del.txt")

        text1 = split_sentence(str1)
        text2 = split_sentence(str2)

        similarity = calc_similiarity(text1, text2)
        # 转化为float，再取小数点后两位
        res = round(similarity.item(), 2)
        print('测试文本1：orig_0.8_del.txt的查重结果为：', res)

    def test_dis_1(self):
        str1 = get_contents(".\\test1\orig.txt")
        str2 = get_contents(".\\test1\orig_0.8_dis_1.txt")

        text1 = split_sentence(str1)
        text2 = split_sentence(str2)

        similarity = calc_similiarity(text1, text2)
        # 转化为float，再取小数点后两位
        res = round(similarity.item(), 2)
        print('测试文本1：orig_0.8_dis_1.txt的查重结果为：', res)

    def test_dis_10(self):
        str1 = get_contents(".\\test1\orig.txt")
        str2 = get_contents(".\\test1\orig_0.8_dis_10.txt")

        text1 = split_sentence(str1)
        text2 = split_sentence(str2)

        similarity = calc_similiarity(text1, text2)
        # 转化为float，再取小数点后两位
        res = round(similarity.item(), 2)
        print('测试文本1：orig_0.8_dis_10.txt的查重结果为：', res)

    def test_dis_15(self):
        str1 = get_contents(".\\test1\orig.txt")
        str2 = get_contents(".\\test1\orig_0.8_dis_15.txt")

        text1 = split_sentence(str1)
        text2 = split_sentence(str2)

        similarity = calc_similiarity(text1, text2)
        # 转化为float，再取小数点后两位
        res = round(similarity.item(), 2)
        print('测试文本1：orig_0.8_dis_15.txt的查重结果为：', res)


    # 以下为测试文本2

    # def test_add_2(self):
    #     str1 = get_contents(".\\test2\orig.txt")
    #     str2 = get_contents(".\\test2\orig_0.8_add.txt")
    #
    #     text1 = split_sentence(str1)
    #     text2 = split_sentence(str2)
    #
    #     similarity = calc_similiarity(text1, text2)
    #     # 转化为float，再取小数点后两位
    #     res = round(similarity.item(), 2)
    #     print('测试文本2：orig_0.8_add.txt的查重结果为：', res)
    #
    # def test_del_2(self):
    #     str1 = get_contents(".\\test2\orig.txt")
    #     str2 = get_contents(".\\test2\orig_0.8_del.txt")
    #
    #     text1 = split_sentence(str1)
    #     text2 = split_sentence(str2)
    #
    #     similarity = calc_similiarity(text1, text2)
    #     # 转化为float，再取小数点后两位
    #     res = round(similarity.item(), 2)
    #     print('测试文本2：orig_0.8_del.txt的查重结果为：', res)
    #
    # def test_dis_1_2(self):
    #     str1 = get_contents(".\\test2\orig.txt")
    #     str2 = get_contents(".\\test2\orig_0.8_dis_1.txt")
    #
    #     text1 = split_sentence(str1)
    #     text2 = split_sentence(str2)
    #
    #     similarity = calc_similiarity(text1, text2)
    #     # 转化为float，再取小数点后两位
    #     res = round(similarity.item(), 2)
    #     print('测试文本2：orig_0.8_dis_1.txt的查重结果为：', res)
    #
    # def test_dis_10_2(self):
    #     str1 = get_contents(".\\test2\orig.txt")
    #     str2 = get_contents(".\\test2\orig_0.8_dis_10.txt")
    #
    #     text1 = split_sentence(str1)
    #     text2 = split_sentence(str2)
    #
    #     similarity = calc_similiarity(text1, text2)
    #     # 转化为float，再取小数点后两位
    #     res = round(similarity.item(), 2)
    #     print('测试文本2：orig_0.8_dis_10.txt的查重结果为：', res)
    #
    # def test_dis_15_2(self):
    #     str1 = get_contents(".\\test2\orig.txt")
    #     str2 = get_contents(".\\test2\orig_0.8_dis_15.txt")
    #
    #     text1 = split_sentence(str1)
    #     text2 = split_sentence(str2)
    #
    #     similarity = calc_similiarity(text1, text2)
    #     # 转化为float，再取小数点后两位
    #     res = round(similarity.item(), 2)
    #     print('测试文本2：orig_0.8_dis_15.txt的查重结果为：', res)



if __name__ == '__main__':
    unittest.main()

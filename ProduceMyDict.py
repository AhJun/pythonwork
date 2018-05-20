import re

strs = open(r'C:/Users/myl/Desktop/SegChineseToWords/英汉词典TXT格式.txt','r',encoding='utf-8').readlines()

for str in strs:

# 形容词典
    adj_re = re.search('adj', str)
    if adj_re != None:
        adj_num = adj_re.end()+1
        adj_str = str[adj_num:]
        adj_list = re.findall("[\u4e00-\u9fa5]+", adj_str)
        for ele_adj in adj_list:
            ele_adj = ele_adj + '\n'
            with open(r'C:/Users/myl/Desktop/SegChineseToWords/Dict/adj_dict.txt', 'a+',encoding='utf-8') as f:
                f.write(ele_adj)


# 副词典
    adv_re = re.search('adv', str)
    if adv_re != None:
        adv_num = adv_re.end()+1
        adv_str = str[adv_num:]
        adv_list = re.findall("[\u4e00-\u9fa5]+", adv_str)
        for ele_adv in adv_list:
            ele_adv = ele_adv + '\n'
            with open(r'C:/Users/myl/Desktop/SegChineseToWords/Dict/adv_dict.txt', 'a+',encoding='utf-8') as f:
                f.write(ele_adv)

# 名词词典
    n_re = re.search('n', str)
    if n_re != None:
        n_num = n_re.end() + 1
        n_str = str[n_num:]
        n_list = re.findall("[\u4e00-\u9fa5]+", n_str)
        for ele_n in n_list:
            ele_n = ele_n + '\n'
            with open(r'C:/Users/myl/Desktop/SegChineseToWords/Dict/n_dict.txt', 'a+', encoding='utf-8') as f:
                f.write(ele_n)


# 动词词典
    v_re = re.search('v', str)
    if v_re != None:
        v_num = v_re.end() + 1
        v_str = str[v_num:]
        v_list = re.findall("[\u4e00-\u9fa5]+", v_str)
        for ele_v in v_list:
            ele_v = ele_v + '\n'
            with open(r'C:/Users/myl/Desktop/SegChineseToWords/Dict/v_dict.txt', 'a+', encoding='utf-8') as f:
                f.write(ele_v)


# 介词词典
    prep_re = re.search('prep', str)
    if prep_re != None:
        prep_num = prep_re.end() + 1
        prep_str = str[prep_num:]
        prep_list = re.findall("[\u4e00-\u9fa5]+", prep_str)
        for ele_prep in prep_list:
            ele_prep = ele_prep + '\n'
            with open(r'C:/Users/myl/Desktop/SegChineseToWords/Dict/prep_dict.txt', 'a+', encoding='utf-8') as f:
                f.write(ele_prep)

# 代词词典
    pron_re = re.search('pron', str)
    if pron_re != None:
        pron_num = pron_re.end() + 1
        pron_str = str[pron_num:]
        pron_list = re.findall("[\u4e00-\u9fa5]+", pron_str)
        for ele_pron in pron_list:
            ele_pron = ele_pron + '\n'
            with open(r'C:/Users/myl/Desktop/SegChineseToWords/Dict/pron_dict.txt', 'a+', encoding='utf-8') as f:
                f.write(ele_pron)











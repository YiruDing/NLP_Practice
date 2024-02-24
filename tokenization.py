import jieba
import re

text = '''台风凤仙（英語：Typhoon Pongsona，国际编号：0226，联合台风警报中心：31W）是2002年太平洋台风季期间的最后一场台风[注 1]，也是2002年对美国造成损失第二大的自然灾害，仅次于飓风丽丽[2]。其名称由朝鲜民主主义人民共和国提供，在朝鲜语中意为“鳳仙花”[3]。系统源于12月2日的一片扰动天气区，接下来逐渐增强，于12月5日达到台风强度。12月8日，风暴以10分钟持续风速每小时175公里强度从关岛和北马里亚纳群岛经过，最终转向东北并减弱，于12月11日转变成温带气旋。 台风凤仙产生的强烈阵风最高时速达278公里，导致关岛全部停电，还有约1300套房屋被毁。由于建筑标准过硬，并且积累有多场台风来袭的经验，岛上没有人员直接因风暴丧生，但飞溅的碎玻璃导致一人遇难，属台风的间接伤亡。关岛共计遭受了超过7亿美元（2002年美元，相当于2024年的11.4億美元）损失，凤仙因此成为该岛有纪录以来造成损失最惨重的5场台风之一。罗塔岛和北马里亚纳群岛其他地区也受到风暴重创，其名称“凤仙”因此退役，今后永不于太平洋台风命名时采用。新名字由紅霞取代。"
'''
# Normalization and cleaning
text = text.lower()
punctuation_marks = re.compile(r'[^\w\s]') 
clean_text = ""
for char in text:
    if not punctuation_marks.match(char) and not char.isdigit() and char !=' ':
        clean_text += char

# Tokenization and calculate the frequency
def token_frequency(clean_text):
    tokens = jieba.lcut(clean_text)  # Tokenize the text with jieba
    frequency = {} 
    for token in tokens:
        if token in frequency:
            frequency[token] += 1
        else:
            frequency[token] = 1
    return frequency

frequency = token_frequency(clean_text)

# Sort the tokens by frequency in descending order
sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

print("Tokens with frequencies (descending order):")
for token, freq in sorted_frequency:
    print(f"{token}: {freq}")

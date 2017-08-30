import operator

def count_tags(file_name):
    with open(file_name, encoding='utf-8') as f:
        content = f.readlines()

    tag_dict = dict()
    for idx, line in enumerate(content):
        if line.startswith('  - '):
            str = line[len('  - '):]
            if str in tag_dict:
                tag_dict[str] += 1
            else:
                tag_dict[str] = 1

    print(len(tag_dict), " number of distinct tags")
    sorted_tag_dict = sorted(tag_dict.items(), key=operator.itemgetter(1), reverse=True)
    for k, v in sorted_tag_dict:
        print(k.strip(), v)
    
    
if __name__ == '__main__':
    file_name = '..\\output\\out_2003_mod.yml'
    count_tags(file_name)
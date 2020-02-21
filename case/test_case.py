import os

def main():
    # 当前项目路径
    base_dir = os.path.dirname(os.path.abspath('.'))
    # 图片路径
    file_name = os.path.join(base_dir, 'report', 'first_case.html')
    print("file_name :%s" % file_name)
    for i in range(1,10):
        print(i)

if __name__ == '__main__':
    main()
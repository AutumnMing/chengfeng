import csv


def create_csv(filename: str, column_names: [str]):
    """
    创建csv文件, 并且写入列名称
    :param filename:
    :param column_names:
    :return:
    """
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=column_names)
        writer.writeheader()


def add_dict_rows(filename: str, dict_data: dict, column_names: [str]):
    """
    追加型写入数据到csv文件
    :param filename:文件名称, 需要以.csv结尾, 例如 example.csv
    :param dict_data:字典形式的数据
    :param column_names:列名称, 列表形式
    :return:
    """
    with open(filename, 'a+', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=column_names)
        writer.writerow(dict_data)

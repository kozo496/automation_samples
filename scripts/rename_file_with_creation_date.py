# ファイルから作成日の情報を取り出して、'yymmdd'の形式でファイル名の最初につける

import os
from datetime import datetime
from glob import glob

def get_dateStr(path: str, system_type='unix'):
    # pathからファイル作成日をyymmddの形式で返す。
    if system_type=='unix':
        c_timestamp = os.stat(path).st_birthtime
    else:
        c_timestamp = os.path.getctime(path)    # for Windows PC

    dt = datetime.fromtimestamp(c_timestamp)
    date_str = datetime.strftime(dt, '%y%m%d')

    return date_str


def rm_cdate(path: str):
    # pathのファイル名を冒頭に作成日を付加して変更する。
    data_str = get_dateStr(path)
    rm_file_name = f"{data_str}_{os.path.basename(path)}"
    rm_path = os.path.join(os.path.dirname(path), rm_file_name)
    os.rename(path, rm_path)


if __name__ == '__main__':
    path_list = glob('*.md')
    for path in path_list:
        rm_cdate(path)
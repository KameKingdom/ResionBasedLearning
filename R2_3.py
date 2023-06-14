import zipfile

total_sum = 0

with zipfile.ZipFile('sample.zip', 'r') as zip_file:

    for file_name in zip_file.namelist():
        if "kitamura" in file_name:
            if int(file_name.split('_')[1]) % 2 != 0:
                with zip_file.open(file_name, 'r') as file:
                    contents = file.read()
                    print(contents)
                    number = int(contents.strip())
                    print(number)
                    total_sum += number

    # 合計を出力する
    print("奇数のファイルの数字の合計:", total_sum)

import json
import os
with open('purchase_log.txt', 'r') as purchase_log:
    for i, b in enumerate(purchase_log):
        if i >= 1:  # пропуск строки
            purchase_log_json_format = json.loads(b)  # здесь создаю словарь
            user_id, category = purchase_log_json_format['user_id'], purchase_log_json_format['category']  # пишу значения в переменные
            purchase_log_new_dict = {user_id: category}  # переношу переменные в словарь
            with open('purchase_log_new_version.txt', 'a') as purchase_log_new_txt:
                purchase_log_new_txt.write(str(purchase_log_new_dict) + '\n')
    old_name, new_name = 'purchase_log.txt', 'purchase_log_new_version.txt'  # избавляюсь от старой версии файла
    os.replace(new_name, old_name)

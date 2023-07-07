import pandas as pd


def split_excel_by_f_column(file_path):
    try:
        # Открываем исходный файл
        df = pd.read_excel(file_path)
        # print(df.columns)
        # print(df.columns[5])

        # Собираем группы строк по уникальным значениям в столбце F
        groups = df.groupby(df.columns[5])

        # Для каждой группы создаем отдельный файл
        for group_name, group_df in groups:
            filename = f"{str(group_name)}.xlsx"
            group_df.to_excel(str(filename), index=False)
            print(f"Создан файл {str(filename)} со строками по {str(group_name)}")
    except Exception as error:
        print("Error: " + str(error))


# Пример вызова функции
split_excel_by_f_column('file.xlsx')
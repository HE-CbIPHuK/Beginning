import os
from hw7.task5 import merge_sorted_files


def test_merge_sorted_files():
        for i in range(1, 4):  # create files and fill content for the test
            with open(f'5_{i}.txt', 'w+') as f:
                f.writelines([f'{1 * i}\n', f'{100 * i}\n', f'{10 * i}\n'])
        assert list(merge_sorted_files(['5_1.txt', '5_2.txt', '5_3.txt'])) == [1, 2, 3, 10, 20, 30, 100, 200, 300]  # compare
        for j in range(1, 4):  # delete used files
            os.remove(f"5_{j}.txt")

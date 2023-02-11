from script_entrance_lottery import script_entrance_lottery
from script_entrance_exercise import script_entrance_exercise
from mouse_move_test import mouse_move_test
from mouse_test import mouse_test
from script_entrance_start_and_stop import script_entrance_start_and_stop
from script_entrance_shutdown import script_entrance_shutdown

if __name__ == '__main__':
    print("1 启动锻炼脚本")
    print("2 启动进退程序脚本")
    print("3 启动获取鼠标位置脚本")
    print("4 启动鼠标测试脚本")
    print("5 启动抽奖脚本")
    print("6 启动关机任务脚本")

    select_type = int(input("请选择："))
    if select_type == 1:
        script_entrance_exercise()
    if select_type == 2:
        script_entrance_start_and_stop()
    if select_type == 3:
        mouse_test()
    if select_type == 4:
        mouse_move_test()
    if select_type == 5:
        script_entrance_lottery()
    if select_type == 6:
        script_entrance_shutdown()


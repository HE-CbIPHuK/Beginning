from hw6.task1 import User


def test_get_created_instances():  # testing the first created method
    assert User.get_created_instances() == 0
    user_1, user_2, user_3 = User(), User(), User()
    assert user_1.get_created_instances() == 3


def test_reset_instances_counter():  # testing the reset method
    assert User.reset_instances_counter() == 3
    assert User.get_created_instances() == 0
from main import Solution, create_linked_list


def test():
    # Пример 1 связанный список нечетной длинны
    # конечное положение указателей из алгоритма Флойда:
    # s - slow, f - fast
    #
    #     s
    # 1 2 3 4 5
    #         f
    values = [1, 2, 3, 4, 5]
    linked_list = create_linked_list(values=values)
    solution = Solution()
    middle_node = solution.middleNode(linked_list.head)
    assert middle_node.val == 3

    # Пример 2 связанный список четной длинны
    # конечное положение указателей из алгоритма Флойда:
    # s - slow, f - fast
    #
    #       s
    # 1 2 3 4 5 6
    #           f
    values = [1, 2, 3, 4, 5, 6]
    linked_list = create_linked_list(values=values)
    solution = Solution()
    middle_node = solution.middleNode(linked_list.head)
    assert middle_node.val == 4

    # Тест связанный список из одного элемента
    # конечное положение указателей из алгоритма Флойда:
    # s - slow, f - fast
    #
    # s
    # 1
    # f
    values = [1]
    linked_list = create_linked_list(values=values)
    solution = Solution()
    middle_node = solution.middleNode(linked_list.head)
    assert middle_node.val == 1

    # Тест связанный список из 100 элементов
    # конечное положение указателей из алгоритма Флойда:
    # s - slow, f - fast
    #
    #              s
    # 1 2 3 ... 50 51 ... 99 100 
    #                         f
    
    values = list(range(1, 101))  # [1, ..., 100]
    linked_list = create_linked_list(values=values)
    solution = Solution()
    middle_node = solution.middleNode(linked_list.head)
    assert middle_node.val == 51


if __name__ == "__main__":
    test()

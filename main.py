from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class ListNode:
    """Класс реализующий ноду односвязного списка."""

    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self) -> str:
        return f"val: {self.val}, next: {self.next}"


class LinkedList:
    """Класс реализующий односвязный список с head, tail и len."""

    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def add_node(self, list_node: ListNode):
        """Добавляет ноду list_node в конец связанного списка.

        Args:
            list_node (ListNode): нода, которую мы хотим добавить
            в односвязный список.
        """
        if self.head is None:
            self.head = list_node
            self.tail = list_node
            self.len = 1
        else:
            self.tail.next = list_node
            self.tail = list_node
            self.len += 1

    def __str__(self):
        """Возвращает строковое представление связанного списка,
        всех нод, которые в нем есть.
        Ограничение по выводу на количество нод в списке корректно
        обрабатывает связанные списки с циклами.

        Returns:
            str: строковое представление односвязного списка.
        """
        current_node = self.head
        linked_list_values = []

        # у нас может быть LinkedList с циклом, чтобы метод не попал в
        # бесконечный цикл мы будет выводить строго все ноды по их
        # количеству в односвязном списке
        for i in range(self.len):
            linked_list_values.append(current_node.val)
            current_node = current_node.next

        return " -> ".join(str(node_value) for node_value in linked_list_values)


def create_linked_list(values: list[int]) -> LinkedList:
    """Создает linked list, согласно условию задачи.
    Используется для создания тестовых данных для решения.

    Args:
        values (list[int]): массив значений, который будут записаны в узлы списка.

    Returns:
        LinkedList: односвязный список
    """
    linked_list = LinkedList()

    for value in values:
        node = ListNode(value)
        linked_list.add_node(node)

    return linked_list


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Функция находит ноду являющейся серединой у связанного списка.

        Если длинна связанного списка:
        - нечетная, то вернет середину списка
        - четная, вернет первый элемент второй половины связанного списка

        Реализует алгоритм Флойда с slow и fast указателями, подвид паттерна
        two pointers.

        Временная сложность: O(n) -пробегаем по всем нодам связанного списка
        Пространственная сложность: O(1) - расходы на 2 указателя

        Args:
            head (Optional[ListNode]): односвязный список с нодами ListNode

        Returns:
            Optional[ListNode]: нода, являющаяся серединой односвязного списка.
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


if __name__ == "__main__":
    list_values = list(map(int, input().split()))
    linked_list = create_linked_list(values=list_values)

    solution = Solution()
    middle_node = solution.middleNode(linked_list.head)
    print(middle_node.val)

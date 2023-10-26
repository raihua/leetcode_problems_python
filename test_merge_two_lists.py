import pytest
from ListNode import ListNode
from merge_two_lists_21 import mergeTwoLists

@pytest.fixture
def list1():
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    return list1

@pytest.fixture
def list2():
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    return list2

def compare_linked_lists(list1, list2):
    while list1 and list2:
        if list1.val != list2.val:
            return False
        list1 = list1.next
        list2 = list2.next
    # If both lists are empty, return True
    return list1 is None and list2 is None

def test_merge_two_lists(list1, list2):
    result = mergeTwoLists(list1, list2)
    expected = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4))))))
    assert compare_linked_lists(result, expected)

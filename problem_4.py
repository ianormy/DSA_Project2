"""
Active Directory

In Windows Active Directory, a group can consist of user(s) and group(s) themselves.
"""
import unittest


class Group(object):
    def __init__(self, name):
        if name is None:
            raise ValueError("name cannot be None")
        if len(name) == 0:
            raise ValueError("name cannot be empty")
        self.name = name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    # first look to see if it's in the current group
    for group_user in group.get_users():
        if group_user == user:
            return True
    for subgroup in group.get_groups():
        if is_user_in_group(user, subgroup):
            return True
    return False


class ActiveDirectoryTestCase(unittest.TestCase):
    def test_valid_data(self):
        parent = Group("parent")
        child1 = Group("child1")
        child2 = Group("child2")
        sub_child = Group("subchild")
        sub_child_user = "donald duck"
        sub_child.add_user(sub_child_user)
        child1.add_group(sub_child)
        parent.add_group(child1)
        parent.add_group(child2)
        self.assertTrue(is_user_in_group(sub_child_user, parent))
        self.assertFalse(is_user_in_group("daffy duck", parent))
        self.assertFalse(is_user_in_group(sub_child_user, child2))

    def test_invalid_group_name(self):
        with self.assertRaises(ValueError):
            Group(None)

    def test_empty_group_name(self):
        with self.assertRaises(ValueError):
            Group('')


if __name__ == '__main__':
    unittest.main()

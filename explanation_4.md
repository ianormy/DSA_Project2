# Active Directory
To determine if a user is in a group I have used a recursive function.

## Time Analysis
**get users** - O(1)

**add user** - O(1)

**get groups** - O(1)

**add group** - O(1)

### is_user_in_group
Let m denote the number of groups and n denote the number of users then:
Worst case search time is: O(m*n)


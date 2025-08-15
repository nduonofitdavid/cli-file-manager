
- Make sorting by extension work with nested folders, that is make the program recursive so that if it finds something that does not match a file, that will likely be a folder, then it should move into that folder, then fall the function that will sort that folder also.

- Make this feature also work when sorting by date.

# Undo Operations

- Can we load the contents of the jsonl file into a stack, and then pop each operation one by one, and then perform that operation. But what if those directories dont exist again, do I create those directories? or do I skip that file, and then log the message into a log files that says, this operation could not be performed, citing the reason whythe program was not able to perform that operation.



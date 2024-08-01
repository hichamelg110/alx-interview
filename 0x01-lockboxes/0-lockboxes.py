#!/usr/bin/python3
"""
Solve the locked boxes problem
"""

def can_unlock_all(boxes):
    """
    Check if all boxes can be opened
    """
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False
    
    keys = set(boxes[0])
    opened = {0}
    
    for i in range(len(boxes)):
        if i in keys:
            opened.add(i)
            keys.update(boxes[i])
    
    return len(opened) == len(boxes)

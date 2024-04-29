#!/usr/bin/python3

""" Module for lockboxes """


def canUnlockAll(boxes):
    """ Checks if lockboxes can be opened """
    n = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        box_idx = unseen_boxes.pop()
        if not box_idx or box_idx >= n or box_idx < 0:
            continue

        if box_idx not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[box_idx])
            seen_boxes.add(box_idx)

    return n == len(seen_boxes)

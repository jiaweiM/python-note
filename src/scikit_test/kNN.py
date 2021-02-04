import numpy as np
import operator


def create_dataset():
    group = np.array([[1.0, 1.1], [1., 1.], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0(inx, dataset, labels, k):
    """
    inx,
    """
    dataset_size = dataset.shape[0]
    diff_mat = np.tile(inx, (dataset_size, 1)) - dataset
    sq_diff_mat = diff_mat ** 2
    sq_distances = sq_diff_mat.sum(axis=1)
    distances = sq_distances ** 0.5
    sorted_dist_indices = distances.argsort()
    class_count = {}
    for i in range(k):
        votei_label = labels[sorted_dist_indices[i]]



group, labels = create_dataset()
print(group)
print(labels)

import csv
import argparse

header = []

def class_counts(data):
    counts = {}
    for datum in data:
        label = datum[-1]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts


def is_numeric(value):
    if isinstance(value, str):
        return False
    else:
        return True


def info_gained_from_split(left, right, uncertainty):
    p = float(len(left)) / (len(left) + len(right))
    return uncertainty - p * calculate_gini_impurity(left) - (1 - p) * calculate_gini_impurity(right)


class Decision:
    def __init__(self, column, value):
        self.column = column
        self.value = value

    def match(self, example):
        val = example[self.column]
        if is_numeric(val):
            return val >= self.value
        else:
            return val == self.value

    #Borrowed from the tutorial to help print the Tree

    def __repr__(self):

        condition = "=="
        if is_numeric(self.value):
            condition = ">="
        return "Is %s %s %s?" % (
            header[self.column], condition, str(self.value))


class Leaf:
    def __init__(self, data):
        self.predictions = class_counts(data)


def split_data_on_decision(data, decision):
    true_rows, false_rows = [], []
    for datum in data:
        if decision.match(datum):
            true_rows.append(datum)
        else:
            false_rows.append(datum)

    return true_rows, false_rows


def calculate_gini_impurity(data):
    counts = class_counts(data) 
    impurity = 1
    for lbl in counts:
        prob_of_lbl = counts[lbl] / float(len(data))
        impurity -= prob_of_lbl**2
    return impurity


def get_best_split_criteria(data):
    best_gain = 0
    best_decision = None
    current_uncertainty = calculate_gini_impurity(data)
    n_features = len(data[0]) - 1
    for column in range(n_features):
        values = set([row[column] for row in data])
        for val in values:
            decision = Decision(column, val)
            true_rows, false_rows = split_data_on_decision(data, decision)

            if len(true_rows) == 0 or len(false_rows) == 0:
                continue
            gain = info_gained_from_split(true_rows, false_rows, current_uncertainty)

            if gain >= best_gain:
                best_gain, best_decision = gain, decision
    return best_gain, best_decision


class TreeNode:

    def __init__(self, decision, true_branch, false_branch):
        self.question = decision
        self.true_branch = true_branch
        self.false_branch = false_branch


def make_tree(dataset):
    info_gain, decision = get_best_split_criteria(dataset)
    if info_gain == 0:
        return Leaf(dataset)

    true_rows, false_rows = split_data_on_decision(dataset, decision)

    true_branch = make_tree(true_rows)

    false_branch = make_tree(false_rows)

    return TreeNode(decision, true_branch, false_branch)


def print_tree(node, spacing=""):
    """This print_tree function is borrowed from 
    a Google tutorial, see README"""

    if isinstance(node, Leaf):
        print(spacing + "Predict", node.predictions)
        return

    print(spacing + str(node.question))

    print(spacing + '--> True:')
    print_tree(node.true_branch, spacing + "  ")

    print(spacing + '--> False:')
    print_tree(node.false_branch, spacing + "  ")


def process_data(cvs_file, attributes):
    global header
    print("Processing ", cvs_file)
    columns = map(int, attributes.split(','))
    columns = map(lambda x: x - 1, columns)
    columns = set(columns)
    dataset = []
    modified_row = []
    with open(cvs_file) as cvsfile:
        filereader = csv.reader(cvsfile, delimiter=',')
        for row in filereader:
            for i in range(len(row)):
                if i in columns:
                    field = row[i]
                    try:
                        field = float(field)
                    except ValueError:
                        field = field
                    modified_row.append(field)
            modified_row.append(row[len(row)-1])
            dataset.append(modified_row)
            modified_row = []
    header = dataset.pop(0)
    print("With attributes ", header)
    return dataset


def main():
    parser = argparse.ArgumentParser(
        description='Create a decision tree from a CSV file.')
    parser.add_argument('csv_file', help='the CSV file to be processed')
    parser.add_argument(
        'attributes', help='the list of attributes for selection, excluding class label')
    args = parser.parse_args()
    dataset = process_data(args.csv_file, args.attributes)
    tree = make_tree(dataset)
    print_tree(tree)

main()

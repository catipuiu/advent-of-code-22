import sys


class File:
    def __init__(self, name, parent=None, size=None, is_dir=False):
        self.name = name
        self.size = size
        self.is_dir = is_dir

        if name == "/":
            self.parent = self
        else:
            self.parent = parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def get_child(self, name):
        for child in self.children:
            if child.name == name:
                return child


def display_tree(file, depth=0):
    print(4 * depth * " ", file.name, end="")

    if file.is_dir:
        print(" (dir, total=%r)" % file.size)
    else:
        print(" (size=%d)" % file.size)

    for c in file.children:
        display_tree(c, depth + 1)


def compute_totals(file):
    if not file.is_dir:
        return file.size

    current_total = 0
    for child in file.children:
        current_total += compute_totals(child)
    file.size = current_total
    return current_total


ans = 0


def compute_sol(file):
    global ans

    if file.is_dir and file.size <= 100_000:
        ans += file.size

    for child in file.children:
        compute_sol(child)


root = File("/", is_dir=True)
assert root.parent == root
assert root.parent.parent.parent == root

current_dir = root


for line in sys.stdin:
    parts = line.strip().split(" ")
    if line[0] == "$":  # procesam o comanda, alternativ: line.startswith('$')
        # cd sau dir
        print("Parts: %r" % parts)

        cmd = parts[1]
        if cmd == "cd":
            target = parts[2]

            if target == "/":
                current_dir = root
            elif target == "..":
                current_dir = current_dir.parent
            else:
                target_dir = current_dir.get_child(target)
                if target_dir == None:
                    print(
                        "Nu am gasit directorul %r in %r" % (target, current_dir.name)
                    )
                    continue
                current_dir = target_dir
                print("Am intrat in directorul %r" % current_dir.name)
    else:  # procesam outputul unui `ls`
        size_or_dir, name = parts[0], parts[1]

        if size_or_dir == "dir":
            print("Am gasit in director cu numele %s" % name)
            file = File(name, parent=current_dir, is_dir=True)
        else:
            size = int(size_or_dir)
            print(
                "Am gasit un fisier normal cu numele %s si dimensiunea %d"
                % (name, size)
            )
            file = File(name, parent=current_dir, size=size)

        current_dir.add_child(file)

    # print("line: %r" % line.strip())


display_tree(root)
compute_totals(root)
print("\n")
display_tree(root)

compute_sol(root)

print("answer is: %d" % ans)

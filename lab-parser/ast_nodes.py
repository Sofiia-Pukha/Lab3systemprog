# Вузол абстрактного синтаксичного дерева (AST)


class Node:
    def __init__(self, kind, children=None, value=None, line=0):
        self.kind = kind
        self.children = children if children is not None else []
        self.value = value
        self.line = line

    def value_str(self):
        if self.value is None:
            return ''
        if isinstance(self.value, tuple):
            return ' '.join(self.value)
        if self.kind == 'printf':
            return '"' + self.value.replace('\n', '\\n') + '"'
        return str(self.value)

    def label(self):
        v = self.value_str()
        return f'{self.kind} {v}' if v else self.kind

    def print_tree(self, prefix='', is_last=True, is_root=True):
        if is_root:
            print(self.label())
        else:
            print(prefix + ('└── ' if is_last else '├── ') + self.label())
            prefix += '    ' if is_last else '│   '
        for i, child in enumerate(self.children):
            child.print_tree(prefix, i == len(self.children) - 1, False)

    def to_dict(self):
        return {
            'name': self.kind,
            'value': self.value_str(),
            'line': self.line,
            'children': [c.to_dict() for c in self.children],
        }

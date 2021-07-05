from dataclasses import dataclass
from typing import Generic, Set, TypeVar, List, Optional, Iterator

T = TypeVar('T')


@dataclass
class TrieNode(Generic[T]):
    data: T
    children: Set['TrieNode[T]'] = None
    # parent: 'TrieNode[T]' = None

    def __hash__(self):
        return hash(self.data)

    def __contains__(self, child: T) -> bool:
        return self[child] is not None

    def __getitem__(self, child: T) -> Optional['TrieNode[T]']:
        if self.children is not None:
            for node in self.children:
                if node.data == child:
                    return node

    def __setitem__(self, child: T, grandchild: Optional[T] = None) -> None:
        if self.children is None:
            self.children = set()

        if node := self[child]:
            node[grandchild] = None

        else:
            node = TrieNode(data=child)
            self.children.add(node)
            # node.parent = self

            if grandchild is not None:
                node[grandchild] = None


@dataclass
class Trie(Generic[T]):
    root: TrieNode[T] = None

    def traverse(self, mode: str = 'bfs') -> Iterator[T]:
        if mode == 'bfs':
            return self._traverse_bfs()
        raise ValueError

    def _traverse_bfs(self) -> Iterator[T]:
        queue: List[TrieNode[T]] = list()
        queue.append(self.root)
        while len(queue) > 0:
            node = queue.pop(0)
            yield node.data
            if node.children is not None:
                queue.extend(node.children)

'''
def build_trie_1(words: List[str]):
    trie = dict()
    for word in words:
        cursor = trie
        for char in word:
            if char not in cursor:
                cursor[char] = dict()
            cursor = cursor[char]
    return trie
'''


def build_trie(words: List[str]) -> Trie[chr]:
    trie = Trie(root=TrieNode(data=None))
    for word in words:
        cursor = trie.root
        for char in word:
            if char not in cursor:
                cursor[char] = None
            cursor = cursor[char]
    return trie


def group_strings(words: List[str]):
    trie = build_trie(words)
    for x in trie.traverse():
        print(x)


if __name__ == '__main__':
    words = ['foo_bar_xyz', 'foo_bar_abc']
    group_strings(words)

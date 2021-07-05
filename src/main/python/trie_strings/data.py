from dataclasses import dataclass, field
from typing import Dict, Generic, Iterator, List, Optional, Tuple, TypeVar

T = TypeVar('T')


@dataclass
class TrieNode(Generic[T]):
    data: T
    children: Dict[T, 'TrieNode[T]'] = field(default_factory=dict)

    def __contains__(self, child: T) -> bool:
        return self[child] is not None

    def __getitem__(self, child: T) -> Optional['TrieNode[T]']:
        return self.children.get(child)

    def __setitem__(self, child: T, grandchild: Optional[T] = None) -> None:
        if child not in self.children:
            self.children[child] = TrieNode(data=child)

        if grandchild is not None:
            self[child][grandchild] = None

    def __len__(self) -> int:
        return len(self.children)


@dataclass
class Trie(Generic[T]):
    root: TrieNode[T] = field(default_factory=lambda: TrieNode(data=None))

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
            queue.extend(node.children.values())

    def iter_paths(self) -> Iterator[Tuple[T, ...]]:
        queue: List[Tuple[T, ...]] = list()
        queue.append(tuple([self.root]))
        while len(queue) > 0:
            path = queue.pop(0)
            node = path[-1]
            if len(node) == 0:
                yield path
            for child in node.children.values():
                next_path = path + tuple([child])
                queue.append(next_path)


if __name__ == '__main__':
    root = TrieNode(data='.')
    root['0'] = 'a'
    root['0'] = 'b'
    root['1'] = 'x'
    root['1'] = 'y'
    print(root)

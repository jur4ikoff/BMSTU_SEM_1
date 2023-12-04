from functools import lru_cache


def findRotateSteps(ring: str, key: str) -> int:
    @lru_cache(None)
    def dfs(ring: str, index: int) -> int:
        if index == len(key):
            return 0

        count = 10 ** 9

        for i, r in enumerate(ring):
            if r == key[index]:
                minRotates = min(i, len(ring) - i)
                newRing = ring[i:] + ring[:i]
                remainingRotates = dfs(newRing, index + 1)
                count = min(count, minRotates + remainingRotates)

        return count

    return dfs(ring, 0) + len(key)


print(findRotateSteps('nyngl', 'yyynnnnnnlllggg'))

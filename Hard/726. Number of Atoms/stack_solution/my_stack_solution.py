class Solution:
    def _getCount(self, s: str, idx: int) -> str:
        countStr = ""
        while idx < len(s) and s[idx].isdigit():
            countStr += s[idx]
            idx += 1

        cnt = int(countStr) if countStr else 1
        return cnt, idx

    def countOfAtoms(self, formula: str) -> str:
        currIdx = 0
        stack = [defaultdict(int)]

        while currIdx < len(formula):
            char = formula[currIdx]

            match char:
                case "(":
                    stack.append(defaultdict(int))
                    currIdx += 1

                case ")":
                    cnt, currIdx = self._getCount(s=formula, idx=currIdx + 1)

                    currMap = stack.pop()
                    currMap = {ele: eleCnt * cnt for ele, eleCnt in currMap.items()}

                    lastAtomCntMap = stack[-1]
                    for element, count in currMap.items():
                        lastAtomCntMap[element] += count

                case char if char.isupper():
                    currIdx += 1

                    element = char
                    while currIdx < len(formula) and formula[currIdx].islower():
                        element += formula[currIdx]
                        currIdx += 1

                    cnt, currIdx = self._getCount(s=formula, idx=currIdx)
                    stack[-1][element] += cnt

                case _:
                    raise Exception("Get unexpected character case in formula.")

        charCntSortedList = sorted([(char, cnt) for char, cnt in stack[-1].items()])

        ans = ""
        for char, cnt in charCntSortedList:
            ans += char
            if cnt > 1:
                ans += str(cnt)

        return ans

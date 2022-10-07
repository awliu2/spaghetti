from typing import List

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        need = {}
        for ch in target:
            need[ch] = 1 + need.get(ch, 0)
        print(need)
        
        sticker_dict = {}
        for sticker in stickers:
            sticker_dict[sticker] = {}
            for ch in sticker:
                sticker_dict[sticker][ch] = 1 + sticker_dict[sticker].get(ch, 0)
        
        print(sticker_dict)


stickers= ["with","example","science"]
target = "thehat"


print(Solution().minStickers(stickers, target))


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        nroom=len(rooms)
        keys={0}
        def dfs(room):
            for key in rooms[room]:
                if key in keys:
                    continue
                keys.add(key)
                dfs(key)

        dfs(0)
        if len(keys)<nroom:
            return False
        return True

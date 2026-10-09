from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.storage_dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage_dict[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        
        current_list = self.storage_dict.get(key, [])
        result: str = ""
        left_pointer, right_pointer = 0, len(current_list) - 1
        
        while left_pointer <= right_pointer:
            middle_pointer = (left_pointer + right_pointer) // 2

            if current_list[middle_pointer][1] == timestamp:
                return current_list[middle_pointer][0]
            elif current_list[middle_pointer][1] < timestamp:
                result = current_list[middle_pointer][0]
                left_pointer = middle_pointer + 1
            else: right_pointer = middle_pointer - 1
        return result





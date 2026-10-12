class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([f"<delimiter>{s}" for s in strs])


    def decode(self, s: str) -> List[str]:
        return s.split("<delimiter>")[1:]

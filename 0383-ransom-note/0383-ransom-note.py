class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_letters = set(ransomNote)

        for letter in ransom_letters:
            if magazine.count(letter) < ransomNote.count(letter):
                return False
        
        return True


        
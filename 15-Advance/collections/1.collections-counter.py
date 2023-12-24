import collections
class Solution:
    def countCharacter(self, notes):
        counter_for_notes = collections.Counter(notes)
        print(counter_for_notes)

# counter is counting the charater
# here a is 16 occurs and b is 4 occurs
ab = "aabaaaaabaaabaaaabaa"
alphabets = ["s","t","w","s","w","p","m","s"]
string = "hello sweetie"
name = "Md. Shahadot Hosen"

test = Solution()
test.countCharacter(ab)
test.countCharacter(alphabets)
test.countCharacter(string)
test.countCharacter(name)

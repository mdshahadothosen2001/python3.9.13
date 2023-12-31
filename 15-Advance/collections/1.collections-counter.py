from collections import Counter

class Solution:
    def countCharacter(self, notes): 
        return Counter(notes)
    
    def counterAccessing(self, counted, item):
        return counted[item]
    
    def counterElements(self, counted):
        return counted.elements()
    
    def counterMostCommonElement(self, counted):
        return counted.most_common()
    
    def counterOperations(self, counted1, counted2):
        union = counted1 + counted2 
        difference = counted1 - counted2 
        intersection = counted1 & counted2
        return {'union':union, "difference":difference, "intersection":intersection}
    
    def counterUpdate(self, counted, note2):
        return counted.update(note2)
    
    def counterSubtract(self, counted, note1):
        return counted.subtract(note1)
    
    def counterClear(self, counted):
        return counted.clear()


# counter is counting the charater
# here a is 16 occurs and b is 4 occurs
ab = "aabaaaaabaaabaaaabaa"
alphabets = ["s","t","w","s","w","p","m","s"]
name = "Md. Shahadot Hosen"
greeting = "Hello"
nums = [1, 2, 3, 1, 2, 1, 4, 5]

checker = Solution()

counted_name = checker.countCharacter(name)
counted_alphabet =checker.countCharacter(alphabets)
counted = checker.countCharacter(nums)
print("counted char", counted)

accessing_item = checker.counterAccessing(counted, 4)
print("number of occurs of 4", accessing_item)

elements = checker.counterElements(counted)
print("diplay elements", elements)

most_common_elements = checker.counterMostCommonElement(counted)
print("most common elements", most_common_elements)

counter_operation = checker.counterOperations(counted_name, counted_alphabet)
print(counter_operation)

counter_update = checker.counterUpdate(counted_name, greeting)
print(counted, counted_name, counter_update)

counter_subtract = checker.counterSubtract(counted_name, ab)
print(counted_name, counter_subtract)

counter_clear = checker.counterClear(counted)
print("After clear th counter", counted)

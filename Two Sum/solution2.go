func twoSum(nums []int, target int) []int {
    var length int = len(nums) - 1
    hashmap := make(map[int]int)
    for i:= 0; i <= length; i++ {
        var k int = target - nums[i]
        if value, ok := hashmap[k]; ok {
            return []int{i, value}
        }
        hashmap[nums[i]] = i
    }
    return []int{}
}

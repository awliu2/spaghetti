package main
import "fmt"

func main(){
	fmt.Println(twoSum([]int{1,2,3}, 5))
}

func twoSum(nums []int, target int) []int {

	var rv []int
	var ht = make(map[int]int)

	for i, n := range nums {
		if val, ok := ht[n]; ok{
			rv = append(rv, val, i)
			break
		}
		ht[target - n] = i

	}
	fmt.Println(ht)
	return rv
}
package main

import "fmt"

func main(){
	fmt.Println(productExceptSelf([]int{1,2,3}))
}

func productExceptSelf(nums []int) []int {

	lenN := len(nums)

	rv := make([]int, lenN)
    for i := range rv {
		rv[i] = 1
	}

	l,r := 1,1
	
	for i := 0; i < lenN; i++  {
		rv[i] *= l
		rv[lenN - 1 - i] *= r
		l *= nums[i]
		r *= nums[lenN - 1 - i]
	}
	return rv
}

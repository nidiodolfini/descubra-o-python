function getSecondLargest(nums) {
    // Complete the function
    let largest = nums[0];
    let secondLargest = nums[0];
    
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] > largest) {
            secondLargest = largest;
            largest = nums[i];
            continue;
        }
        console.log("s",secondLargest)
        console.log('l',largest)
        if ((nums[i] > secondLargest) && (nums[i] < largest)) {
            secondLargest = nums[i];
        }
    }
    
    return secondLargest;
}

console.log(getSecondLargest('2 3 6 6 5'))
function threeSumClosest(nums: number[], target: number): number {
    let sum = 0;
    if (nums.length == 3) {
        for (let i = 0; i < 3; i++) {
            sum += nums[i];
        }
        return sum;
    }
    let sortedNums: number[] = nums.sort((n1, n2) => n1 - n2),
        prevJ = null,
        prevK = null,
        diff = 10000,
        result = 0;
    for (let i = 0; i < sortedNums.length - 2; i++) {
        prevJ = null;
        for (let j = i + 1; j < sortedNums.length - 1; j++) {
            if (prevJ != null && prevJ == sortedNums[j]) {
                continue;
            }
            prevJ = sortedNums[j];
            let left = j + 1,
                right = sortedNums.length - 1,
                middle = 0;
            while (left <= right) {
                middle = Math.floor((left + right) / 2);
                sum = sortedNums[i] + sortedNums[j] + sortedNums[middle];
                if (sum - target > 0) {
                    right = middle - 1;
                } else {
                    left = middle + 1;
                }
                if (Math.abs(sum - target) < diff) {
                    diff = Math.abs(sum - target);
                    result = sum;
                }
            }
        }
    }
    return result;
};
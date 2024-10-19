
/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let newArr = []
    for (let i=0; i<arr.length; i++) {
        if (Boolean(fn(arr[i], i))) {
            newArr.push(arr[i])
        }         
    }
    return newArr
};

//console.log(filter([1,2,3,4,5,6,7,8,9], (n) => n > 10)) //->Test
//42ms 48.50Mb (96.46% 92.75%)
/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    results = {}

    return function(...args) {
        const argsStringify = JSON.stringify(args);
        if (argsStringify in results) {
            return results[argsStringify]
        } else {
            res = fn(...args)
            results[argsStringify] = res
            return res
        }
    }
}

/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */

//300ms 85.51Mb (54.67% 93.86%)
/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
    var hasBeenCalled = false
    return function(...args){
        if (!hasBeenCalled) {
            hasBeenCalled = true
            return fn(...args)
        }
    }
};


/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */

//49ms 49.01Mb (75.22% 24.13%)
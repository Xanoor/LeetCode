/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function (promise1, promise2) {
    return promise1.then((e) => promise2.then((e2) => e + e2));
};

// addTwoPromises(Promise.resolve(2), Promise.resolve(2)).then(console.log); // 4
// 59ms 49.89Mb

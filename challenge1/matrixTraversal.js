

let n = 6;

let matrix = Array.from({ length: n }, () =>
  Array.from({ length: n }, () => Math.floor(Math.random() * 10))
);

console.log(matrix);




function spiralOrder(matrix) {
    const n = matrix.length;
    const  result = [];

    let top = 0;
    let bottom = n - 1;
    let left = 0;
    let right = n - 1;

    while (top <= bottom && left <= right) {
        for (let col = left; col <= right; col++) {
            result.push(matrix[top][col]);
        }
        top++;

        for (let row = top; row <= bottom; row++) {
            result.push(matrix[row][right]);
        }
        right--;

        for (let col = right; col >= left; col--) {
            result.push(matrix[bottom][col]);
        }
        bottom--;

        for (let row = bottom; row >= top; row--) {
            result.push(matrix[row][left]);
        }
        left++;
    }
    return result;
}

console.log(spiralOrder(matrix));
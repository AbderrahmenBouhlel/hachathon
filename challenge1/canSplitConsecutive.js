

function canSplitConsecutive(ch) {
    const n = ch.length;
    for (let len = 1 ; len <= Math.floor(n / 2); len++) {
        let firstStr = ch.slice(0,len);

        if (firstStr[0] === '0' && firstStr.length > 1) continue;

        let first = parseInt(firstStr,10);
        let pointer = len ;
        let next = first + 1;


        while (pointer <= n){
            let nextStr = next.toString();
            let nextLen = nextStr.length;

            let sub = ch.slice(pointer, pointer + nextLen);

            if (sub !== nextStr) {
                break; 
            }

            pointer += nextLen;
            next += 1;
        }

        if (pointer === n) {
            return true;
        }
    }

    
    return false;
}

console.log(canSplitConsecutive("99100"));        
console.log(canSplitConsecutive("979899100101"));
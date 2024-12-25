const isArmstrongNumber = (number) => {
    var numberString = number.toString();
    var numDigits = numberString.length;
    var sum = 0;
    
    for(let i=0;i<numDigits;i++)
    {
        sum += Math.pow(parseInt(numberString[numDigits-i-1]),i);
    }
    return sum == number;
    
    //throw new Error('Remove this statement and implement this function');
};

let d = 5869;
console.log(isArmstrongNumber(d));
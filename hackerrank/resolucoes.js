function Rectangle(a, b) {
//    var length = a;
//    var width = b;
//    var perimeter = 2 * (length + width);
//    var area = length * width;
//    console.log(length);
//    console.log(width);
//    console.log(perimeter);
//   console.log(area);

    var rectangle = {
        length: a,
        width: b,
        perimeter: 2 * (a + b),
        area: a * b
    }
    return rectangle;

}

console.log(Rectangle(4, 5))
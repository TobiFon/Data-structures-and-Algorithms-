function selectionSort(list) {
  for (let i = 0; i < list.length -1; i++) {
    let lowestNumberIndex = i;
    for (let j = i + 1; j < list.length; j++) {
      if (list[j] < list[lowestNumberIndex]) {
        lowestNumberIndex = j;
      }
    }
    if (lowestNumberIndex != i) {
      let temp;
      temp = list[i];
      list[i] = list[lowestNumberIndex];
      list[lowestNumberIndex] = temp;
    }
  }
  return list
}

console.log(selectionSort([333, 17, 753, 80, 202]))
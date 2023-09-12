exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, element) => {
    if (element === searchElement) {
      return count + 1;
    }
    return count;
  }, 0);
};

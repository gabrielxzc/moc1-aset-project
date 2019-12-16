export const range = (start, end) => {
  const x = [];

  for (let i = start; i < end; ++i) {
    x.push(i);
  }

  return x;
};

export const randomInt = (min, max) => {
  min = Math.ceil(min);
  max = Math.floor(max);

  return Math.floor(Math.random() * (max - min + 1)) + min;
};

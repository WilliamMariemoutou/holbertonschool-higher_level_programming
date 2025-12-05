#!/usr/bin/node

const args = process.argv.slice(2).map(x => parseInt(x, 10));

if (args.length < 2) {
  console.log(0);
} else {
  let max = Math.max(...args);
  let filtered = args.filter(n => n !== max);
  console.log(filtered.length === 0 ? 0 : Math.max(...filtered));
}

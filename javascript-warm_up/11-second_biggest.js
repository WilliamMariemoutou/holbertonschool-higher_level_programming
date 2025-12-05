#!/usr/bin/node

const args = process.argv.slice(2).map(x => parseInt(x, 10));

if (args.length < 2) {
  console.log(0);
} else {
  const max = Math.max(...args);
  const filtered = args.filter(n => n !== max);
  console.log(filtered.length === 0 ? 0 : Math.max(...filtered));
}

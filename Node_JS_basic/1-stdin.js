console.log('Welcome to Holberton School, what is your name?');
process.stdin.on('readable', () => {
    const data = process.stdin.read();
    if (data != null) process.stdout.write(`Your name is: ${data.toString()}`);
});

process.stdin.on('end', () => {
    process.stdout.write('This important software is now closing\n');
});
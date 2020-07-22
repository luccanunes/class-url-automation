const venom = require('venom-bot');

venom.create().then((client) => start(client));

function start(client) {
    const zoom = process.argv[2]
    const pdf = process.argv[3]
    client.onMessage((message) => {
        if (message.body.toLowerCase() === 'zoom') {
            client.sendText(message.from, zoom);
        }
        if (message.body.toLowerCase() === 'pdf') {
            client.sendText(message.from, pdf);
        }
    });
}
